unicorn_1 = True
import random

number = random.randint(1, 5)
number_guessed = False
sound_made = False
words = ["aah","AAHHH","boe","scream","leave","AHHH"]
import time #For time.sleep

right = True

#End of world 3
def end_key_found():
    # the end of the world. This will be put at every end, the mountain path
    # and the valley path have both different ending places, so with the
    # function you can put the same end at different places.
    time.sleep(4)
    print(
        "Now that you've found the key. You take a good look at it. You"
        " start wondering what to do with the key. But then.... The key"
        " begins to emit a blue light."
    )
    time.sleep(5)
    print(
        "Then suddenly you feel a surge of energy flow through your body. "
        " Your are pulled towards the key, you feel like you are being"
        " transported ..."
    )
    time.sleep(3)
    print(
        "Congratulations! You have succesfully completed the Mountain level!"
    )


def sound_guess():
    # You want to scare the unicorn, to make a game of it you have made a list
    # of words, if the guess the correct word they can scare the unicorn and
    # get the key, and end the world
    # if they can't correctly guesse the word they will also be able to get
    # the key but they give an apple
    input_ = 0
    guesses = 3
    while input_ < guesses:
        sound_input = input("Make a sound: ")
        if sound_input in words:
            print(
                "Yess!! You made a sound that scared the unicorn! \n The"
                " unicorn drops the object and runs away. You check what it"
                " is, it is the key indeed."
            )
            end_key_found()
            break
        else:
            if input_ < 2:
                print("Try again")
            input_ += 1
            if input_ == 3:
                print(
                    "You haven't made a sound that scared the unicorn, but you"
                    " remember that you have an apple in your pocket. You"
                    " give the apple to the unicorn. The unicorn drops the key"
                    " and picks the apple. The unicorn flees. Now you have the"
                    " key."
                )
                end_key_found()


def slope():
    # If you want to walk into the valley and not rest you walk until a dead end
    # here you can choose to get back to the rest place, this is also a function
    # or the can choose to kick the mountain and let find the key, that falls
    # of the mountain
    print(
          "\nYou keep on walking further into the valley. After a while, you"
          " notice that there are a lot less trees and that the mountain"
          " sides slowly are approaching. After a while you reach a dead"
          " end. You feel angry about it. You can choose to turn back or"
          " express your anger."
          )
    while True:
        dead_end = input(
            "What do you choose? Turn back or express your anger (back or"
            " anger): "
        )
        if dead_end == "Back" or dead_end == "back":
            print("You walk back.")
            valley_walk()
            break
        elif dead_end == "anger" or dead_end == "Anger":
            print(
                " \nYou kick the mountain slope. You hear a loud sound."
                " Stones are coming down the mountain. You try to hide, by"
                " leaning against the mountain slope. When the stones stop"
                " coming you look around. \nUnder one stone you see somthing"
                " shining. You look under the stone, and you see a key."
                "\n"
            )
            end_key_found()
            break
        else:
            print("Invalid input, choose: turn or anger \n")


def valley_walk():
    # When walking through the valley, there is a resting place. If they want
    # to keep going they come at the that end, the slope function.
    # They can choose to rest, if they do that they come across a unicorn that
    # has the key, before they get it they must choose to be calm and make a 
    #sound to scare the unicorn, the sound_guess function, and find the key.
    # if they decide to run the come also at the dead end and will find a key
    rest_valley_loop = True
    unicorn_1 = True

    print(
        "You keep on walking through the valley. After a while you see a tree"
        " trunk. It looks like a really good resting spot. You can keep on"
        " going or rest here."
    )
    while rest_valley_loop == True:
        rest_valley = input("Do you want to rest here? (y/n): ")
        if rest_valley == "y" or rest_valley == "Y":
            print(
                "\nYou go to the tree trunk. You lie down on the trunk, the"
                " sun is really nice shining on your face, hopefully you get a"
                " bit of a tan. You put all your stuff close to you. You"
                " close your eyes."
            )
            time.sleep(2)
            print(
                "\nAfter a while you wake up, the sun light is blocked. When"
                " you open your eyes, you see a unicorn! You know you have two"
                " options or you keep calm and try not to scare it and your"
                " self or you get your stuff and run away as hard as you can."
            )
            while unicorn_1 == True:
                unicorn = input(
                    "What do you do? Keep calm or run away (choose calm or"
                    " run): "
                )
                if unicorn == "calm" or unicorn == "Calm":
                    print(
                        "\nYou try to stay calm. But when you move, the"
                        " unicorn is scared. It runs away. Just before it"
                        " turns you see that there is something shining in"
                        " it's mouth. You are curious and you decide to"
                        " follow it."
                    )
                    time.sleep(3)
                    print(
                        "You get to an open space, the unicorn is standing in"
                        " the middle of it. Now you see that the thing that it"
                        " has in his mouth looks like a key, but your not"
                        " really sure. So you decide to scare it, and look if"
                        " it drops the key."
                    )
                    print("What sound would you make? (e.g. AHHH or boe) ")
                    sound_guess()
                    unicorn_1 = False
                    rest_valley_loop = False
                elif unicorn == "run" or unicorn == "Run":
                    print("You run further into the valley")
                    slope()
                    unicorn_1 = False
                    rest_valley = False
                    rest_valley_loop = False
                else:
                    print("Invalid input, choose calm or run")
        elif rest_valley == "N" or rest_valley == "n":
            slope()
            rest_valley_loop = False
        else:
            print("Invalid input, choose y/n")


troll_1 = True


def mountain_east():
    # This is the route to the top of the mountain, they can choose at the
    # top to rest. Then they find the key and end the world. Or they can
    # get back down to the t-junction.
    top = True
    print(
        "\nThe path begins to climb, and it gets really steep. After hours you"
        " finally get to the top of the mountain. \nThis wasn't what you had"
        " planned. You can choose to rest on top of a stone block or you can"
        " walk back down."
    )
    time.sleep(4)
    while top == True:
        rest_mountain = input(
            "Do you want to rest or walk back down?  Choose rest or back: "
        )
        if rest_mountain == "Rest" or rest_mountain == "rest":
            print(
                "\nYou sit on the stone block. When you look around you have a"
                " beautiful view. When the sun breaks through the clouds,"
                " something triggers your attention in the corner of your eye."
                " \nWhen you take a take a closer look, you see something"
                " shining under a stone. When you pick the stone up you see a"
                " key under it."
            )
            top = False
            end_key_found()
        elif rest_mountain == "back" or rest_mountain == "Back":
            print(
                "You walk back down the mountain. You are at the t-junction"
                " again"
            )
            mountain_choose()
            top = False
        else:
            print("Invalid input, choose rest or back.")


def mountain_north():
    # When they choose north they can choose to rest. When not, they go to the
    # function mountain_east. When they choose to rest they wake because of 
    # a troll, they can run and then they also go to function mountain_east. 
    # When they stay calm, they go to function sound_make. 
    # Here they get a game to scare the troll
    # And get the key and end the game
    troll_1 = True
    rest_mountain = True
    print(
        "\nYou keep on walking the road on the mountain. After a while you see"
        " an inlet in the mountain slope. It looks like a really good resting"
        " spot. You can keep on going or rest here."
    )
    while rest_mountain == True:
        rest = input("Do you want to rest here? (y/n): ")
        if rest == "y" or rest == "Y":
            print(
                "You go into the inlet. You lie down on the floor, You put"
                " all your stuff close to you. You close your eyes."
            )
            time.sleep(3)
            print(
                "After a while you wake up, there is a shadow on your face. "
                " When you open your eyes, you see a giant troll!\n"
            )
            time.sleep(3)
            print(
                "You know you have two options; you keep calm and try not to"
                " make it angry or you get your stuff and run away as hard as"
                " you can."
            )
            while troll_1 == True:
                troll = input(
                    "What do you do? Keep calm or run away (choose calm or"
                    " run): "
                )
                if troll == "calm" or troll == "Calm":
                    print(
                        "You try to stay calm. But when you move, the troll"
                        " tries to grab you. But then...\n"
                    )
                    time.sleep(2)
                    print(
                        "The sun breaks through the clouds. The troll"
                        " immediately turns around and runs away. You"
                        " instantly remember that trolls turns to stone when"
                        " they are in contact with sunlight.\nBefore the troll"
                        " ran away, you saw a shining object around the trolls"
                        " neck. You are curious and you decide to follow it."
                    )
                    time.sleep(5)
                    print(
                        "You get to an open space, the troll is standing in"
                        " the middle of it. Now you see that the troll has the"
                        " object in his hand. It looks like a key, so you"
                        " decide to scare the troll, and look if it drops the"
                        " key."
                    )
                    print(
                        "What sound would you make? To make a loud enough"
                        " sound, you have to enter 3 integer numbers. "
                        " (Hopefully you enter the right numbers) "
                    )
                    sound_make()
                    troll_1 = False
                    rest_mountain = False
                elif troll == "run" or troll == "Run":
                    print("You run further into the mountain.")
                    mountain_east()
                    rest_mountain = False
                    break
                else:
                    print("Invalid input, choose calm or run")
        elif rest == "n" or rest == "N":
            mountain_east()
            rest_mountain = False
        else:
            print("Invalid input, choose y/n.")


def mountain_choose():
    # Here is the t-junction, or they stay at the mountain or they go back to
    # the valley. South is back to the valley.
    mountain_path = True
    while mountain_path == True:
        path = input("Which path do you choose? North, South or East? ")
        if path == "North" or path == "north":
            mountain_path = False
            mountain_north()
        elif path == "South" or path == "south":
            print(
                " The path goes down the mountain again, and you walk into the"
                " valley."
            )
            mountain_path = False
            valley_walk()
        elif path == "East" or path == "east":
            mountain_path = False
            mountain_east()
        else:
            print("Invalid input, choose between north/south/east. ")


def sound_make():
    # This is the game to scare the troll
    # Here they have to make a number above 15 to scare the troll.
    # If the result isn't above 15, the troll will give the key in exchange for
    # a mirror. Both get the key and end the game.
    import time
    
    # to add up the different integer numbers, without getting an error if
    # there is an invalid input.
    def integer_number(x):
        number_under_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        while True:
            first_number = input("Enter an integer number under 10: ")
            print()

            if first_number.isdigit():
                first_number = int(first_number)  
                # Makinf sure that the input is integer

            if first_number not in number_under_10:  
                # If number isn't in {1-10}
                print(
                    "You have entered an invalid value. Please choose a "
                    "number between 1 and 10."
                    )
            else:
                return x + first_number
                break

    number_total = 0
    input_times = 0
    enters = 3
    scare_troll = False
    while input_times < enters:
        number_total = integer_number(number_total)
        input_times += 1
    
    # total to check if the end total is above 15
    print(f'Your total is {number_total}')

    while scare_troll == False:
        if number_total < 15:
            print("\nYour sound wasn't loud enough.")
            print(
                "\nYou haven't made a sound that scared the troll. It looks"
                " angry at you. But then you remember you have a mirror in"
                " your backpack. You try to give it. Hopefully the troll let's"
                " go of the key."
            )
            time.sleep(3)
            print(
                "It works! The troll let's go of the key, picks the mirror and"
                " goes away.\nYou have the key now."
            )
            end_key_found()
            scare_troll = True
        else:
            print(
                "Yess! Your sound was loud enough to scare the troll. The"
                " troll drops the key and flees. You have the key now."
            )
            end_key_found()
            scare_troll = True


def mountain_function():
    # The choose to go to the mountain
    # The t-junction is next
    print(
        "\n"
        "You walk up the mountain, the road is steep but fortunately the"
        " path is clearly visible. The trees have made place for small plants"
        " and rocks. After a while, you come across a t-junction. One road"
        " heads north, up the mountain. You can't see where the path goes,"
        " because of the dense fog. Another path goes south, down the mountain"
        " again. But you can't be sure because the path turns a corner."
        " Finally, there is a path that goes east. That path goes straight"
        " ahead, but it looks very steep."
    )
    time.sleep(4)
    mountain_choose()


valley = True


def valley_function():
    # The choose to go to the valley
    # There is a choose to go to a bridge, here they have to fix the bridge
    # When the bridge is fixed, they go to the mountain_function
    # When the bridge isn't fixed or they don't want to go to the bridge, they
    # walk furtger into the valley, the valley_walk function
    valley = True
    bridge = False
    import random
    import time

    number_choose = [1, 2, 3, 4, 5]

    number_random = random.randint(1, 5)
    #print(number_random)

    print(
        "\nYou walk into the valley, beside you are blooming trees"
        " and behind them you can see mountains. After a while you see a small"
        " river appearing next to you. There is an old wooden bridge crossing"
        " the river. You can see a path at the other side of the river."
    )
    while valley == True:
        walk = input("Do you walk to the bridge? (choose y/n) ")
        if walk == "y" or walk == "Y":
            print(
                "You walk towards the bridge, and you try to get over it."
                " When you try to get over the bridge, the bridge collapses."
                " Now you have to find a way to get over the bridge, you see"
                " rope and wooden blocks that you can use to repair the"
                " bridge."
            )
            while bridge == False:
                material = input(
                    "What material do you choose to repair the bridge?  Do you"
                    " choose the rope or the wooden blocks? (wood or rope): "
                )

                if material == "Wood" or material == "wood":
                    print(
                        "You repair the bridge with the wood. It looks"
                        " stable enough te use. You carefully cross the river"
                        " and you see a pathway. The path leads you up the"
                        " mountain."
                    )
                    time.sleep(3)
                    bridge = True
                    valley = False
                    mountain_function()

                elif material == "rope" or material == "Rope":
                    print(
                        "You try to repair the bridge with rope. To"
                        " succesfully repair the bridge you have to guess the"
                        " right number between one and five."
                    )
                    bridge = True
                    while True:
                        repair = input("Choose a number between 1 and 5: ")
                        print()

                        if repair.isdigit():
                            repair = int(repair)  
                            # Making sure that the input is integer

                        if repair not in number_choose:  
                            # If number isn't in {1-5}
                            print(
                                "You have entered an invalid value. Please "
                                "choose a number between 1 and 5."
                                )
                        elif repair == number_random:
                            print(
                                "Good guess! The bridge is fixed, you cross"
                                " the river carefully and you see a pathway."
                                " The path leads you up the mountain."
                            )
                            valley = False
                            mountain_function()
                            break
                            
                        else:
                            print(
                                "Wrong guess! The bridge isn't steady, you"
                                " can't cross the river. You have to walk"
                                " further into the valley. \n"
                            )
                            valley = False
                            valley_walk()
                            break
                else:
                    print("invalid input, choose rope or wood \n")

        elif walk == "n" or walk == "N":
            valley = False
            valley_walk()
        else:
            print("Invalid input, choose between y/n")


# Start of world program
def mountain():
    # the player stand infront of the mountain
    # They have to choose which way they want to go, up the mountain or
    # into the valley
    print(
        "You walked through the blue portal. When you look around, you see"
        " mountains and a large valley. The trees, in the valley and on the"
        " mountain are very green."
    )
    time.sleep(3)
    print(
        "\nYou're standing at the foot of the mountain., You see a old little"
        " man standing next to a old wooden board. The old man has something"
        ' to tell you, he says: "If you want to succeed your quest, you have'
        ' to find the key to succes, good luck to you!" \n'
    )

    time.sleep(6)
    print(
        "The old man is gone before you get the chance to ask what he means"
        " exactly. You turn to the board, there is something written on it,"
        " the letters are barely visible. You can make out what is written:"
        " Danger! Keep out!."
    )
    time.sleep(3)
    print(
        "\nNow you're not really feeling any better. Hopefully you will"
        " understand more once you're on your way. You look at your"
        " surroundings, there is a path that follows the mountain and there"
        " is a path that goes into the valley."
    )
    answer = True
                
    while answer == True:
        question_1 = input(
            "What path do you choose? Up the mountain or into the valley? "
            "(choose mountain or valley): "
            )
        if question_1 == "Valley" or question_1 == "valley":
            valley_function()
            answer = False
        elif question_1  == "mountain" or question_1  == "Mountain":
            mountain_function()
            answer = False
        else:
            print("Invalid input, choose valley or mountain")

