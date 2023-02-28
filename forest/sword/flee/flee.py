import time
from forest.sword.flee.pole.pole import pole
from forest.sword.flee.swim.swim import swim

short_timer = 0
long_timer = 0


def flee():
    print()
    print("You run out of the clearing and towards the glittering river.")
    time.sleep(short_timer)
    print()
    print(
        "You have quite a headstart on the spider, "
        "but you have to quickly choose how to get across the clearing."
    )
    print()
    print(
        "Do you jump in and swim across the river? "
        "Or do you cut of a branch with the sword and make a pole to jump?"
    )
    print()

    swim_pole = [1, 2]

    while True:
        river = input(
            "Choose 1 to swim across the river "
            "and 2 to a pole to polevault across the river. "
        )
        print()
        if river.isdigit():
            river = int(river)

        if river not in swim_pole:
            print(
                "You have entered an invalid value. Please choose from"
                f" {swim_pole}."
            )
        elif river == 1:
            print(
                "You have chosen to swim across the river to flee from the"
                " spider."
            )
            swim()
            break
        elif river == 2:
            print(
                "You have chosen to make a pole to polevault across the river."
            )
            pole()
            break
