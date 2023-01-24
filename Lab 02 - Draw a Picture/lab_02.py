"""
I'm going to try and depict a video game image.

"""

# Import the arcade library.
import arcade

# Open a window for drawing.
arcade.open_window(1000, 600, "Jumpy Spot Bros.")

# Set the background color of the window.
arcade.set_background_color(arcade.csscolor.DODGER_BLUE)

# Tell the arcade library that I'm about to draw:
arcade.start_render()

# Begin the drawing!

# Try to draw the ground with a polygon shape.
arcade.draw_polygon_filled(((0, 0),
                            (0, 100),
                            (50, 100),
                            (50, 150),
                            (100, 150),
                            (100, 200),
                            (150, 200),
                            (150, 250),
                            (200, 250),
                            (200, 300),
                            (250, 300),
                            (250, 350),
                            (300, 350),
                            (300, 400),
                            (350, 400),
                            (350, 100),
                            (1000, 100),
                            (1000, 0),
                            ),
                           arcade.csscolor.DARK_RED)
# Try to make it look like bricks by adding outlines of squares.
arcade.draw_rectangle_outline(75, 125, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(125, 125, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(175, 125, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(225, 125, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(275, 125, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(325, 125, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(125, 175, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(175, 175, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(225, 175, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(275, 175, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(325, 175, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(175, 225, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(225, 225, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(275, 225, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(325, 225, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(225, 275, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(275, 275, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(325, 275, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(275, 325, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(325, 325, 50, 50, arcade.csscolor.BLACK, 2)
arcade.draw_rectangle_outline(325, 375, 50, 50, arcade.csscolor.BLACK, 2)
# Add some lines to the ground to make it different from bricks.
arcade.draw_line(0, 100, 1000, 100, arcade.csscolor.BLACK, 2)
arcade.draw_line(0, 75, 1000, 75, arcade.csscolor.BLACK, 2)
arcade.draw_line(0, 50, 1000, 50, arcade.csscolor.BLACK, 2)
arcade.draw_line(0, 25, 1000, 25, arcade.csscolor.BLACK, 2)

# Try to draw player 1.  Remember that a "sprite" will be 50 x 50 pixels.
# Start with his feet.
# Draw left foot.
arcade.draw_triangle_filled(300, 400, 320, 400, 320, 410, arcade.csscolor.WHITE)
# Draw right foot.
arcade.draw_triangle_filled(330, 400, 350, 400, 330, 410, arcade.csscolor.WHITE)
# Draw left leg.
arcade.draw_polygon_filled(((310, 405),
                            (320, 410),
                            (325, 430),
                            (315, 430)
                            ),
                           arcade.csscolor.CRIMSON)
# Draw right leg.
arcade.draw_polygon_filled(((340, 405),
                            (330, 410),
                            (325, 430),
                            (335, 430)
                            ),
                           arcade.csscolor.CRIMSON)
# Draw the circle body.
arcade.draw_circle_filled(325, 435, 15, arcade.color.YELLOW)
arcade.draw_circle_outline(325, 435, 15, arcade.color.BLACK, 1)
# Draw the eyes.
arcade.draw_circle_filled(320, 440, 5, arcade.color.DIM_GRAY)
arcade.draw_circle_filled(330, 440, 5, arcade.color.DIM_GRAY)
arcade.draw_circle_filled(320, 440, 2, arcade.color.HONEYDEW)
arcade.draw_circle_filled(330, 440, 2, arcade.color.HONEYDEW)
# Draw a smile.
arcade.draw_arc_filled(325, 430, 15, 10, (0,0,0), 170, 370)

# Try to draw player 2.  Remember that a "sprite" will be 50 x 50 pixels.  This one faces right.
# Start with his feet.
arcade.draw_triangle_filled(600, 100, 620, 100, 600, 110, arcade.csscolor.WHITE)
arcade.draw_triangle_filled(610, 100, 630, 100, 610, 110, arcade.csscolor.WHITE)
# his legs
arcade.draw_polygon_filled(((600, 110),
                            (610, 105),
                            (610, 130),
                            (600, 130)
                            ),
                           arcade.csscolor.SEA_GREEN)
arcade.draw_polygon_filled(((610, 110),
                            (620, 105),
                            (620, 130),
                            (610, 130)
                            ),
                           arcade.csscolor.SEA_GREEN)
# Draw the circle body.
arcade.draw_circle_filled(610, 135, 15, arcade.color.YELLOW)
arcade.draw_circle_outline(610, 135, 15, arcade.color.BLACK, 1)
# Draw the eyes.
arcade.draw_circle_filled(615, 140, 5, arcade.color.DIM_GRAY)
arcade.draw_circle_filled(620, 140, 5, arcade.color.DIM_GRAY)
arcade.draw_circle_filled(623, 140, 2, arcade.color.HONEYDEW)
arcade.draw_circle_filled(618, 140, 2, arcade.color.HONEYDEW)
# Draw a smile.
arcade.draw_arc_filled(615, 130, 15, 10, (0,0,0), 170, 370)

# Draw a couple blocks on the stage.
arcade.draw_rectangle_filled(500, 250, 50, 50, arcade.csscolor.GOLD)
arcade.draw_rectangle_outline(500, 250, 50, 50, arcade.csscolor.BLACK, 3)
arcade.draw_rectangle_filled(650, 250, 50, 50, arcade.csscolor.GOLD)
arcade.draw_rectangle_outline(650, 250, 50, 50, arcade.csscolor.BLACK, 3)
arcade.draw_text("?", 488, 235, arcade.color.WHITE, 30)
arcade.draw_text("?", 638, 235, arcade.color.WHITE, 30)

# Draw the flag-finish-marker.
# Here's the base:
arcade.draw_rectangle_filled(850, 125, 50, 50, arcade.csscolor.FIREBRICK)
arcade.draw_rectangle_outline(850, 125, 50, 50, arcade.csscolor.BLACK, 2)
# Here's the pole:
arcade.draw_rectangle_filled(850, 300, 10, 300, arcade.csscolor.SILVER)
# Here's the flag:
arcade.draw_triangle_filled(845, 400, 800, 420, 845, 440, arcade.csscolor.WHITE)

# Add some clouds in the sky.
# Cloud 1:
arcade.draw_ellipse_filled(150, 500, 200, 25, (255,255,255))
arcade.draw_circle_filled(100, 500, 20, (255,255,255))
arcade.draw_circle_filled(125, 500, 25, (255,255,255))
arcade.draw_circle_filled(150, 500, 20, (255,255,255))
arcade.draw_circle_filled(175, 500, 25, (255,255,255))
arcade.draw_circle_filled(200, 500, 20, (255,255,255))
# Cloud 2:
arcade.draw_ellipse_filled(450, 530, 200, 25, (255,255,255))
arcade.draw_circle_filled(400, 530, 20, (255,255,255))
arcade.draw_circle_filled(425, 530, 25, (255,255,255))
arcade.draw_circle_filled(450, 530, 20, (255,255,255))
arcade.draw_circle_filled(475, 530, 25, (255,255,255))
arcade.draw_circle_filled(500, 530, 20, (255,255,255))
# Cloud 3:
arcade.draw_ellipse_filled(850, 520, 200, 25, (255,255,255))
arcade.draw_circle_filled(800, 520, 20, (255,255,255))
arcade.draw_circle_filled(825, 520, 25, (255,255,255))
arcade.draw_circle_filled(850, 520, 20, (255,255,255))
arcade.draw_circle_filled(875, 520, 25, (255,255,255))
arcade.draw_circle_filled(900, 520, 20, (255,255,255))

# Finish drawing!
arcade.finish_render()

# Put this in so the window stays open until manually closed.
arcade.run()