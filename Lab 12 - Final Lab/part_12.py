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


# Create a class for each level:
class Level:
    """
    Each level will have its own wall list, blue and green gem list, gear list, and enemy list.
    """

    def __init__(self):
        self.player_list = None
        self.wall_list = None
        self.blue_gem_list = None
        self.green_gem_list = None
        self.gear_list = None
        self.enemy_list = None
        self.portal_list = None
        self.gear_req = 0


def setup_level_0():
    level = Level()

    # Sprites in the default level, 0:
    level.player_list = arcade.SpriteList()
    level.wall_list = arcade.SpriteList()
    level.blue_gem_list = arcade.SpriteList()
    level.green_gem_list = arcade.SpriteList()
    level.gear_list = arcade.SpriteList()
    level.enemy_list = arcade.SpriteList()
    level.portal_list = arcade.SpriteList()
    level.color = arcade.color.PINK

    # Gear count required to access portal to next level:
    level.gear_req = 1

    # Start by placing the bottom border:
    for x in range(0, 20):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = x * 64
        border_wall.center_y = 0
        level.wall_list.append(border_wall)
    # Here's the top border:
    for x in range(0, 20):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = x * 64
        border_wall.center_y = 960
        level.wall_list.append(border_wall)
    # Place left border.
    for y in range(1, 15):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = 0
        border_wall.center_y = y * 64
        level.wall_list.append(border_wall)
    # Place the right border.
    for y in range(1, 15):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = 1216
        border_wall.center_y = y * 64
        level.wall_list.append(border_wall)

    # Put out some blue gems for the default level.
    coordinate_list = [[5, 5],
                       [8,9]]
    for coordinate in coordinate_list:
        blue_gem = arcade.Sprite(":resources:images/items/gemBlue.png", GEM_SPRITE_SCALING)
        blue_gem.center_x = coordinate[0]*64
        blue_gem.center_y = coordinate[1]*64
        level.blue_gem_list.append(blue_gem)

    # Put out some green gems.
    coordinate_list = [[2, 9],
                       [8,2]]
    for coordinate in coordinate_list:
        green_gem = arcade.Sprite(":resources:images/items/gemGreen.png", GEM_SPRITE_SCALING)
        green_gem.center_x = coordinate[0]*64
        green_gem.center_y = coordinate[1]*64
        level.green_gem_list.append(green_gem)

    # Put out the gears.
    coordinate_list = [[11, 5],
                       [5,12]]
    for coordinate in coordinate_list:
        gear = arcade.Sprite(":resources:images/enemies/saw.png", GEAR_SPRITE_SCALING)
        gear.center_x = coordinate[0]*64
        gear.center_y = coordinate[1]*64
        level.gear_list.append(gear)

    # Set out some boxes.
    coordinate_list = [[3, 7],
                       [7, 2]]
    for coordinate in coordinate_list:
        box = arcade.Sprite(":resources:images/tiles/boxCrate.png", BOX_SPRITE_SCALING)
        box.center_x = coordinate[0]*64
        box.center_y = coordinate[1]*64
        level.wall_list.append(box)

    # Put out some robots for the default level enemies.
    coordinate_list = [[6, 6],
                       [10, 10]]
    for coordinate in coordinate_list:
        robo = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", ENEMY_SPRITE_SCALING_1)
        robo.center_x = coordinate[0]*64
        robo.center_y = coordinate[1]*64
        level.enemy_list.append(robo)

    # Place the portal to the next level.
    # This requires a certain number of gears to activate.
    portal = arcade.Sprite(":resources:images/tiles/lockRed.png", PORTAL_SPRITE_SCALING)
    portal.center_x = 8*64
    portal.center_y = 4*64
    level.portal_list.append(portal)


    return level

def setup_level_1():
    level = Level()

    # Sprites in the next level, 1:
    level.player_list = arcade.SpriteList()
    level.wall_list = arcade.SpriteList()
    level.blue_gem_list = arcade.SpriteList()
    level.green_gem_list = arcade.SpriteList()
    level.gear_list = arcade.SpriteList()
    level.enemy_list = arcade.SpriteList()
    level.portal_list = arcade.SpriteList()
    level.color = arcade.color.DODGER_BLUE

    # Gear count required to access portal to next level:
    level.gear_req = 2

    # For now, the room is built the same.  Update this for new shapes.
    # Start by placing the bottom border:
    for x in range(0, 20):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = x * 64
        border_wall.center_y = 0
        level.wall_list.append(border_wall)
    # Here's the top border:
    for x in range(0, 20):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = x * 64
        border_wall.center_y = 960
        level.wall_list.append(border_wall)
    # Place left border.
    for y in range(1, 15):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = 0
        border_wall.center_y = y * 64
        level.wall_list.append(border_wall)
    # Place the right border.
    for y in range(1, 15):
        border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
        border_wall.center_x = 1216
        border_wall.center_y = y * 64
        level.wall_list.append(border_wall)

    # Put out some blue gems for the default level.
    coordinate_list = [[19, 15],
                       [18, 3]]
    for coordinate in coordinate_list:
        blue_gem = arcade.Sprite(":resources:images/items/gemBlue.png", GEM_SPRITE_SCALING)
        blue_gem.center_x = coordinate[0]*64
        blue_gem.center_y = coordinate[1]*64
        level.blue_gem_list.append(blue_gem)

    # Put out some green gems.
    coordinate_list = [[1, 2],
                       [3, 9]]
    for coordinate in coordinate_list:
        green_gem = arcade.Sprite(":resources:images/items/gemGreen.png", GEM_SPRITE_SCALING)
        green_gem.center_x = coordinate[0]*64
        green_gem.center_y = coordinate[1]*64
        level.green_gem_list.append(green_gem)

    # Put out the gears.
    coordinate_list = [[3, 10],
                       [14, 2]]
    for coordinate in coordinate_list:
        gear = arcade.Sprite(":resources:images/enemies/saw.png", GEAR_SPRITE_SCALING)
        gear.center_x = coordinate[0]*64
        gear.center_y = coordinate[1]*64
        level.gear_list.append(gear)

    # Set out some boxes.
    coordinate_list = [[13, 7],
                       [17, 2]]
    for coordinate in coordinate_list:
        box = arcade.Sprite(":resources:images/tiles/boxCrate.png", BOX_SPRITE_SCALING)
        box.center_x = coordinate[0]*64
        box.center_y = coordinate[1]*64
        level.wall_list.append(box)

    # Put out some robots for the default level enemies.
    coordinate_list = [[16, 6],
                       [4, 10]]
    for coordinate in coordinate_list:
        robo = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", ENEMY_SPRITE_SCALING_1)
        robo.center_x = coordinate[0]*64
        robo.center_y = coordinate[1]*64
        level.enemy_list.append(robo)

    # Only have a portal in the final level if there's another level to go to, or the game breaks.
    # # Place the portal to the next level.
    # # This requires a certain number of gears to activate.
    # portal = arcade.Sprite(":resources:images/tiles/lockRed.png", PORTAL_SPRITE_SCALING)
    # portal.center_x = 15 * 64
    # portal.center_y = 14 * 64
    # level.portal_list.append(portal)

    arcade.set_background_color(arcade.color.PINK)

    return level


class MyGame(arcade.Window):
    """ Making my game. """

    def __init__(self, width, height, title):
        """ Initializer """
        super().__init__(width, height, title, resizable=True)

        # My sprite lists
        self.player_list = None
        self.wall_list = None
        self.blue_gem_list = None
        self.green_gem_list = None
        self.gear_list = None
        self.enemy_list = None

        # Set up the player stuff
        self.player_sprite = None
        self.levels = None
        self.current_level = 1
        self.green_gem_count = 0
        self.blue_gem_count = 0
        self.gear_count = 0
        self.gear_req = 0

        # To refine combat, info about combos will have to go here.  At first, combat is won just by collision.

        # Physics engine setup:
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

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

        self.level = 0
        self.green_gem_count = 0
        self.blue_gem_count = 0
        self.gear_count = 0

        # Set up the player.

        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png", PLAYER_SPRITE_SCALING)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        # Set up the list into which I shall add my levels.
        self.levels = []

        # Set up level 0, the default level.
        level = setup_level_0()
        self.levels.append(level)

        # Set up level 1.
        level = setup_level_1()
        self.levels.append(level)

        # Starting level:
        self.current_level = 0

        # Set up the physics engine for this level:
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)

        self.gear_req = self.levels[self.current_level].gear_req

        # Set the background color
        arcade.set_background_color(arcade.color.DIM_GRAY)

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
                                     40,
                                     arcade.color.ALMOND)
        output = "gear count: " + str(self.gear_count) + "   gear req: " + str(self.levels[self.current_level].gear_req)
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 20)
        arcade.draw_text("current level: " + str(self.current_level), 350, 10, arcade.color.BLACK, 10)

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
        blue_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.levels[self.current_level].blue_gem_list)
        green_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.levels[self.current_level].green_gem_list)
        gear_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.levels[self.current_level].gear_list)
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
        enemy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        # Do stuff when an enemy is hit.  At first, just remove it, like a collected item.  Add combat later.
        for robo in enemy_hit_list:
            robo.remove_from_sprite_lists()
            arcade.play_sound(self.robo_sound)




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
        portal_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.levels[self.current_level].portal_list)
        for portal in portal_hit_list:
            if self.gear_count > self.levels[self.current_level].gear_req:
                portal.remove_from_sprite_lists()
        if len(portal_hit_list)>0 and self.gear_count >= self.gear_req:
            self.current_level += 1
            self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.levels[self.current_level].wall_list)
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

    def on_resize(self, width, height):

        """
        Handle the user grabbing the edge and resizing the window.
        """

        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))

def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()