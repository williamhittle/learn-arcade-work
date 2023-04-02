""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None

        self.physics_engine = None

        # Cameras
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)



    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        # Set up the lists for player and sprites
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set score
        self.score = 0

        # Add player sprite to the player list
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # Add some boxes with various methods to the box list
        # manually create box 1
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        # manually create box 2
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)

        # place with a loop
        # You can open an image in chrome and the tab heading shows the pixel size.
        for x in range(173, 650, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        # place with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # create physics engine and reference the player, and what you can't run into
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


    def on_draw(self):
        arcade.start_render()

        # Now, with several cameras, choose which camera gets which things drawn in it
        self.camera_for_sprites.use()
        # Draw sprites
        self.wall_list.draw()
        self.player_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)
    def update(self, delta_time):

        # Update sprites with physics engine
        self.physics_engine.update()


        # camera doesn't seem to work on this one for some reason, so this is busted!

        # Update screen, scrolling it to player
        # self.scroll_to_player()
        # CAMERA_SPEED = 1
        # lower_left_corner = (self.player_sprite.center_x - self.width / 2,
        #                      self.player_sprite.center_y - self.height / 2)
        # self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)
        # camera_speed of 1 instantly moves

        # see https://api.arcade.academy/en/latest/examples/sprite_move_scrolling_box.html

    # keyboard function


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0





def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()