# I modified the game from Learn Python3 the Hard Way exercise 31.

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("""There's a giant bear here eating a cheese cake.\n
    What do you do?
    \t1. Take the cake?
    \t2. Scream for help.""")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("""No body is coming...\n What do you do next?
        \t1. Run away!
        \t2. Try to find weapon, and fight!
        \t3. Engage a punch fight with the bear.""")

        action1 = input("> ")
        
        if action1 == "1":
            print("Your body survives powered by a fast run.")
            print("Good job!")
        elif action1 == "2":
            print("""You find a knife, what do you want try?
            \t1. Jump on him and push the knife into his throat!
            \t2. Nothing, a knife against a bear.. no way!!""")
        
            action2 = input("> ")

            if action2 == "1":
                print("You brave, but the bear is to strong...\n The bear eats you head.. You're die!")
            else:
                print("Doing Nothing is probably the best thing to do!\n Your life is safe!")
        else:
            print("You brave, but the bear is to strong...\n The bear eats your body. You're die!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away!")

elif door == "2":
    print("It looks like a dimentional portal..\n What do you do?")
    print("""
    \t1. Pass through the hollow, and see what's happen.
    \t2. To strange for you. You close the door.
    \t3. You destroys the house where you are!
    """)

    what = input("> ")

    if what == "1":
        print("""
        Welcome to the future.
        Good job! You're arrives in 4030, the world is totally destroyed by the humans.
        Only robots live on this earth right now...
        The human race, left the planets 2000 years ago
        """)
    elif what == "2":
        print("It's probably the best decision you can take!")

    else: 
        print("You put too much C4 around the house, the explosion kills you.")
        print("Game over!")

else:
    print("You stumble around and fall on a knife and die. Good job!.")
