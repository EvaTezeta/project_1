import time
import random

short_timer = 0
long_timer = 0


def fight():
    print()
    print(
        "The spider advances quickly and attacks! "
        "You fight back with the sword and try and kill it."
    )
    time.sleep(short_timer)
    print()

    for i in range(3):
        input("Press any key to try and kill the spider. ")
        num = random.randint(0, 2)
        if num == 1:
            break
        else:
            print("You failed to kill the spider, try again.")

    print()
    print("You killed the spider!")
    time.sleep(short_timer)
    print()
    print("After killing the spider, you walk towards the river.")
    print()
    time.sleep(long_timer)
    print(
        "You see something glimmering in the corner of your eye. \n"
        "It's the spider's nest and it's full of strong spider silk."
    )
    time.sleep(long_timer)
    print()
    print(
        "You collect all the spider silk and braid it into a rope."
        "Then you attach the rope unto a strong looking tree "
        "and swing across the river."
    )
    time.sleep(short_timer)
    print()
    print("You safely make it to the other side of the river!")
