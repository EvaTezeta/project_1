import time  # time is imported for aesthetic pauses between lines


def cave():
    introduction()


# the story begins with an introduction to the monster as well as the cave and
# the fact that the monster has something for you to do
def introduction():
    print(
        "You enter the cave, you have picked up a sword and a shield along the"
        " way, presumably belonging to dead warriors who didn't make it"
        " out of the cave alive, but you are no ordinary person so you enter"
        " the cave with confidence."
    )
    time.sleep(13)

    print(
        '"Welcome to the cave of madness" a voice coming from the shadows'
        ' says\n\nHe continues: "To continue on your quest and make it through'
        " my cave, there's something you need to do for me\""
    )

    time.sleep(11)
    print(
        '"I have lost my precious diamonds somewhere in this cave, if'
        " you're able to find them and return them to me, I will let you pass"
        ' my cave freely and no one will bother you."'
    )
    time.sleep(11)
    print()
    print('"Will you promise to find them for me?"')
    time.sleep(3)

    conversation()

    conversation()


# in the conversation, the player gets to make his or her first choice to either help
# or not help the monster, this is done by asking a question in an input function
# based on the players answer the player will be redirected to another function
# if the player enters an incorrect answer the question will be asked again
def conversation():
    response = input("Are you gonna help the monster? (Yes or No) ")
    if response == "Yes":
        print(
            '"Ah well that brings a smile to my face, '
            'thank you kind stranger."'
        )
        time.sleep(5)
        print(
            ' "The diamonds are of great emotional value to me and I am lost"'
            '" without them, please find them quick! Good luck my friend! "'
            '" Go look for the monsters diamonds as quickly as possible"'
        )
        time.sleep(12)
        run()

    elif response == "No":
        not_helping()
    else:
        print("Invalid response, answer yes or no.")
        return conversation()


# another choice/input function
def not_helping():
    print(
        "\"You're not gonna help me? This saddens me deeply, because now I"
        ' have no choice but to ask you to leave MY cave"'
    )
    response_1 = input(
        "You have angered the monster, what do you do?, (leave cave/confront"
        " monster)"
    )
    if response_1 == "leave cave":
        print("You went back and left the cave, you have failed your quest")
        return cave()
    elif response_1 == "confront monster":
        confront()
    else:
        print("Invalid response")
        return not_helping()


# in this function the player can die and will thus start over
def confront():
    response_2 = input(
        "\"Ah, so you are brave enough to fight me, let's see if you are strong"
        ' enough, to beat me"\n\nThe monster lunges itself at you from the'
        " dark, unexpectedly, you only have, a split second to react\n\nWhat do"
        " you do? (defend/duck) "
    )
    if response_2 == "defend":
        print(
            "With fast reflexes you manage to put you're shield, up between you"
            " and the monster, but to no avail, the monster breaks through, the"
            " shield and kills you. "
        )
        return cave()

    elif response_2 == "duck":
        duck()
    else:
        print("Invalid response")
        return confront()


hit = False
gift = False
# the monster can be both killed/gifted his diamonds or neither, so while 
# neither has happened, these variables will be false, as soon as one 
# 'activates' or plays out a function where the monster dies/ is gifted
# his diamonds, the corresponding statement  will turn True. This is done 
# so that when the player has gifted/killed the monster the player is not
# able to return to a storyline in which the monster is still alive
# or still wants his diamonds


# Another choice/input function
def duck():
    response_3 = input(
        "You managed to dodge the terrifying monster and rolled away, You now"
        " have to, choose to either attack the monster or try and make a run"
        " for it., \nWhat do you do? (run/strike)"
    )
    if response_3 == "run":
        print(
            "You make a run for it and narrowly escape the wrath of the"
            " monster.\nNonetheless, the monster is still chasing you and you"
            " need to escape the cave. "
        )
        time.sleep(9)
        run()
    elif response_3 == "strike":
        strike()

    else:
        print("Invalid response")
        return duck()


# You can kill the monster and therefor hit will turn true and thus you cannot
# come across the monster anymore
def strike():
    global hit
    hit = True
    print(
        "You take your sword and hit the monster right in it's eye, and behold,"
        " the, monster stops in it's tracks and drops dead! "
    )
    time.sleep(9)
    print(
        "euphorically you celebrate, you continue running through the cave, ,"
        " to hopefully find a way out. "
    )
    time.sleep(9)

    run()


# import function, since there are a lot of ways and times to end up at this
# cross section, a lot of functions redirect to this one
def run():
    response_4 = input(
        "While running you end up at a cross section.You either have to"
        " take a left, where, you only see darkness, or you take a right where"
        " you see a faint light and hear birds sing.What side do you"
        " pick? (left/right) "
    )
    if response_4 == "right":
        right()

    elif response_4 == "left":
        left()

    else:
        print("Invalid response, choose left or right.")
        return run()


# another choice to make
def left():
    print(
        "You turn left and run through a dark tunnel, but at the end of the"
        " tunnel there's a faint glow. "
    )
    time.sleep(8)
    print(
        "You run over and discover the glow is coming from two different"
        " objects, a red key and countless diamonds. "
    )
    time.sleep(3)
    response_5 = input(
        "You're in a hurry and can't take everything.\n\nWhich do you pick?"
        " (key/diamonds) "
    )
    if response_5 == "key":
        key()
    elif response_5 == "diamonds": 
        diamonds()
    else:
        print("Invalid response. Choose key or diamonds.")
        return left()


# You can take one thing at once, but you can return to take another, so 
# the player is able to both give the monster his diamonds and 
# make it out of the cave


def key():
    print("You have taken the key and run back to the cross section.")
    time.sleep(7)
    run()


def diamonds():
    print("You have taken some diamonds and run back.")
    time.sleep(5)
    run()


# the way to the gate, but you need the keys
def right():
    print(
        "You have taken a right turn, you keep running and end up at a"
        " magnificent red gate!"
    )
    time.sleep(6)
    response_6 = input(
        "You come to realize that the gate is locked, do you have the key?"
        " Yes or No? "
    )

    if response_6 == "Yes": 
        promise()
    elif response_6 == "No":
        face_monster()

    else:
        print("Invalid response")
        return right()


# checking to see if you're a man of your word
def promise():
    response_9 = input(
        "So you have the key, and you want to get out of this cave and move on"
        " with your quest, but have you forgotten about someone? A monster has"
        " feelings too... Have you made a promise that you have not"
        " fulfilled yet? (Yes or No) "
    )
    if response_9 == "Yes":
        word()
    elif response_9 == "No":
        print(
            "Then there shall be no guilty conscience for you, carry on."
        )
        time.sleep(5)
        succes()
    else:
        print("Invalid response")
        return promise()


def word():
    response_10 = input(
        "So you have made a promise to a certain monster. Are you a person"
        " of your word? Do you care about your honor? Do you wanna"
        " fulfill your promise? (Yes or No) "
    )
    if response_10 == "Yes":
        print("Then you will have to return the lost diamonds to the monster.")
        time.sleep(5)
        diamonds_3()
    elif response_10 == "No":
        print(
            "Very well, you made the choice, so you will live with a guilty"
            " conscience. "
        )
        time.sleep(5)
        succes_2()
    else:
        print("Invalid response")
        return word()


def diamonds_3():
    response_11 = input(
        "Do you have the diamonds that belong to the monster? (Yes or No)"
    )
    if response_11 == "Yes":
        diamonds_2()
    elif response_11 == "No":
        print("Well, in that case you will have to go back and look for them.")
        time.sleep(5)
        run()
    else:
        print("Invalid response")
        return diamonds_3()


# this is where you can meet the monster again UNLESS you have killed or
# gifted it therefore both variables need to be False for 
# you to meet the monster
def face_monster():
    global hit
    global gift
    if hit == False and gift == False:
        print(
            "You turn around to get back to the cross section to get the key,"
            " but all of a sudden you hear a noise coming from the dark."
        )
        time.sleep(9)
        response_7 = input(
            'The monster emerges from the shadows, it asks you: "Hello there'
            " stranger, good to see you again, have you found my precious"
            " diamonds? (Yes/No) "
        )

        if response_7 == "Yes":
            print("You tell the monster you have his diamonds. ")
            time.sleep(4)
            diamonds_2()
        elif response_7 == "No":
            conversation()
        else:
            print("Invalid response")
            return face_monster()

    else:
        print(
            "You realize that you need the key to open the gate, so you run"
            " back to the intersection."
        )
        time.sleep(8)
        run()


# possibility to help the monster or fight it
def diamonds_2():
    print(
        'The monster politely asks: " My friend, would you be so kind to give,'
        " me my diamonds?"
    )
    time.sleep(9)
    print(
        "They used to belong to my mother, but she died and they're the only,"
        " thing I have left of her."
    )
    time.sleep(9)
    response_8 = input(
        "Will you return the diamonds to the monster? (Yes or No) "
    )

    if response_8 == "Yes":
        print(
            'The monster is eternally grateful: "Thank you so much my'
            " friend... What is mine, is yours, you are free to do what you"
            " want in my cave! I won't bother you in any way! " 
        )
        time.sleep(12)
        print("You continue to look for a way out of the cave.")
        time.sleep(5)
        gifted()

    elif response_8 == "No":
        not_helping()
    else:
        print("Invalid response")
        return diamonds_2()

    # this turns the variable true


def gifted():
    global gift
    gift = True
    run()

# the non honorable ending

def succes_2():
    print(
        "You open the gate and run out of the cave, in bittersweet joy you"
        ' exclaim: "I made it! "But deep down you feel sorry for the monster.'
    )
    time.sleep(9)
    print("You have completed this level, but at what cost? ")
    return True


# the honorable ending
def succes():
    print(
        'You open the gate and run out of the cave, in joy you exclaim:'
        '"I made it!"'
    )
    time.sleep(8)
    print("You have completed this level.")
    return True

#End of world 4