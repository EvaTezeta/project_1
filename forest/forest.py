import time

# Sets two timers
short_timer = 3
long_timer = 6

# Import side quests from other files
from forest.sword.sword import sword
from forest.parchment.parchment import parchment


# Define desert level
def forest(name):  # (name) imports input from user_name from main menu
    print(
        "As you step through the green portal you find yourself standing at " 
        "the edge of a lush green forest and you hear the chirping of birds."
    )
    time.sleep(long_timer)
    print()
    print(
        "You see a fairy flying around the edge of the forest. The fairy flies"
        " towards you and begins speaking."
    )
    time.sleep(long_timer)
    print()
    print(
        f'"Welcome {name}, to the magical forest that I call home. I am Eryn' 
        'and I will help you on your way."'
    )
    time.sleep(long_timer)
    print()
    print(
        'Eryn continues speaking: "To get back to the portal room, you have to'
        " enter this forest. You will come across a clearing where you must"
        " choose an item. Then you will use that item to get across the river"
        " to get to the portal that takes you to the main menu. "
        f'Good luck {name}!"'
    )
    time.sleep(long_timer)
    print()
    print("You say your goodbyes to Eryn and make your way into the forest.")
    time.sleep(long_timer)
    print()
    print(
        "After walking for quite some time you come across the clearing. You"
        " see a big tree in the centre of it and through the branches, across"
        " the clearing you can spot the deep blue water of the river."
    )
    time.sleep(long_timer)
    print()
    print(
        "You approach the tree and see the items that Eryn told you about. A"
        " piece of parchment and a sword. \nYou hear Eryn's voice in the back"
        f' of your head. "You have to choose an item {name}! Which one will it'
        ' be?"'
    )
    time.sleep(long_timer)
    print()

    # Define that chosen item can be either 1 or 2
    chosen_item = [1, 2]

    # Loop that let's player choose 1 or 2 for the quests
    while True:
        item = input("Choose 1 for the sword and 2 for the parchment. ")
        print()

        if item.isdigit():
            item = int(item)  # Makes sure that the input is integer

        if item not in chosen_item:  # If item is not 1 or 2
            print(
                "You have entered an invalid value. Please choose from"
                f" {chosen_item}."
            )
        elif item == 1:
            print("You have picked up the sword.")
            sword()  # Takes player to file sword.py to continue
            break  # Stops loop after chosing 1
        elif item == 2:
            print("You have picked up the parchment paper.")
            parchment()  # Takes player to file parchment.py to continue
            break  # Stops loop after chosing 2

    print()
    input(
        "You see the end portal and walk to it. Press any key to open the"
        " portal and to go back to the portal room. "
    )  # End of world 1
