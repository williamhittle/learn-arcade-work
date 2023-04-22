# This is level 0 for my final project
# First comes the chunk of code that I need to make any instance of my Level class:

import arcade

PLAYER_SPRITE_SCALING = 0.45
BORDER_SPRITE_SCALING = 0.5
BOX_SPRITE_SCALING = 0.5
GEM_SPRITE_SCALING = 0.5
GEAR_SPRITE_SCALING = 0.5
ENEMY_SPRITE_SCALING_1 = 0.5
ENEMY_SPRITE_SCALING_2 = 1.0
PORTAL_SPRITE_SCALING = 0.5

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

# Now here is level_0:

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
    coordinate_list = [[1, 7],
                       [1, 8],
                       [1, 9],
                       [1, 10],
                       [5, 6],
                       [5, 7],
                       [6, 6],
                       [6, 7],
                       [14, 10],
                       [14, 11],
                       [15, 10],
                       [15, 11]]
    for coordinate in coordinate_list:
        blue_gem = arcade.Sprite(":resources:images/items/gemBlue.png", GEM_SPRITE_SCALING)
        blue_gem.center_x = coordinate[0]*64
        blue_gem.center_y = coordinate[1]*64
        level.blue_gem_list.append(blue_gem)

    # Put out some green gems.
    coordinate_list = [[8, 12],
                       [9, 12],
                       [10, 12],
                       [11, 12],
                       [11, 2],
                       [11, 3],
                       [12, 2],
                       [12, 3]]
    for coordinate in coordinate_list:
        green_gem = arcade.Sprite(":resources:images/items/gemGreen.png", GEM_SPRITE_SCALING)
        green_gem.center_x = coordinate[0]*64
        green_gem.center_y = coordinate[1]*64
        level.green_gem_list.append(green_gem)

    # Put out the gears.
    coordinate_list = [[1, 4],
                       [7, 3],
                       [16,14]]
    for coordinate in coordinate_list:
        gear = arcade.Sprite(":resources:images/enemies/saw.png", GEAR_SPRITE_SCALING)
        gear.center_x = coordinate[0]*64
        gear.center_y = coordinate[1]*64
        level.gear_list.append(gear)

    # Set out some boxes.
    coordinate_list = [[2, 13],
                       [3, 13],
                       [4, 13],
                       [5, 13],
                       [6, 13],
                       [7, 13],
                       [8, 13],
                       [9, 13],
                       [10, 13],
                       [11, 13],
                       [12, 13],
                       [13, 13],
                       [14, 13],
                       [15, 13],
                       [16, 13],
                       [17, 13],
                       [12, 12],
                       [1, 11],
                       [2, 11],
                       [3, 11],
                       [4, 11],
                       [5, 11],
                       [6, 11],
                       [7, 11],
                       [8, 11],
                       [9, 11],
                       [10, 11],
                       [12, 11],
                       [10, 10],
                       [12, 10],
                       [2, 9],
                       [3, 9],
                       [4, 9],
                       [5, 9],
                       [6, 9],
                       [7, 9],
                       [8, 9],
                       [10, 9],
                       [12, 9],
                       [2, 8],
                       [8, 8],
                       [10, 8],
                       [12, 8],
                       [2, 7],
                       [8, 7],
                       [10, 7],
                       [12, 7],
                       [14, 7],
                       [15, 7],
                       [16, 7],
                       [17, 7],
                       [2, 6],
                       [2, 5],
                       [2, 4],
                       [6, 4],
                       [7, 4],
                       [8, 4],
                       [9, 4],
                       [1, 3],
                       [2, 3],
                       [3, 3],
                       [6, 3],
                       [3, 2],
                       [6, 2]]
    for coordinate in coordinate_list:
        box = arcade.Sprite(":resources:images/tiles/boxCrate.png", BOX_SPRITE_SCALING)
        box.center_x = coordinate[0]*64
        box.center_y = coordinate[1]*64
        level.wall_list.append(box)

    # Put out some robots for the default level enemies.
    coordinate_list = [[4, 2],
                       [7, 8],
                       [10, 6],
                       [15, 8]]
    for coordinate in coordinate_list:
        robo = arcade.Sprite(":resources:images/animated_characters/robot/robot_idle.png", ENEMY_SPRITE_SCALING_1)
        robo.center_x = coordinate[0]*64
        robo.center_y = coordinate[1]*64
        level.enemy_list.append(robo)

    # Place the portal to the next level.
    # This requires a certain number of gears to activate.
    portal = arcade.Sprite(":resources:images/tiles/lockRed.png", PORTAL_SPRITE_SCALING)
    portal.center_x = 18*64
    portal.center_y = 14*64
    level.portal_list.append(portal)


    return level