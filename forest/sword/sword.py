import time

from forest.sword.fight.fight import fight
from forest.sword.flee.flee import flee

short_timer = 0
long_timer = 0


def sword():
    print()
    print("As you pick up the sword, something snaps and you hear a noise.")
    time.sleep(short_timer)
    print()
    print(
        "At the edge of the clearing a huge spider appears! It was triggered "
        "by the sound that was made when you picked up the sword."
    )
    print()
    time.sleep(short_timer)
    print("The spider starts running towards you, what do you do?")
    print()

    fight_flee = [1, 2]

    while True:
        spider = input("Choose 1 to fight and 2 to flee from the spider. ")
        print()
        if spider.isdigit():
            spider = int(spider)

        if spider not in fight_flee:
            print(
                "You have entered an invalid value. Please choose from"
                f" {fight_flee}."
            )
        elif spider == 1:
            print("You have chosen to fight the spider.")
            fight()
            break
        elif spider == 2:
            print("You have chosen to flee from the spider.")
            flee()
            break
