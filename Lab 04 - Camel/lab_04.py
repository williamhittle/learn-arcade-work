"""
Time to make a loopy game!
"""

# Import my libraries.

import random


# Define my functions.


def print_instructions():
    print("""
    Welcome to Camel!
    You have stolen a camel to make your way across the great Mobi desert.
    The natives want their camel back and are chasing you down!
    Survive your desert trek and out run the natives.

    If your thirst gets too high, your camel gets too tired, or the natives catch you, it's GAME OVER, MAN!

    Here are your options.  What will you do?
    """)


# Create the main function.


def main():
    # Define and initialize some variables for the game.

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance_traveled = -20
    max_canteen_swigs = 3
    canteen_swigs = 3

    print_instructions()
    done = False
    while not done:
        print("""
        A. Drink from your canteen.
        B. Ahead moderate speed.
        C. Ahead full speed.
        D. Stop for the night.
        E. Status check.
        Q. Quit.
        """)

        user_choice = input("What is your choice? ")

        # Option Q. Quit lets the player exit the loop without doing anything else. """
        if user_choice.upper() == "Q":
            print("You have chosen to quit the game.")
            break

        # Option E. Status check lets the player view their distance traveled,
        # how many drinks they have left in their canteen,
        # whether they're thirsty or the camel is tired,
        # and how close the natives are to them.
        elif user_choice.upper() == "E":
            print("You have traveled " + str(miles_traveled) + " miles.")
            if canteen_swigs > 1:
                print("You have " + str(canteen_swigs) + " drinks left in your canteen.")
            else:
                print("You have " + str(canteen_swigs) + " drink left in your canteen.")
            print("The natives are " + str(miles_traveled - native_distance_traveled) + " miles behind you.")

        # Option D. Stop for the night lets the player rest,
        # resetting the camel tiredness to 0,
        # but allowing the natives a chance to catch up.
        elif user_choice.upper() == "D":
            print("You are resting for the night.  The camel is happy.")
            camel_tiredness = 0
            native_distance_traveled += random.randint(7, 14)

        # Option C. Ahead full speed moves the player forward a large random amount of distance,
        # increases their thirst by 1,
        # increases their camel tiredness a random amount,
        # and moves the natives forward a random amount.
        # There is a chance to find an oasis when moving.
        elif user_choice.upper() == "C":
            miles_traveled += random.randint(10, 20)
            print("You have traveled " + str(miles_traveled) + " miles.")
            thirst += 1
            camel_tiredness += random.randint(1, 3)
            native_distance_traveled += random.randint(7, 14)
            oasis_roll = random.randint(1, 20)
            if oasis_roll == 1:
                print("You have found on oasis!  You refill your canteen while you and your camel rest.")
                canteen_swigs = max_canteen_swigs
                camel_tiredness = 0
                thirst = 0

        # Option B. Ahead moderate speed moves the player forward a small random amount of distance,
        # increases their thirst by 1,
        # increases their came tiredness by 1,
        # and moves the natives forward a random amount.
        # There is a chance to find an oasis when moving.
        elif user_choice.upper() == "B":
            miles_traveled += random.randint(5, 12)
            print("You have traveled " + str(miles_traveled) + " miles.")
            thirst += 1
            camel_tiredness += 1
            native_distance_traveled += random.randint(7, 14)
            oasis_roll = random.randint(1, 20)
            if oasis_roll == 1:
                print("You have found on oasis!  You refill your canteen while you and your camel rest.")
                canteen_swigs = max_canteen_swigs
                camel_tiredness = 0
                thirst = 0

        # Option A. Drink from your canteen resets the player's thirst to 0,
        # thereby using a swig from the canteen, if one is available.
        elif user_choice.upper() == "A":
            if canteen_swigs > 0:
                canteen_swigs -= 1
                thirst = 0
                print("You take a refreshing drink from your canteen.  Ahh!")
            else:
                print("Your canteen must be refilled, first!")

        # Now run some other checks.
        # Check thirst and print the appropriate text.
        if not done and thirst > 6:
            print("You died of thirst!")
            done = True
        elif not done and thirst > 4:
            print("You are thirsty.")

        # Check tiredness and print the appropriate text.
        if not done and camel_tiredness > 8:
            print("Your camel is dead.  The game is over.")
            done = True
        elif not done and camel_tiredness > 5:
            print("Your camel is getting tired.")

        # Check if the natives have caught up and end the game (if they have).
        # Also check if they're close.
        if not done and miles_traveled - native_distance_traveled <= 0:
            print("The natives have caught you!  The game is over.")
            done = True
        elif not done and miles_traveled - native_distance_traveled < 15:
            print("The natives are getting close!")

        # Check if the user has traveled 200 miles across the desert and reached safety (and won).
        if not done and miles_traveled >= 200:
            print("You have crossed the entire desert without getting caught!  You won!")
            done = True


# Call the main function.
main()