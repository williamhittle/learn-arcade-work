"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import arcade
from pyglet.math import Vec2

SPRITE_SCALING = 0.45
BORDER_SPRITE_SCALING = 0.5
BOX_SPRITE_SCALING = 0.5
GEM_SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.blue_gem_list = None
        self.green_gem_list = None

        # Set up the player stuff
        self.player_sprite = None
        self.score = 0

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # Include sound for gem collection.
        self.gem_sound = arcade.load_sound(":resources:sounds/coin5.wav")

        # Create the cameras. One for the GUI, one for the sprites.

        # We scroll the 'sprite world' but not the GUI.

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.blue_gem_list = arcade.SpriteList()
        self.green_gem_list = arcade.SpriteList()

        # Initialize the score variable that the player will see.
        self.score = 0

        # Set up the player.  I want to use the robot sprite again!
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        # -- Set up several columns of walls
        """ Built-in resources I'll use:
        :resources:images/tiles/boxCrate_single.png
        :resources:images/tiles/boxCrate_double.png
        :resources:images/tiles/boxCrate.png
        :resources:images/tiles/brickTextureWhite.png
        :resources:images/items/gemBlue.png
        :resources:images/items/gemGreen.png
        """

        # Place the out barrier that the player can't escape.  Probably a better way to code this.
        # Place bottom border.
        for x in range(0, 1280, 64):
            border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
            border_wall.center_x = x
            border_wall.center_y = 0
            self.wall_list.append(border_wall)
        # Place top border.
        for x in range(0, 1280, 64):
            border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
            border_wall.center_x = x
            border_wall.center_y = 960
            self.wall_list.append(border_wall)
        # Place left border.
        for y in range(64, 960, 64):
            border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
            border_wall.center_x = 0
            border_wall.center_y = y
            self.wall_list.append(border_wall)
        # Place the right border.
        for y in range(64, 960, 64):
            border_wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", BORDER_SPRITE_SCALING)
            border_wall.center_x = 1216
            border_wall.center_y = y
            self.wall_list.append(border_wall)

        # Place the boxes that will form the maze.
        # It'd be nice if I could import a coordinate list from a csv file or something, but I don't know how, yet.
        # This list is nasty long and painful to write, but doesn't follow a pattern other than what I drew.
        # How to speed this up?
        coordinate_list = [[704, 64],
                           [128, 128],
                           [192, 128],
                           [256, 128],
                           [320, 128],
                           [384, 128],
                           [448, 128],
                           [512, 128],
                           [576, 128],
                           [704, 128],
                           [832, 128],
                           [960, 128],
                           [1024, 128],
                           [1088, 128],
                           [128, 192],
                           [704, 192],
                           [832, 192],
                           [1024, 192],
                           [128, 256],
                           [256, 256],
                           [320, 256],
                           [576, 256],
                           [704, 256],
                           [832, 256],
                           [896, 256],
                           [1024, 256],
                           [1152, 256],
                           [576, 320],
                           [896, 320],
                           [960, 320],
                           [1024, 320],
                           [64, 384],
                           [128, 384],
                           [192, 384],
                           [256, 384],
                           [320, 384],
                           [384, 384],
                           [448, 384],
                           [576, 384],
                           [704, 384],
                           [768, 384],
                           [1024, 384],
                           [1088, 384],
                           [576, 448],
                           [768, 448],
                           [896, 448],
                           [960, 448],
                           [1024, 448],
                           [128, 512],
                           [256, 512],
                           [320, 512],
                           [384, 512],
                           [448, 512],
                           [576, 512],
                           [640, 512],
                           [768, 512],
                           [1024, 512],
                           [1152, 512],
                           [128, 576],
                           [640, 576],
                           [768, 576],
                           [832, 576],
                           [896, 576],
                           [1024, 576],
                           [128, 640],
                           [256, 640],
                           [384, 640],
                           [512, 640],
                           [1024, 640],
                           [1088, 640],
                           [128, 704],
                           [192, 704],
                           [256, 704],
                           [320, 704],
                           [384, 704],
                           [448, 704],
                           [512, 704],
                           [576, 704],
                           [640, 704],
                           [704, 704],
                           [832, 704],
                           [896, 704],
                           [1024, 768],
                           [1088, 768],
                           [1152, 768],
                           [64, 832],
                           [128, 832],
                           [192, 832],
                           [320, 832],
                           [384, 832],
                           [448, 832],
                           [576, 832],
                           [640, 832],
                           [704, 832],
                           [768, 832],
                           [832, 832],
                           [896, 832],
                           [960, 832],
                           [1024, 832],
                           [576, 896]
                           ]
        for coordinate in coordinate_list:
            box = arcade.Sprite(":resources:images/tiles/boxCrate.png", BOX_SPRITE_SCALING)
            box.center_x = coordinate[0]
            box.center_y = coordinate[1]
            self.wall_list.append(box)

        # Place blue gems at specific coordinates.
        coordinate_list = [[64, 64],
                           [128, 64],
                           [768, 64],
                           [832, 64],
                           [896, 64],
                           [1024, 64],
                           [1088, 64],
                           [1152, 64],
                           [896, 128],
                           [192, 192],
                           [320, 192],
                           [640, 192],
                           [896, 192],
                           [960, 192],
                           [192, 256],
                           [64, 320],
                           [192, 320],
                           [640, 320],
                           [1088, 320],
                           [1152, 320],
                           [832, 384],
                           [1152, 384],
                           [64, 448],
                           [192, 448],
                           [512, 448],
                           [1088, 448],
                           [1152, 448],
                           [192, 512],
                           [832, 512],
                           [896, 512],
                           [960, 512],
                           [192, 576],
                           [256, 576],
                           [320, 576],
                           [384, 576],
                           [448, 576],
                           [512, 576],
                           [960, 576],
                           [192, 640],
                           [448, 640],
                           [768, 640],
                           [960, 640],
                           [960, 704],
                           [1024, 704],
                           [512, 768],
                           [576, 768],
                           [640, 768],
                           [704, 768],
                           [768, 768],
                           [960, 768],
                           [128, 896],
                           [192, 896],
                           [256, 896],
                           [320, 896],
                           [384, 896],
                           [448, 896],
                           [512, 896]
                           ]
        for coordinate in coordinate_list:
            blue_gem = arcade.Sprite(":resources:images/items/gemBlue.png", GEM_SPRITE_SCALING)
            blue_gem.center_x = coordinate[0]
            blue_gem.center_y = coordinate[1]
            self.blue_gem_list.append(blue_gem)

        # Place green gems at specific coordinates.
        # There are 12 of these.  Don't collect any to get a secret!
        coordinate_list = [[960, 64],
                           [256, 192],
                           [640, 256],
                           [960, 256],
                           [128, 320],
                           [128, 448],
                           [832, 448],
                           [512, 512],
                           [320, 640],
                           [768, 704],
                           [512, 832],
                           [64, 896]
                           ]
        for coordinate in coordinate_list:
            green_gem = arcade.Sprite(":resources:images/items/gemGreen.png", GEM_SPRITE_SCALING)
            green_gem.center_x = coordinate[0]
            green_gem.center_y = coordinate[1]
            self.green_gem_list.append(green_gem)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """ Render the screen. """

        # This command has to happen before we start drawing
        self.clear()

        # Select the camera we'll use to draw all our sprites

        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.blue_gem_list.draw()
        self.green_gem_list.draw()

        # Draw the special note text.  Implement this better!
        if len(self.green_gem_list) < 12:
            output = "Don't collect green gems next time."
            arcade.draw_text(output, 640, 896, arcade.color.BLACK, 20)
        elif len(self.green_gem_list) == 12 and len(self.blue_gem_list) == 0:
            output = "Congrats!  A secret should be here someday!"
            arcade.draw_text(output, 640, 896, arcade.color.BLACK, 20)
        elif len(self.green_gem_list) == 12:
            output = "Blue gems remaining: "
            arcade.draw_text(output + str(len(self.blue_gem_list)), 640, 896, arcade.color.BLACK, 20)

        # Select the (un-scrolled) camera for our GUI

        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        # text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
        #        f"{self.camera_sprites.position[1]:5.1f})"
        # arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)
        output = "Gems collected: " + str(self.score)
        arcade.draw_text(output, 10, 10, arcade.color.BLACK, 20)

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

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Find out which gems have collided with the player.
        blue_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.blue_gem_list)
        green_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.green_gem_list)
        # Loop through those lists and remove/update sprites that have been collected.
        for gem in blue_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)
        for gem in green_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

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

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):

        """
        Scroll the window to the player.
        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = Vec2(self.player_sprite.center_x - self.width / 2,

                        self.player_sprite.center_y - self.height / 2)

        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):

        """
        Resize window
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
