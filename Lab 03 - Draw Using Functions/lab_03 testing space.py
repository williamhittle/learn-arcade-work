"""
I'm going to draw my game image from lab 2, and hopefully make it better now that I can draw with functions.

"""

# Import the library.
import arcade

# Set up my screen size variables so that I can call them later.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
CHARACTER_1_COLOR = arcade.csscolor.CRIMSON
CHARACTER_2_COLOR = arcade.csscolor.SEA_GREEN

# All my actions are going to be defined here, and then called by my 'main' program.


def draw_ground():
    """ This will draw the ground.  It will be a rectangle across the whole screen, 100 pixels high.
    Remember that my 'block size' is 50 by 50. """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 100, 0, arcade.csscolor.DARK_RED)
    for i in range(5):
        arcade.draw_line(0, 100-20*i, SCREEN_WIDTH, 100-20*i, arcade.csscolor.BLACK, 2)


def draw_brick(x, y):
    """ This function will draw a single brick with the bottom left corner at a given x,y location. """
    arcade.draw_lrtb_rectangle_filled(x, x+50, y+50, y, arcade.csscolor.DARK_RED)
    arcade.draw_lrtb_rectangle_outline(x, x+50, y+50, y, arcade.csscolor.BLACK, 2)


def draw_brick_stairs():
    """ This function will draw the brick stairs that go before a flagpole on any stage.
    This is a still image, so I'm entering fixed numbers.
    It uses the draw_brick function I just made.
    This way, my main drawing function calls this one time, and if I want to change the stair design,
    I can do it here instead of in the final drawing.
    I can probably do this with a couple nested for loops, but I can't figure that out, yet. """
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
    """ This will draw a question mark block, with the bottom left corner at a given x,y location. """
    arcade.draw_lrtb_rectangle_filled(x, x+50, y+50, y, arcade.csscolor.GOLD)
    arcade.draw_lrtb_rectangle_outline(x, x+50, y+50, y, arcade.csscolor.BLACK, 3)
    arcade.draw_text("?", x+13, y+11, arcade.color.WHITE, 30)


def draw_flagpole(x, y):
    """ This will draw the flagpole, with the given x,y being the bottom left corner of the base block.
    I think I'd like the flag to be able to move, so it will be a separate draw function. """
    arcade.draw_lrtb_rectangle_filled(x+20, x+30, y+300, y+50, arcade.csscolor.SILVER)
    arcade.draw_lrtb_rectangle_outline(x+20, x+30, y+300, y+50, arcade.csscolor.BLACK)
    arcade.draw_lrtb_rectangle_filled(x, x+50, y+50, y, arcade.csscolor.FIREBRICK)
    arcade.draw_lrtb_rectangle_outline(x, x+50, y+50, y, arcade.csscolor.BLACK, 2)


def draw_flag(x, y):
    """ This will draw the flag, with the bottom pointy bit being the given x,y location. """
    arcade.draw_triangle_filled(x, y, x-50, y+25, x, y+50, arcade.csscolor.WHITE)
    arcade.draw_triangle_outline(x, y, x-50, y+25, x, y+50, arcade.csscolor.BLACK)


def draw_big_cloud(x, y):
    """ This will draw the same long cloud I made in lab 2, with the center at a given x,y location. """
    arcade.draw_ellipse_filled(x, y, 200, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-50, y, 20, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-25, y, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x, y, 20, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+25, y, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+50, y, 20, arcade.csscolor.WHITE)


def draw_small_cloud(x, y):
    """ This will draw a smaller version of the cloud, centered at the given x,y location. """
    arcade.draw_ellipse_filled(x, y, 100, 25, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x-25, y, 15, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x, y, 20, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(x+25, y, 15, arcade.csscolor.WHITE)


def draw_character_standing(x, y, z):
    """ This will draw a player with its bottom left 'shoe pixel' at the given x,y location,
    and a color given by z, which defines player 1 or 2. """
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


""" 
Define other drawing functions here.

Do I want a character 2, who may slide down the flagpole?
Anything else?
"""


def on_draw(delta_time):
    """ This draws everything. """
    arcade.start_render()

    # Insert all draw functions here, using x,y coordinates.
    draw_ground()
    draw_brick_stairs()
    draw_question_block(500, 250)
    draw_flagpole(850, 100)
    draw_flag(870, 350)
    draw_big_cloud(300, 500)
    draw_big_cloud(650, 475)
    draw_small_cloud(500, 450)
    draw_small_cloud(900, 550)
    draw_character_standing(500, 100, CHARACTER_1_COLOR)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Jumpy Spot Bros V2.0")
    arcade.set_background_color(arcade.csscolor.DODGER_BLUE)

    # Call the on_draw function every fraction of a second.  The book used 1/60th.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Now I call the main function and have it run all the building blocks I've made.
main()
