"""
Let's try importing arcade

"""

# gotta import a library
import arcade


# trying to open a window
# arcade.open_window(window width, window height, "text on title bar")
arcade.open_window(600, 600, "Drawing Example")
# the API (Application Program Interface) should tell me about the functions.

# this should set the background color
arcade.set_background_color(arcade.csscolor.ALICE_BLUE)

# tell the arcade library I'm about to draw:
arcade.start_render()

# here I will draw
arcade.draw_lrtb_rectangle_filled(0, 600, 300, 0, arcade.csscolor.GREEN)
# another arcade function for a rectangle is arcade.draw_rectangle_filled(); see api for optional parameters
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
# now draw a circle
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
# now draw a 'tree' with an oval top
arcade.draw_rectangle_filled(200, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)
# note that you can try different colors with code like this:
# arcade.draw_ellipse_filled(300, 370, 60, 80, (164, 198, 57))
# look up those RGB values from the API list, or the color picker thing

# let's draw a filled arc, like half an ellipse:
arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# let's draw a pointy triangle tree!
arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# but no!  I can't stop!  make a tree with a polygon shape!
arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)

# more code for a sun!
# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
# Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)

# now add some text!
arcade.draw_text("This is a thing of beauty.",
                 150, 230,
                 arcade.color.BLACK, 24)
arcade.draw_text("Truly a masterpiece.", 160, 180, arcade.color.BLACK, 24)
# note that I didn't have to put things on a new line, but it can be handy to separate stuff like that.

# also note that just throwing numbers into the argument of the function may be poor for reading.
# Taking some time to code "center_x=300" instead of just "300" when drawing can make it much easier
# to come back later and change things.

# finish drawing
arcade.finish_render()

# This keeps the window open until I manually close it.
arcade.run()
