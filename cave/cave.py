import time  # time is imported for aesthetic pauses between lines
hit = False
gift = False
# the monster can be both killed/gifted his diamonds or neither, so while 
# neither has happened, these variables will be false, as soon as one 
# 'activates' or plays out a function where the monster dies/ is gifted
# his diamonds, the corresponding statement  will turn True. This is done 
# so that when the player has gifted/killed the monster the player is not
# able to return to a storyline in which the monster is still alive
# or still wants his diamonds

# You can take one thing at once, but you can return to take another, so 
# the player is able to both give the monster his diamonds and 
# make it out of the cave


def key():
    print("You have taken the key and run back to the cross section. ")
    time.sleep(5)
    run()


def diamonds():

    print("You have taken some diamonds and run back. ")
    time.sleep(5)
    run()

# another choice to make
def left():
    while True:
        print(
            "You turn left and run through a dark tunnel, but at the end of "
            "the tunnel there's a faint glow. "
        )
        time.sleep(5)
        print(
            "You run over and discover the glow is coming from two different"
            " objects, a red key and countless diamonds. "
        )
        time.sleep(3)
        response_5 = input(
            "You're in a hurry and can't take everything.\n\nWhich do you "
            "pick? (key/diamonds) "
        )
        if response_5 == "key":
            key()
            break
        elif response_5 == "diamonds": 
            diamonds()
            break
        else:
            print("Invalid response. Choose key or diamonds.")

def gifted():
    global gift
    gift = True
    run()

# possibility to help the monster or fight it
def diamonds_2():
    while True:
        print(
            'The monster politely asks: "My friend, would you be so kind '
            'to give me my diamonds?" '
        )
        print()
        time.sleep(5)
        print(
            "\"They used to belong to my mother, but she died and they're the "
            "only thing I have left of her.\""
        )
        time.sleep(5)
        print()
        response_8 = input(
            "Will you return the diamonds to the monster? (Yes or No) "
        )

        if response_8 == "Yes":
            print()
            print(
                'The monster is eternally grateful: "Thank you so much my'
                " friend... What is mine, is yours, you are free to do what"
                " you want in my cave! I won't bother you in any way!\"" 
            )
            time.sleep(5)
            print("You continue to look for a way out of the cave.")
            time.sleep(5)
            gifted()
            break

        elif response_8 == "No":
            not_helping()
            break
        else:
            print("Invalid response, answer Yes or No")
    


# this is where you can meet the monster again UNLESS you have killed or
# gifted it therefore both variables need to be False for 
# you to meet the monster
def face_monster():
    global hit
    global gift
    if hit == False and gift == False:
        print()
        print(
            "You turn around to get back to the cross section to get the key,"
            " but all of a sudden you hear a noise coming from the dark."
        )
        time.sleep(5)
        response_7 = input(
            'The monster emerges from the shadows, it asks you: "Hello there'
            " stranger, good to see you again, have you found my precious"
            " diamonds? (Yes/No) "
        )

        if response_7 == "Yes":
            print("You tell the monster you have his diamonds. ")
            time.sleep(3)
            diamonds_2()
        elif response_7 == "No":
            conversation()
        else:
            print("Invalid response, answer Yes or No")
            return 

    else:
        print(
            "You realize that you need the key to open the gate, so you run"
            " back to the intersection."
        )
        time.sleep(5)
        run()

# the non honorable ending

def succes_2():
    print()
    print(
        "You open the gate and run out of the cave, in bittersweet joy you"
        ' exclaim: "I made it! But deep down you feel sorry for the monster."'
    )
    time.sleep(5)
    print("You have completed this level, but at what cost? ")
    print("You are transported back to the portal room.")
    return True


def diamonds_3():
    while True:
        response_11 = input(
            "Do you have the diamonds that belong to the monster? (Yes or No)"
        )
        if response_11 == "Yes":
            diamonds_2()
            break
        elif response_11 == "No":
            print(
                "Well, in that case you will have to go back and "
                 "look for them."
            )
            time.sleep(5)
            run()
            break
        else:
            print("Invalid response, answer Yes or No")

# the honorable ending
def succes():
    print(
        'You open the gate and run out of the cave, in joy you exclaim:'
        '"I made it!"'
    )
    print()
    time.sleep(5)
    print(
        "You have completed this level and you are transported "
         "back to the portal room."
    )
#End of world 4

def word():
    while True:
        response_10 = input(
            "So you have made a promise to a certain monster. Are you a person"
            " of your word? Do you care about your honor? Do you want to"
            " fulfill your promise? (Yes or No) "
        )
        if response_10 == "Yes":
            print(
                "Then you will have to return the lost diamonds to "
                 "the monster."
            )
            time.sleep(5)
            diamonds_3()
            break
        elif response_10 == "No":
            print(
                "Very well, you made the choice, so you will live with a "
                "guilty conscience. "
            )
            time.sleep(5)
            succes_2()
            break
        else:
            print("Invalid response, answer Yes or No")

# checking to see if you're a person of your word
def promise():
    while True:
        response_9 = input(
            "So you have the key, and you want to get out of this cave and "
            "move on with your quest, but have you forgotten about someone? "
            "A monster has feelings too... Have you made a promise that "
            "you have not fulfilled yet? (Yes or No) "
        )
        if response_9 == "Yes":
            word()
            break
        elif response_9 == "No":
            print(
                "Then there shall be no guilty conscience for you, carry on."
            )
            time.sleep(5)
            succes()
            break
        else:
            print("Invalid response, answer Yes or No")

# the way to the gate, but you need the keys
def right():
    while True:
        print(
            "You have taken a right turn, you keep running and end up at a"
            " magnificent red gate!"
        )
        time.sleep(5)
        response_6 = input(
            "You come to realize that the gate is locked, do you have the key?"
            " Yes or No? "
        )

        if response_6 == "Yes": 
            promise()
            break
        elif response_6 == "No":
            face_monster()
            break

        else:
            print("Invalid response, answer Yes or No")
    
# import function, since there are a lot of ways and times to end up at this
# cross section, a lot of functions redirect to this one
def run():
    while True:
        response_4 = input(
            "While running you end up at a cross section. You either have to"
            " take a left, where, you only see darkness, or you take a right "
            "where you see a faint light and hear birds sing. "
            "What side do you  pick? (left/right) "
        )
        if response_4 == "right":
            right()
            break
        elif response_4 == "left":
            left()
            break

        else:
            print("Invalid response, choose left or right.")

# You can kill the monster and therefor hit will turn true and thus you cannot
# come across the monster anymore
def strike():
    global hit
    hit = True
    print(
        "You take your sword and hit the monster right in it's eye, "
        "and behold, the monster stops in it's tracks and drops dead! "
    )
    time.sleep(5)
    print()
    print(
        "Euphorically you celebrate, you continue running through the cave,"
        " to hopefully find a way out. "
    )
    time.sleep(5)

    run()


# Another choice/input function
def duck():
    while True:
        print()
        response_3 = input(
            "You managed to dodge the terrifying monster and rolled away."
            " You now have to choose to either attack the monster or try "
            "and make a run for it. \nWhat do you do? (run/strike)"
        )
        if response_3 == "run":
            print()
            print(
                "You make a run for it and narrowly escape the wrath of the"
                " monster.\nNonetheless, the monster is still chasing you "
                "and you need to escape the cave. "
            )
            time.sleep(5)
            run()
            break
        elif response_3 == "strike":
            strike()
            break

        else:
            print("Invalid response, answer run or strike")

# in this function the player can die and will thus start over
def confront():
    while True:
        print()
        response_2 = input(
            "\"Ah, so you are brave enough to fight me, let's see if you are "
            "\"strong enough, to beat me!\"\n\nThe monster lunges itself at "
            "you from the' dark, unexpectedly, you only have a split second"
            " to react\n\nWhat do you do? (defend/duck) "
        )
        if response_2 == "defend":
            print()
            print(
                "With fast reflexes you manage to put your shield "
                "up between you and the monster, but to no avail, "
                "the monster breaks through the shield and kills you. "
            )
            cave()
            break

        elif response_2 == "duck":
            duck()
        else:
            print("Invalid response, answer confront or duck")


# another choice/input function
def not_helping():
    while True:
        print()
        print(
            "\"You're not gonna help me? This saddens me deeply, because now I"
            ' have no choice but to ask you to leave MY cave"'
        )
        print()
        response_1 = input(
            "You have angered the monster, what do you do? "
            "(leave cave/confront monster)"
        )
        if response_1 == "leave cave":
            print("You went back and left the cave, you have failed your quest")
            cave()
            break
        elif response_1 == "confront monster":
            confront()
            break
        else:
            print("Invalid response, answer leave cave or confront monster")

# in the conversation, the player gets to make his or her first choice to 
# either help or not help the monster, this is done by asking a question in
# an input function based on the players answer the player will be redirected
# to another function if the player enters an incorrect answer the question
# will be asked again
def conversation():
    while True:
        print()
        response = input("Are you gonna help the monster? (Yes or No) ")
        if response == "Yes":
            print(
                '"Ah well that brings a smile to my face, '
                'thank you kind stranger."'
            )
            print()
            time.sleep(5)
            print(
                '"The diamonds are of great emotional value to me and I am '
                'lost without them, please find them quick! Good luck my '
                'friend!" Go look for the monsters diamonds as '
                'quickly as possible!'
            )
            time.sleep(5)
            print()
            run()
            break

        elif response == "No":
            not_helping()
            break
        else:
            print("Invalid response, answer Yes or No.")
            

# the story begins with an introduction to the monster as well as the cave and
# the fact that the monster has something for you to do
def introduction():
    print()
    print(
        "You enter the cave, you have picked up a sword and a shield along the"
        " way, presumably belonging to dead warriors who didn't make it"
        " out of the cave alive, but you are no ordinary person so you enter"
        " the cave with confidence."
    )
    time.sleep(5)
    print()
    print(
        '"Welcome to the cave of madness" a voice coming from the shadows'
        ' says.\n\nHe continues: "To continue on your quest and make it through'
        " my cave, there's something you need to do for me.\""
    )
    print()
    time.sleep(5)
    print(
        '"I have lost my precious diamonds somewhere in this cave, if'
        " you're able to find them and return them to me, I will let you pass"
        ' through my cave freely and no one will bother you."'
    )
    time.sleep(5)
    print()
    print('"Will you promise to find them for me?"')
    time.sleep(3)

    conversation()
    
def cave():
    introduction()
