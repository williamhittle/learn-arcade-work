"""
Text Adventure time!

"""
class Room:
    """
    This is a class defining a room.
    """
    def __init__(self, description, north, east, south, west):
        """ This is a method to set up the variables for the object. """
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
def main():
    """ Here is the main program function. """

    room_list = []

    # This is room 0, the West Wing.  N -> Kitchen.  E -> Great Hall.
    room = Room("This room is the West Wing.", 5, 1, None, None)
    room_list.append(room)

    # This is room 1, the Great Hall.  W -> West Wing.  E -> East Study.
    room = Room("This room is the Great Hall.", None, 2, None, 0)
    room_list.append(room)

    # This is room 2, the East Study.  W -> Great Hall.  N -> Stairwell.
    room = Room("This room is the East Study.", 3, None, None, 1)
    room_list.append(room)

    # This is room 3, the Stariwell.  N -> Dining Room.  S -> East Study.
    room = Room("This room is the stairwell.", 4, None, 2, None)
    room_list.append(room)

    # This is room 4, the Dining Room.  W -> Kitchen.  S -> Stairwell.
    room = Room("This room is the dining room.", None, None, 3, 5)
    room_list.append(room)

    # This is room 5, the Kitchen.  E -> Dining Room.  S -> West Wing.
    room = Room("This room is the kitchen.", None, 4, 0, None)
    room_list.append(room)

    current_room = room_list[1]
    print("You have entered a scary mansion.  You are standing in the Great Hall.")

    done = False
    while not done:
        print()
        print(current_room.description)
        user_choice = input("What would you like to do? ")

        if user_choice.upper() == "N":
            next_room = current_room.north
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
        elif user_choice.upper() == "W":
            next_room = current_room.west
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
        elif user_choice.upper() == "E":
            next_room = current_room.east
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
        elif user_choice.upper() == "S":
            next_room = current_room.south
            if next_room == None:
                print("You can't go that way.")
            else:
                current_room = room_list[next_room]
        elif user_choice.upper() == "Q":
            print("You have chosen to quit.")
            break
        else:
            print("I didn't understand what direction you wanted to go")
            print("Pick a direction: N, S, E, or W.  Type Q to quit.")


main()
