import time
import random

short_timer = 0
long_timer = 0


def parchment():
    print()
    print(
        "As you pick up the piece of parchment paper, you see that it has a"
        " magic spell written on it that will make you fly over the river."
    )
    time.sleep(short_timer)
    print()

    for i in range(3):
        input("Press any key to try and cast the spell. ")
        num = random.randint(0, 2)
        if num == 1:
            break
        else:
            print("You failed to cast the spell correctly, try again.")
    print()
    print("You cast the spell correctly and fly over the river!")
