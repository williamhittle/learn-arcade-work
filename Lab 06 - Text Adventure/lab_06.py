"""
Text Adventure time!

"""


class Room:
    """
    This is a class defining a room.
    """
    def __init__(self, description, name, north, east, south, west):
        """ This is a method to set up the variables for the object. """
        self.description = description
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    """ Here is the main program function. """

    # Initialize the room list!
    room_list = []

    # This is room 0, the West Wing.  N -> Kitchen.  E -> Great Hall.
    room = Room("This room is the west wing.\nThere is a door to the north, and a door to the east.\nGloomy moonlight "
                "spills in from the western windows.", "west wing", 5, 1, None, None)
    room_list.append(room)

    # This is room 1, the Great Hall.  W -> West Wing.  E -> East Study.
    room = Room("This room is the central hall, where you first entered the mansion.\nThere is a door to the west, "
                "and a door to the east.\nTo the north is a ruined staircase.  You can't go that way.\nYou could exit "
                "to the south...", "central hall", None, 2, 6, 0)
    room_list.append(room)

    # This is room 2, the East Study.  W -> Great Hall.  N -> Stairwell.
    room = Room("This room is the east study.\nThere is a door to the north, and a door to the west.\nAncient "
                "leathery tomes line the walls from floor to ceiling.", "east study", 3, None, None, 1)
    room_list.append(room)

    # This is room 3, the Stairwell.  N -> Dining Room.  S -> East Study.
    room = Room("This room is the stairwell.\nThe stairs lead west back through the central hall, but they appear to "
                "be ruined.  You can't go that way.\nThere is a door to the north, and a door to the south.",
                "stairwell", 4, None, 2, None)
    room_list.append(room)

    # This is room 4, the Dining Room.  W -> Kitchen.  S -> Stairwell.
    room = Room("This room is the northeast dining room.\nA collapsed passage to the southwest appears to be the "
                "ruined stairs.\nA fancy table set with fine dinnerware is covered with thick dust.\nThere is a door "
                "to the west, and a door to the south.", "dining room", None, None, 3, 5)
    room_list.append(room)

    # This is room 5, the Kitchen.  E -> Dining Room.  S -> West Wing.
    room = Room("This room is the northwest kitchen.  There is a door to the east, and a door to the south.\nThe "
                "north exit to the back of the house appears to be blocked.\nThe massive stove is dark with soot and "
                "eerily silent.", "kitchen", None, 4, 0, None)
    room_list.append(room)

    # This is room 6, the front of the mansion, which is an alternative exit for the player.
    room = Room("This is the front yard of the mansion.\nYou have the chance to escape!\nOr you could head north back "
                "into the mansion...", "front yard", 1, None, 7, None)
    room_list.append(room)

    # This is room 7.  If a player "goes" here, they've escaped.
    room = Room("You have escaped!", "escape!", None, None, None, None)
    room_list.append(room)

    secret_count = 0
    current_room = room_list[1]
    print("You have entered a scary mansion.  You are standing in the great hall.")
    done = False
    while not done:

        """
        This still needs to be able to handle inputs other than the basic letters and words.
        It would be cool if some inputs allowed hidden options, like typing 'grab book' could trigger something.
        """

        # Every time we have start the loop, do some checks:
        # This first check will be for how many times the player has typed something other than the expected directions.
        # This will be a clue that maybe there are other things they could type that lead to new stuff...
        if secret_count > 3:
            print()
            print("There are some words and phrases that might work, but it's not that...")

        # This is the expected beginning of what the player sees with every iteration of the while loop.
        print()
        print(current_room.description)
        # Here is a check to see if the player is in a special place (the front yard) that might allow an escape.
        # Other checks could be put in for other special places.
        if current_room.name == "front yard":
            user_choice = input("Do you want to go north into the mansion, or run south and escape? ")
        # If they're not in a special place, they must be in a room and need to make a decision.
        # Right now, the only apparent decision to make is which way to go.
        # But typing other things could do new stuff, if I add that functionality.
        else:
            user_choice = input("What direction would you like to go?  You can type N, E, S, or W.  (Type Q to quit.) ")

        # This code will not trigger with the current game configuration,
        # because the only way to leave is walking south from the central hall,
        # but it's here for the future.
        if current_room.name == "escape!":
            print("You have escaped!  Flee!  Never return!")
            break

        # The player moves north.
        if user_choice.upper() == "N" or user_choice.upper() == "NORTH":
            next_room = current_room.north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
                print("You enter the " + current_room.name)
                secret_count = 0

        elif user_choice.upper() == "W" or user_choice.upper() == "WEST":
            next_room = current_room.west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
                print("You enter the " + current_room.name)
                secret_count = 0

        elif user_choice.upper() == "E" or user_choice.upper() == "EAST":
            next_room = current_room.east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
                print("You enter the " + current_room.name)
                secret_count = 0

        elif user_choice.upper() == "S" or user_choice.upper() == "SOUTH":
            next_room = current_room.south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
                # Heading south is the only way (currently) to exit, if the player is in the front yard,
                # so check to see if moving south has caused them to enter the "escape!" room.
                if current_room.name == "escape!":
                    print("You have escaped!")
                    break
                else:
                    print("You enter the " + current_room.name)
                    secret_count = 0

        elif user_choice.upper() == "Q" or user_choice.upper() == "QUIT":
            print("You have chosen to quit.")
            break

        else:
            print("I didn't understand what direction you wanted to go.\nLet's try this again, shall we?")
            secret_count += 1


main()
