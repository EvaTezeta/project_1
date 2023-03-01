# Define desert world

def next_functie():
    while True:
        next_ = input(" Next? (yes/y) ")  
        # i want this to be the equivalent of a mouse left-click
        if next_ == "yes" or next_ == "y":
            break
        elif next_ == "no" or next_ =="n":
            print("You have no choice but to say 'yes'.")
        else:
            print("Say 'yes', please.")

def desert():
    # Backstory: how the player ended up in the desert
    print()
    print(
        "You wake up to find yourself standing in the middle of a vast desert."
        " The sun beats down on you relentlessly, and you have no idea how you"
        " got there. You have no food or water, only a single rusty dagger."
        " You see nothing but endless sand dunes stretching in all directions."
        " You keep wondering about how you ended up here, but it feels like"
        " that memory is completely erased. Suddenly you hear a faint voice"
        ' saying, "Find... The... Blue... Crystal... To... Escape...".'
        " Feeling terrified, lonely and desperate you set a goal for yourself:"
        "  Find a way to survive and make it out of the desert alive."
    )
    print()  # Blank line

    # Story: player looks around
    next_functie()
    print(
        "With the blinding sun shining in your eyes it feels"
        " impossible to open them. After some time your eyes are"
        " well adjusted and you are able to open them. Now with a"
        " better vision you look around and observe your"
        " surroundings. In the distance you see an oasis."
    )
    
    print()    
    # Story: player walks towards the oasis
    next_functie()
    print(
        "Since this is the only thing you see in this barren land,"
        " you really have no choice but to make your way towards"
        " the oasis."
    )
    print()
    # Player sees a cactus and ask player if they want to go to it or not
    next_functie()
    print(
        "While you are trying to reach the oasis, you start to"
        " feel thirsty. Suddenly you see a cactus."
    )

    cactus = True
    do = True

    while cactus == True:
        print()  # Blank line
        go_to_cactus = input("Do you go to the cactus? (yes/no) ")
        # Go to the cactus & consequences
        if go_to_cactus == "no" or go_to_cactus == "n":
            print(
                "You don't go to the cactus and keep walking forward. You"
            " are still thirsty."
            )
            while True:
                print()  # blank line
                pee = input(
                    "After a while you get the feeling that you need "
                    "to pee. Do you pee on the sand, or in your hand?"
                    " (sand/hand) "
                )
                # pee on the sand
                if pee == "sand":
                    print(
                        "You pee on the sand. After your deed you keep"
                        " walking forward. As you keep going, your"
                        " throat starts to feel parched and you are"
                        " feeling a bit dizzy. You look for something"
                        " that will quench your, thirst, but when"
                        " there's nothing to be seen the drowsiness"
                        " starts to kick in... And before you know it,"
                        " your body, thuds onto the sand. You died!"
                        " Try the other option."
                    )
                    continue
                # pee in the hand
                elif pee == "hand":
                    print(
                        "You pee in your hand and you drink the pee."
                        " Yikes, that was gross! But it was this, or"
                        " death. Anyways, your thirst is quenched for"
                        " now. Somehow you lost your dagger and you"
                        " didn't notice."
                    )
                    cactus = False
                    break
                    
                else:
                    print(
                        "Sorry, I didn't understand that. Try saying"
                        " 'sand' or 'hand'."
                    )
        elif go_to_cactus == "yes" or go_to_cactus == "y":
            print('You go to the cactus.')
            while do == True:
                print()  # blank line
                cactus = input(
                    "What will you do to the cactus? (touch it/cut it) "
                )
                # Touch cactus
                if cactus == "touch it":
                    print(
                        "You touch the cactus. The spikes on the"
                        " cactus are poisonous! It causes your blood"
                        " to clot immediately, which makes all of your"
                        " organs shut down. You died! Try the other"
                        " option."
                    )
                    continue
                # cut cactus open
                elif cactus == "cut it":
                    print(
                        "You cut the cactus open with your dagger. "
                        "The dagger breaks! Water flows out of the"
                        " cactus and you drink all of it. Your thirst"
                        " is quenched!"
                    )
                    cactus = False
                    do = False
                    
                else:
                    print(
                        "Sorry, I didn't understand that. Try saying"
                        " 'touch it' or 'cut it'."
                    )
            cactus = False
            do = False
        else:
            print(
                "Sorry, I didn't understand that. "
                "Try saying 'yes' or 'no'."
                )
    print()  # blank line

    # story: player arrives at the oasis
    next_functie()
    print()
    print(
        "The sun is as hot as ever, but you keep walking because"
        " the oasis may be the only hope for you to survive."
        " After a while it doesn't seem like the oasis is getting"
        " closer. This makes you feel a bit let down, and you"
        " start to lose hope. To make matters worse, you get"
        " thirsty again and your stomach starts to rumble. So,"
        " you look down in order to block out the negative"
        " thoughts and the desire to drink. Eventually you stopped"
        " seeing sand at your feet and you see something crystal"
        " clear in which you see your reflection. You realize it"
        " is water that you're looking at. You look up to see the"
        " oasis. You can't believe it is actually real and you are"
        " absolutely overjoyed! You arrive at the oasis."
    )

    # story: player drinks water from oasis and eats berries
    next_functie()
    print()
    print(
        "Immediately you went for the water in the oasis and drank"
        " until your thirst was fully quenched., Afterwards you ate"
        " the berries that grew on bushes to satisfy your hunger."
    )

    # player decides whether to make a water pouch or a sharp stick
    while True:
        print()  # blank line
        water_pouch_or_sharp_stick = input(
            "What is the next thing you do? (make a: water pouch / sharp"
            " stick) "
        )
        if water_pouch_or_sharp_stick == "water pouch":
            # make a water pouch
            print("You make a water pouch with leaves from the trees.")
            break
        elif water_pouch_or_sharp_stick == "sharp stick":
            # make a sharp stick
            print("You make a sharp stick with a twig from the trees")
            break
        else:
            print(
                "Sorry, I didn't understand that. Try saying 'water pouch'"
                " or 'sharp stick'"
                )
    print()  # blank line

    # story: player sleeps
    next_functie()
    print(
        "As the sun starts to set, you feel the immense fatigue."
        " You look for a nice grassy patch in the shadow created"
        " by the trees and you make yourself comfortable. Soon"
        " after you fall asleep."
    )

    # story: player wakes up
    next_functie()
    print(
        "The sun is out and you wake up but it feels kind of"
        " weird. You can't seem to get any air. When"
        " you open your eyes, you see that you are being strangled"
        " by a man! He is looking at you with crazy eyes. You"
        " need to stop him or else you'll die!"
    )

    # player defends themselves from the attacker
    while True:
        print()  # blank line
        sharp = input("Do you have something to defend yourself? (yes/no) ")
        # stop the attacker with water pouch
        if sharp == "yes" and water_pouch_or_sharp_stick == "water pouch":
            print(
                "You use your water pouch to hit the man in the face. The"
                " leaves are quite sharp so it makes cuts in his face,"
                " causing him to release his grip on you. That's when you"
                " throw him off of you and knock him out."
            )
            break
        # stop the attacker with sharp stick
        elif sharp == "yes" and water_pouch_or_sharp_stick == "sharp stick":
            print(
                "You use your sharp stick to stab the man in the leg,"
                " causing him to release his grip on you. That's when you"
                " throw him off of you and knock him out."
            )
            break
        elif sharp == "no":
            print("Remember that you made something yesterday!")
        else:
            print(
                "Sorry, I didn't understand that. Try saying 'yes' or 'no'"
            )
    print()  # blank line

    # story: the attacker and his motive
    next_functie()
    print(
        "You wondered why would anyone want to kill me, an"
        " innocent person? We could've survived, together. He must"
        " have been lonely too, right? Then it struck you. Food."
        " That man was probably starving and because, you ate all"
        " the berries yesterday, there was nothing left to be"
        " eaten, except you. After you have shaken these, thoughts"
        " you plan to leave to oasis before he wakes up and you"
        " leave the man behind."
    )
    # story: player leaves the oasis for the temple
    next_functie()
    print(
        "To prepare for your journey ahead you quickly drink some"
        " water from the oasis. You look, around to you to see"
        " where your next destination will be and luckily, not too"
        " far from the oasis, you see a temple., With nowhere"
        " better to go to, you make your way towards the temple."
    )


    # story: player arrives at the temple
    next_functie()
    print(
        "After some time you arrive at the temple. You go inside"
        " of it and walk through - what appears, to be - a very"
        " long hallway."
    )

    # story: player sees two hallways
    next_functie()
    print(
        "At the end of the hallway it splits into two hallways:"
        " left and right. From the left you hear, a faint voice"
        ' calling out to you, "Here... Lies... The... Blue...'
        ' Crystal... Come...". From the right hallway you hear'
        " nothing."
    )


    # player chooses between left/right hallway
    choose_hallway = True
    while choose_hallway == True:
        print()  # blank line
        hallway = input("Which hallway do you choose? (left/right) ")
        # player chooses the left hallway
        if hallway == "left":
            print(
                "You choose the left hallway. You follow the faint voice"
                " to the crystal room."
            )
            print()  # blank line
            break
        # player chooses the right hallway
        elif hallway == "right":
            print(
            "You choose the right hallway. You walk through the silent"
            " hallway and at the end of it you, find yourself standing"
            " in a room lit up by torches. It is an empty room with"
            " only a coffin in the center. The, curiosity got the"
            " better of you and you go towards the coffin. As you got"
            " closer, the coffin started to shake and, then it broke."
            " A mummy emerged from it! You decide to fight the mummy"
            )
            print()  # blank line
            while True:
                print()  # blank line
                fight = input("Did you kill it? (???) ")
                # fight outcome if player had chosen to make a water pouch
                if (
                    fight == "???"
                    and water_pouch_or_sharp_stick == "water pouch"
                    ):
                    print(
                        "You quickly took one of the torches from the"
                        " walls and you fight the mummy with, it. The"
                        " fire from the torch was passed on to the"
                        " mummy and it caught on fire! You stood there"
                        " and watched how the, mummy burnt to a crisp."
                    )
                    print()  # blank line
                    # victory message after beating the mummy
                    print("Yayy, you beat the mummy!")
                    print()  # blank line
                    # player walks through the other door
                    print(
                        "On the other side of the room, you see a door"
                        " that opens by itself. You walk, through it"
                        " and you get to the crystal room."
                    )
                    print()  # blank line
                    choose_hallway = False
                    break
                # fight outcome if player had chosen to make a sharp stick
                elif (
                    fight == "???"
                    and water_pouch_or_sharp_stick == "sharp stick"
                    ):
                    print(
                        "You grab your sharp stick and you stab the"
                        " mummy with it. It didn't die from the, first"
                        " hit, but after ten hits or so it eventually"
                        " fell onto the ground."
                    )
                    print()  # blank line
                    # victory message after beating the mummy
                    print("Yayy, you beat the mummy!")
                    print()  # blank line
                    # player walks through the other door
                    print(
                        "On the other side of the room, you see a door"
                        " that opens by itself. You walk through it"
                        " and you get to the crystal room."
                    )
                    print()  # blank line
                    choose_hallway = False
                    break
                else:
                    print(
                        "Sorry, I didn't understand that. Try saying"
                        " '???'"
                    )
            
        else:
            print(
                "Sorry, I didn't understand that. Try saying 'left' or"
                " 'right'"
            )

    # story: player reaches the crystal room and grabs the blue crystal
    next_functie()
    print(
        "In the crystal room you see the Blue Crystal floating on"
        " a pedestal in the center of the room., It is glowing"
        " blue and it is amanating a strange energy from it. It is"
        " hard to describe, but it feels like it's, calling out to"
        " you. Without a second thought you reach for the Blue"
        " crystal"
    )

    # story: player teleports back to the portal room
    next_functie()
    print(
        "As you grab the crystal, a sudden surge of energy rushes"
        " through your body. You feel a strange, sensation, as if"
        " you are being transported to another place... "\
        "Back to the portal room..." 
    ) #End of world 2

