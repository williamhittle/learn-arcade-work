""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


# import my background drawing functions here (without the extra comments about what they do):
def draw_ground():
    """ This will draw instructions for this program, in addition to the ground that I had before. """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 100, 0, arcade.csscolor.DARK_RED)
    for i in range(5):
        arcade.draw_line(0, 100-20*i, SCREEN_WIDTH, 100-20*i, arcade.csscolor.BLACK, 2)
        arcade.draw_text("Use WASD to move the green bro.", 5, 5, arcade.color.WHITE, 10)
        arcade.draw_text("Use the arrow keys to move the red bro.", 5, 25, arcade.color.WHITE, 10)
        arcade.draw_text("Use the mouse to move the angry sun.", 5, 45, arcade.color.WHITE, 10)


def draw_brick(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x+50, y+50, y, arcade.csscolor.DARK_RED)
    arcade.draw_lrtb_rectangle_outline(x, x+50, y+50, y, arcade.csscolor.BLACK, 2)


def draw_brick_stairs():
    draw_brick(50, 100)
    draw_brick(100, 100)
    draw_brick(150, 100)
    draw_brick(200, 100)
    draw_brick(250, 100)
    draw_brick(100, 150)
    draw_brick(150, 150)
    draw_brick(200, 150)
    draw_brick(250, 150)
    draw_brick(150, 200)
    draw_brick(200, 200)
    draw_brick(250, 200)
    draw_brick(200, 250)
    draw_brick(250, 250)
    draw_brick(250, 300)


def draw_question_block(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x+50, y+50, y, arcade.csscolor.GOLD)
    arcade.draw_lrtb_rectangle_outline(x, x+50, y+50, y, arcade.csscolor.BLACK, 3)
    arcade.draw_text("?", x+13, y+11, arcade.color.WHITE, 30)


def draw_flagpole(x, y):
    arcade.draw_lrtb_rectangle_filled(x + 20, x + 30, y + 300, y + 50, arcade.csscolor.SILVER)
    arcade.draw_lrtb_rectangle_outline(x + 20, x + 30, y + 300, y + 50, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(x, x + 50, y + 50, y, arcade.csscolor.FIREBRICK)
    arcade.draw_lrtb_rectangle_outline(x, x + 50, y + 50, y, arcade.csscolor.BLACK, 2)


def draw_flag(x, y):
    arcade.draw_triangle_filled(x, y, x-50, y+25, x, y+50, arcade.csscolor.WHITE)
    arcade.draw_triangle_outline(x, y, x-50, y+25, x, y+50, arcade.csscolor.BLACK)

# I think I'd like these clouds to be a class, and then I'll create cloud objects
# But that'll be bonus content, if I get the sounds done first.
# For now, they're just chilling here, commented out.


# def draw_big_cloud(x, y):
#     """ This will draw the same long cloud I made in lab 2, with the center at a given x,y location. """
#     arcade.draw_ellipse_filled(x, y, 200, 25, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x-50, y, 20, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x-25, y, 25, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x, y, 20, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x+25, y, 25, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x+50, y, 20, arcade.csscolor.WHITE)
#
#
# def draw_small_cloud(x, y):
#     """ This will draw a smaller version of the cloud, centered at the given x,y location. """
#     arcade.draw_ellipse_filled(x, y, 100, 25, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x-25, y, 15, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x, y, 20, arcade.csscolor.WHITE)
#     arcade.draw_circle_filled(x+25, y, 15, arcade.csscolor.WHITE)


def draw_character_standing(x, y, z):
    arcade.draw_triangle_filled(x+10, y, x+30, y, x+10, y+10, arcade.csscolor.WHITE)
    arcade.draw_triangle_outline(x+10, y, x+30, y, x+10, y+10, arcade.csscolor.BLACK)
    arcade.draw_triangle_filled(x, y, x+20, y, x, y+10, arcade.csscolor.WHITE)
    arcade.draw_triangle_outline(x, y, x + 20, y, x, y + 10, arcade.csscolor.BLACK)
    arcade.draw_polygon_filled(((x+10, y+10),
                                (x+15, y+7),
                                (x+15, y+30),
                                (x+10, y+30)),
                               z)
    arcade.draw_polygon_outline(((x + 10, y + 10),
                                (x + 15, y + 7),
                                (x + 15, y + 30),
                                (x + 10, y + 30)),
                                arcade.csscolor.BLACK)
    arcade.draw_polygon_filled(((x, y+10),
                                (x+10, y+5),
                                (x+10, y+30),
                                (x, y+30)),
                               z)
    arcade.draw_polygon_outline(((x, y + 10),
                                (x + 10, y + 5),
                                (x + 10, y + 30),
                                (x, y + 30)),
                                arcade.csscolor.BLACK)
    arcade.draw_circle_filled(x+8, y+35, 15, arcade.color.YELLOW)
    arcade.draw_circle_outline(x+8, y+35, 15, arcade.color.BLACK)
    arcade.draw_circle_filled(x+13, y+40, 5, arcade.color.DIM_GRAY)
    arcade.draw_circle_filled(x+18, y+40, 5, arcade.color.DIM_GRAY)
    arcade.draw_circle_filled(x+21, y+40, 2, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(x+16, y+40, 2, arcade.color.HONEYDEW)
    arcade.draw_arc_filled(x+13, y+30, 15, 10, (0, 0, 0), 170, 370)

# Here's a new image created just for this lab!  An angry sun!
# I only need a position to be optional for this, and I'll hardcode its size, shape, and color


def draw_angry_sun(x, y):
    arcade.draw_circle_filled(x, y, 30, arcade.color.YELLOW)
    arcade.draw_circle_outline(x, y, 30, arcade.color.BLACK)
    arcade.draw_line(x-40, y, x-30, y, arcade.color.BLACK)
    arcade.draw_line(x+40, y, x+30, y, arcade.color.BLACK)
    arcade.draw_line(x, y+40, x, y+30, arcade.color.BLACK)
    arcade.draw_line(x, y-40, x, y-30, arcade.color.BLACK)
    arcade.draw_line(x-30, y-30, x-20, y-20, arcade.color.BLACK)
    arcade.draw_line(x-30, y+30, x-20, y+20, arcade.color.BLACK)
    arcade.draw_line(x+30, y-30, x+20, y-20, arcade.color.BLACK)
    arcade.draw_line(x+30, y+30, x+20, y+20, arcade.color.BLACK)
    arcade.draw_arc_filled(x-10, y+15, 10, 10, arcade.color.BLACK, 180, 360)
    arcade.draw_arc_filled(x+10, y+15, 10, 10, arcade.color.BLACK, 180, 360)
    arcade.draw_arc_outline(x, y-20, 30, 30, arcade.csscolor.BLACK, 0, 180)


# Make a class for drawing my 'player'
# I shall call it the 'Bro' class, and each instance will be a numbered bro.
class Bro:
    def __init__(self, position_x, position_y, change_x, change_y, color):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.color = color

        # Load up the sounds I want to trigger when bumping into the edge, and create a 'player' attribute.
        self.edge_sound = arcade.load_sound(":resources:sounds/rockHit2.ogg")
        self.edge_sound_player = None

    # I have to actually define what it means to draw my bro, utilizing the functions I've made previously.
    def draw(self):

        draw_character_standing(self.position_x,
                                self.position_y,
                                self.color)

    # I want the bro to move, based on some movement amount that I'll figure out later from inputs.
    def update(self):

        self.position_x += self.change_x
        self.position_y += self.change_y

        # Make sure the bro can't run off the screen, dude! Remember that its 'position' is the bottom left pixel of
        # my image's shoe. If the bro hits the edge of the screen, play a sound. Make sure to add some conditions so
        # that the sound doesn't keep playing over itself if the bro is smashed up against the edge by an unusually
        # rude human player.

        if self.position_x < 8:
            self.position_x = 8
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

        if self.position_y < 0:
            self.position_y = 0
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

        if self.position_x > SCREEN_WIDTH - 25:
            self.position_x = SCREEN_WIDTH - 25
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

        if self.position_y > SCREEN_HEIGHT - 50:
            self.position_y = SCREEN_HEIGHT - 50
            if not self.edge_sound_player or not self.edge_sound_player.playing:
                self.edge_sound_player = arcade.play_sound(self.edge_sound)
                arcade.play_sound(self.edge_sound)

# Make a class for the 'angry sun'


class Sun:
    def __init__(self, position_x, position_y, change_x, change_y):

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

        # Since the sun is moved with a mouse, add a sound for mouse clicking!
        self.click_sound = arcade.load_sound(":resources:sounds/fall3.wav")
        self.click_sound_player = None

    # Define the drawing of my sun.
    def draw(self):

        draw_angry_sun(self.position_x,
                       self.position_y)

    # Define the moving of my sun.
    def update(self):

        self.position_x += self.change_x
        self.position_y += self.change_y


# Here we go!  The actual creation of objects using the classes I made and the drawing thereof!
class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        # Set the background color
        arcade.set_background_color(arcade.csscolor.DODGER_BLUE)

        # Create my Bros with some attributes.
        self.bro1 = Bro(400, 100, 0, 0, arcade.csscolor.CRIMSON)
        self.bro2 = Bro(250, 350, 0, 0, arcade.csscolor.GREEN)

        # Create my angry sun with some attributes.
        self.sun1 = Sun(500, 500, 0, 0)

        # Make sure mouse disappears when it's on the window.
        self.set_mouse_visible(False)

        # Let's add some sounds for different clickings!
        self.click_sound1 = arcade.load_sound(":resources:sounds/fall3.wav")
        self.click_sound2 = arcade.load_sound(":resources:sounds/fall4.wav")

    def on_draw(self):
        arcade.start_render()

        # Start by drawing the static stuff.
        draw_ground()
        draw_brick_stairs()
        draw_question_block(450, 250)
        draw_question_block(650, 250)
        draw_flagpole(850, 100)
        draw_flag(870, 350)

        # Be sure to draw the objects that move by input.
        self.bro1.draw()
        self.sun1.draw()
        self.bro2.draw()

    # Now to make the bro move when I do stuff.  Start by making sure it updates.
    def update(self, delta_time):
        self.bro1.update()
        self.bro2.update()

    # Make the image move when you press a direction.
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bro1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.bro1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.bro1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.bro1.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.bro2.change_y = MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.bro2.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.bro2.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.bro2.change_x = MOVEMENT_SPEED

    # Make the image stop moving when you let go of the key.
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.bro1.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.bro1.change_y = 0
        if key == arcade.key.A or key == arcade.key.D:
            self.bro2.change_x = 0
        if key == arcade.key.W or key == arcade.key.S:
            self.bro2.change_y = 0

    # Now also make the sun move.  For this project, it will only be a simple 'move with mouse' thing.
    def on_mouse_motion(self, x, y, dx, dy):
        self.sun1.position_x = x
        self.sun1.position_y = y

    # Now to play the sound when the mouse is clicked.
    # I don't mind if the sound overlaps itself from a user's rapid clicking.  I think the lasers sound cool.
    # I know they're 'falling sounds', but I don't care.  I think they're lasers.
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.click_sound1)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.click_sound2)

# Release the Kraken!


def main():
    window = MyGame()
    arcade.run()


main()
