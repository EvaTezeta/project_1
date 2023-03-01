# Import module time for the time.sleep to create pauses between prints
import time
from forest.forest import forest
from desert.desert import desert
from mountain.mountain import mountain
from cave.cave import cave

# Sets two timers
short_timer = 3
long_timer = 6

# Welcome player
print("Welcome adventurer, to this fantasy text adventure game!")
time.sleep(short_timer)  # Inserts short timer to create pause between lines

# Ask the player for name and greet him/her
print("What is your name? ")
user_name = input("Name: ")

print(f"Nice to meet you {user_name}! Please continue to the portal room.")
time.sleep(short_timer)
print()  # Prints empty line for readability

# Enter portal room
print(
    "You find yourself in a mystical room filled with four portals. It seems"
    " like each portal leads to a different world. You see a sign that reads,"
    f' \n "Choose your portal wisely, {user_name}."'
)
time.sleep(long_timer)  # Inserts long timer to create pause between lines
print()

# Describe the different portals
print(
    "The first (1) portal emits a green light, the second (2) emits a yellow"
    " light, the third (3) a blue light, and the final fourth (4) portal a red"
    " light."
)
time.sleep(long_timer)
print()

# Choose portal
print(
    "Please choose a portal with a number. You can choose out of 1, 2, 3"
    " and 4. "
)

# Defines the levels that have yet to be completed
unfinished_levels = [1, 2, 3, 4]
print()

# While loop to finish all levels until finished
while True:
    if unfinished_levels == []:
        break  # If unfinished_levels is empty, it breaks the loop
        # and prints the farewell.

    # Ensures that input is digital
    # Otherwise it will print the else statement
    chosen = input("Portal: ")
    if chosen.isdigit():
        chosen = int(chosen)  # Defines the input of chosen as integer

    # If input is one of 4 levels but not in unfinished_levels
    # It will print that you have already finished it
    # and should choose another
    if chosen in [1, 2, 3, 4] and chosen not in unfinished_levels:
        print(
            "You have already finished this level. Please choose from"
            f" {unfinished_levels}."
        )
    elif chosen == 1:
        print("You have chosen the green portal and you enter a forest.")
        forest(name=user_name)  # Transfers input user name to forest level
        unfinished_levels.remove(1)  # If world 1 done,
        # it removes 1 from unfinished levels
        print()
        print(
            "You have finished the forest level. Please choose one of"
            f" {unfinished_levels}"
        )  # After removing 1,
        # the unfinished_levels displays the remaining levels
    elif chosen == 2:
        print()
        print("You have chosen the yellow portal and you enter a desert.")
        desert()
        unfinished_levels.remove(2)
    elif chosen == 3:
        print()
        print("You have chosen the blue portal and you enter mountains.")
        mountain()
        unfinished_levels.remove(3)
    elif chosen == 4:
        print()
        print("You have chosen the red portal and you enter a cave.")
        cave()
        unfinished_levels.remove(4)
    else:
        print(
            "You entered an invalid value, please enter an integer number"
            " between 1 and 4."
        )


# End of game
print()
print(f"Farewell {user_name}! Thanks for playing!")
