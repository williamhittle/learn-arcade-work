"""
Building my sprite lab from scratch.  Let's do this!
This is a basic version.  I would like to update the sprites and add more types of movement.
This meets the lab requirements, though, and I'm pressed for time.
"""

import arcade
import random

# Define some constants

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
SCALE_PLAYER = .7
SCALE_SPRITE_GOOD = .5
SCALE_SPRITE_BAD = .3
BAD_SPRITE_COUNT = 20
GOOD_SPRITE_COUNT = 20


# Set up a class for my bad sprites (bombs) and another for my good sprites (gems)
class Bomb(arcade.Sprite):

    def reset_position(self):
        """ Reset the bomb position.  Currently above the top of the screen.
        To be called when the sprite reaches the bottom of the screen or collides with the player."""
        self.center_y = random.randrange(SCREEN_HEIGHT + 10,
                                         SCREEN_HEIGHT + 40)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        """ Bomb movement! """
        self.center_y -= 1

        # Check for moving off-screen, and if so, call the reset position function above.
        if self.top < 0:
            self.reset_position()


class Gem(arcade.Sprite):

    def reset_position(self):
        """ Reset the gem position.  Currently just moving gems back to the left of the screen.
        To be called when the sprite goes off the screen to the right. """
        self.right = 0

    def update(self):
        """ Gem movement! """
        self.center_x += 1

        # Check for moving off-screen.  Remember to use "left, right, top, and bottom" of sprites.
        # That will make it seem like the sprite moves only after the last bit of it is visible.
        # Don't reset these to random, because I like them to be the same ol' gems.
        if self.left > SCREEN_WIDTH:
            self.reset_position()

# Set up my game class


class MyGame(arcade.Window):
    """ subclass the built-in arcade window class to inherit its functionality. """
    def __init__(self):
        """ Initialize! """
        # Always call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        # Variables for my sprites go here.
        self.player_list = None
        self.good_sprite_list = None
        self.bad_sprite_list = None

        # Info about the player goes here.
        self.player_sprite = None
        self.score = 0

        # I want to hide the mouse cursor, and I can do that here, too.
        self.set_mouse_visible(False)

        # Set the background color of the game here.
        arcade.set_background_color(arcade.color.WHITE)

        # Include sounds for good and bad things.
        self.gem_sound = arcade.load_sound(":resources:sounds/coin5.wav")
        self.bomb_sound = arcade.load_sound(":resources:sounds/explosion1.wav")

    def setup(self):
        """ Set up game and initialize variables. """

        # Sprite lists go here.  These are instances of the built-in SpriteList class.
        self.player_list = arcade.SpriteList()
        self.good_sprite_list = arcade.SpriteList()
        self.bad_sprite_list = arcade.SpriteList()

        # Initialize the score variable.
        self.score = 0

        # Set up the player.  For now, use built-in sprites, but update this later to be cooler.
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", SCALE_PLAYER)
        self.player_sprite.center_x = 75
        self.player_sprite.center_y = 125
        self.player_list.append(self.player_sprite)

        # Set up the Bad Sprites (bombs for now - create better sprites and include them later).
        for i in range(BAD_SPRITE_COUNT):

            # Create the bombs
            bomb = Bomb(":resources:images/tiles/bomb.png", SCALE_SPRITE_BAD)

            # Position the bombs
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the bomb to the bomb sprite list
            self.bad_sprite_list.append(bomb)

        # Set up the Good Sprites (gems for now).
        for i in range(GOOD_SPRITE_COUNT):

            # Create the gems
            gem = Gem(":resources:images/items/gemBlue.png", SCALE_SPRITE_GOOD)

            # Position the gems
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the gem to the gem sprite list
            self.good_sprite_list.append(gem)

    def on_draw(self):
        """ Draw stuffs! """

        arcade.start_render()

        # Draw all the sprites in my lists using the sprite list built-in draw function.
        self.bad_sprite_list.draw()
        self.good_sprite_list.draw()
        self.player_list.draw()

        # This game has a score based on sprites collected, so put that on the screen.
        # I'm not going to use 'string formatting' because I don't understand that yet.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.BLACK, 14)

        # Draw Game Over when there are no more gems to collect.
        if len(self.good_sprite_list) == 0:
            arcade.draw_text("Game Over!  You collected all the gems.  You're final score was " + str(self.score) + ".",
                             100, 200, arcade.color.BLACK, 20)

    def on_mouse_motion(self, x, y, dx, dy):
        """ How to do stuff based on mouse motion input """

        # Make sure the player sprite moves to the mouse position, so long as the game isn't over.
        if len(self.good_sprite_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Things be moving, yo! """

        # Update all the sprite lists using their update methods, so long as there are good sprites to collect.
        if len(self.good_sprite_list) > 0:
            self.good_sprite_list.update()
            self.bad_sprite_list.update()

        # Find out which sprites have collided with the player.
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprite_list)
        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprite_list)

        # Loop through those lists and remove/update the sprites that have been hit.
        # Make sure to adjust the score as appropriate for each kind.
        for bomb in bad_hit_list:
            # I want the bombs to get reset, so they can always get in the way.
            bomb.reset_position()
            self.score += -1
            arcade.play_sound(self.bomb_sound)
        for gem in good_hit_list:
            # I want gems to be removed, so they can only be collected once.  When the list is empty, you win!
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)


def main():
    """ The main method goes here. """
    window = MyGame()
    window.setup()
    arcade.run()


# I don't remember why this is how we call the main function; remember to ask.
if __name__ == "__main__":
    main()
