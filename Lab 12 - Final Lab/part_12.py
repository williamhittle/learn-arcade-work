"""
IDEA:
basic:
You are a person trying to escape.
You start in one room with enemies and a locked door.
To unlock the door, you need parts.
You collect parts by picking them up or defeating robot enemies.
Once you have enough parts, you can unlock the door and move on.

better:
There are multiple rooms with enemies that get progressively harder to defeat.
Combat involves timed button presses.
Successful combos increase the damage output of your combos, making combat easier.

best:
The rooms aren't static, and involve a large maze, so that you need to navigate to find extra things.
Gems can be collected to increase your stats as well.
Enemies don't just sit around waiting for you to bump into them and attack.  They move and counter-attack.
"""

import arcade
from pyglet.math import Vec2

# Import my levels, saved in other files to save space in this code.
# (Also, it theoretically makes it easier to create a level then pull it in here.)
# Those files have the Level class built into them, so I can pull in any of them I want.

import map0
import map1
import map2

# Define some constants

PLAYER_SPRITE_SCALING = 0.45
BORDER_SPRITE_SCALING = 0.5
BOX_SPRITE_SCALING = 0.5
GEM_SPRITE_SCALING = 0.5
GEAR_SPRITE_SCALING = 0.5
ENEMY_SPRITE_SCALING_1 = 0.5
ENEMY_SPRITE_SCALING_2 = 1.0
PORTAL_SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Final Lab: Escape from ROBO-jail"

# I want some maps to get big enough that the player moves around, so I'll need some camera stuff.
# This is the pixel count between character and edge of screen.
VIEWPOINT_MARGIN = 220

# This is how fast the camera pans to the player.  (1.0 is instant.)
CAMERA_SPEED = 0.1

# This is how fast the character moves.
PLAYER_MOVEMENT_SPEED = 7


# Create a start screen with instructions:
class InstructionView(arcade.View):
    """ Class to handle the start screen. """

    def on_show_view(self):
        """ Called when switching to this view.  Should happen after advancing from game over screen."""
        arcade.set_background_color(arcade.color.WHITE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def on_draw(self):
        """ Draw the start screen. """
        self.clear()
        arcade.draw_text("Escape from ROBO-prison", 150, 400, arcade.color.BLACK, font_size=30)
        arcade.draw_text("Press the space bar to begin. ", 50, 300, arcade.color.BLACK, font_size=20)
        arcade.draw_text("Hitting robots will reduce your hit points. ", 50, 200, arcade.color.BLACK, font_size=20)
        arcade.draw_text("Run out of hit points and it's Game Over. ", 50, 100, arcade.color.BLACK, font_size=20)

    def on_key_press(self, key, _modifiers):
        """ The button to go from the start screen to the game. Can have other secret options. """
        if key == arcade.key.SPACE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)


# Create the game over screen:
class GameOverView(arcade.View):
    """ This is what the player sees when they encounter a robot. """

    def __init__(self):
        """ Here is what happens when we switch to this view. """
        super().__init__()
        arcade.set_viewport(0, DEFAULT_SCREEN_WIDTH - 1, 0, DEFAULT_SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view. """
        self.clear()
        arcade.draw_text("Game over.", 150, 400, arcade.color.BLACK, font_size=30)
        arcade.draw_text("Press escape to restart the game. ", 50, 200, arcade.color.BLACK, font_size=20)

    def on_key_press(self, key, _modifiers):
        """ The button to press to go back to the first level.  Again, potential secrets here. """
        if key == arcade.key.ESCAPE:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)


class VictoryView(arcade.View):
    """ This is the screen you see when you escape. """

    def __init__(self):
        """ Set it up. """
        super().__init__()
        arcade.set_viewport(0, DEFAULT_SCREEN_WIDTH - 1, 0, DEFAULT_SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw the view. """
        self.clear()
        arcade.draw_text("You escaped!", 150, 400, arcade.color.BLACK, font_size=30)
        arcade.draw_text("Press escape to go back to the start screen and play again. ", 50, 200, arcade.color.BLACK,
                         font_size=20)

    def on_key_press(self, key, _modifiers):
        """ The button to press to go back to the start menu.  Secrets! """
        if key == arcade.key.ESCAPE:
            game_view = InstructionView()
            self.window.show_view(game_view)


# Create the game itself:
class GameView(arcade.View):
    """ Making my game. """

    def __init__(self):
        """ Initializer """
        super().__init__()

        # My sprite lists
        self.player_list = None
        self.wall_list = None
        self.blue_gem_list = None
        self.green_gem_list = None
        self.gear_list = None
        self.enemy_list = None
        self.portal_list = None
        self.width = DEFAULT_SCREEN_WIDTH
        self.height = DEFAULT_SCREEN_HEIGHT

        # Set up the player stuff
        self.player_sprite = None
        self.levels = None
        self.current_level = 1
        self.green_gem_count = 0
        self.blue_gem_count = 0
        self.gear_count = 0
        self.gear_req = 0
        self.hit_points = 3

        # To refine combat, info about combos will have to go here.  At first, combat is won just by collision.
        # The simpler implementation is just to have contact return the player to level 0, or end the game.

        # Physics engine setup:
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.enter_pressed = False

        # Include sounds for gem and gear collection, and robot defeat.
        self.gem_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.gear_sound = arcade.load_sound(":resources:sounds/coin1.wav")
        self.robo_sound = arcade.load_sound(":resources:sounds/error1.wav")

        # Create the cameras: one for the GUI, one for the combat stuff, one for the sprites.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_combat = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.blue_gem_list = arcade.SpriteList()
        self.green_gem_list = arcade.SpriteList()
        self.gear_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.portal_list = arcade.SpriteList()

        # Initialize the level and other counts that are visible to the player.

        self.current_level = 0
        self.green_gem_count = 0
        self.blue_gem_count = 0
        self.gear_count = 0

        # Set up the player.

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png",
                                           PLAYER_SPRITE_SCALING)
        self.player_sprite.center_x = 1*64
        self.player_sprite.center_y = 1*64
        self.player_list.append(self.player_sprite)

        # Set up the list into which I shall add my levels.
        # Add them in order, so that the position in my levels list equals the number of the level.
        self.levels = []

        # Set up level 0, the default level.
        level = map0.setup_level_0()
        self.levels.append(level)

        # Set up level 1.
        level = map1.setup_level_1()
        self.levels.append(level)

        # Set up level 2.
        level = map2.setup_level_2()
        self.levels.append(level)

        # Set up additional levels here:

        # Set up the physics engine for this level:
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)

        # Set up the required number of gears to get through the portal of this level:
        self.gear_req = self.levels[self.current_level].gear_req

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing:
        self.clear()

        # Select the camera we'll use to draw the sprites:
        self.camera_sprites.use()

        # Draw the sprites:
        self.levels[self.current_level].wall_list.draw()
        self.levels[self.current_level].blue_gem_list.draw()
        self.levels[self.current_level].green_gem_list.draw()
        self.levels[self.current_level].gear_list.draw()
        self.levels[self.current_level].enemy_list.draw()
        self.levels[self.current_level].portal_list.draw()
        self.player_list.draw()

        # Select the un-scrolled camera for the GUI:
        self.camera_gui.use()

        # Draw the GUI info:
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     110,
                                     arcade.color.ALMOND)
        output1 = "gears: " + str(self.gear_count) + "   gears required: " +\
                  str(self.levels[self.current_level].gear_req)
        output2 = "current level: " + str(self.current_level) + "   hit points: " + str(self.hit_points)
        output3 = "blue gems: " + str(self.blue_gem_count) + "   green gems: " + str(self.green_gem_count)
        instructions1 = "Use the arrow keys to navigate the stage. "
        instructions2 = "Gather enough gears to open the locked door to the next level. "
        instructions3 = "Collect blue and green gems for points. "  # (Later they'll benefit combat.)
        arcade.draw_text(output1, 10, 30, arcade.color.BLACK, 13)
        arcade.draw_text(output2, 10, 50, arcade.color.BLACK, 13)
        arcade.draw_text(output3, 10, 10, arcade.color.BLACK, 13)
        arcade.draw_text(instructions1, 350, 50, arcade.color.BLACK, 10)
        arcade.draw_text(instructions2, 350, 30, arcade.color.BLACK, 10)
        arcade.draw_text(instructions3, 350, 10, arcade.color.BLACK, 10)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
        elif key == arcade.key.DOWN:
            self.down_pressed = True
        elif key == arcade.key.LEFT:
            self.left_pressed = True
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
        elif key == arcade.key.ENTER:
            self.enter_pressed = True

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
        elif key == arcade.key.DOWN:
            self.down_pressed = False
        elif key == arcade.key.LEFT:
            self.left_pressed = False
        elif key == arcade.key.RIGHT:
            self.right_pressed = False
        elif key == arcade.key.ENTER:
            self.enter_pressed = False

    def on_update(self, delta_time):
        """ Movement and game logic. """

        # Find out which gems and gears have collided with the player.
        blue_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.levels[self.current_level].blue_gem_list)
        green_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.levels[self.current_level].green_gem_list)
        gear_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.levels[self.current_level].gear_list)
        # Look through those lists and remove/update sprites that have been collected.
        for gem in blue_hit_list:
            gem.remove_from_sprite_lists()
            self.blue_gem_count += 1
            arcade.play_sound(self.gem_sound)
        for gem in green_hit_list:
            gem.remove_from_sprite_lists()
            self.green_gem_count += 1
            arcade.play_sound(self.gem_sound)
        for gear in gear_hit_list:
            gear.remove_from_sprite_lists()
            self.gear_count += 1
            arcade.play_sound(self.gear_sound)

        # Find out which enemies have collided with the player.
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.levels[self.current_level].enemy_list)
        # Do stuff when an enemy is hit.  At first, just remove it, like a collected item.  Add combat later.
        for robo in enemy_hit_list:
            robo.remove_from_sprite_lists()
            arcade.play_sound(self.robo_sound)
            self.hit_points -= 1
            if self.hit_points == 0:
                view = GameOverView()
                self.window.show_view(view)

        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

        # Update sprites.
        self.physics_engine.update()

        # Check if the player has collided with the portal, and erase it

        """ Insert the logic to check which level we're in, based on if the player has reached the portal with enough 
        gears.  This should increase the current level by 1, and then update stuff. """
        portal_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                               self.levels[self.current_level].portal_list)
        # Add some functionality that lets a player go back to previous levels.
        # That may require different sprites with some kind of color indication of what level you'd go back to.
        if len(portal_hit_list) > 0 and self.gear_count >= self.levels[self.current_level].gear_req:
            self.current_level += 1
            if self.current_level == 3:
                view = VictoryView()
                self.window.show_view(view)
            elif self.current_level < 3:
                # self.player_sprite.center_x = 1 * 64
                # self.player_sprite.center_y = 1 * 64
                # Use this code if you want to reset the player to a specific start point with each level.
                self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                                 self.levels[self.current_level].wall_list)
                self.gear_req = self.levels[self.current_level].gear_req
                arcade.set_background_color(self.levels[self.current_level].color)

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):

        """
        Use the scrolling code from lab 9 to scroll the window to the player.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,
                        self.player_sprite.center_y - self.height / 2)
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    # This doesn't seem to work with the View method.  Figure out why.
    # def on_resize(self, width, height):
    #
    #     """
    #     Handle the user grabbing the edge and resizing the window.
    #     """
    #
    #     self.camera_sprites.resize(int(width), int(height))
    #     self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = arcade.Window(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
