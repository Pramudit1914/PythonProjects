import time, random

def FNAF():
    TIME = 0
    ACTIONAMOUNT = 0
    Probabilities=["You dont hear anything.", "You dont hear anything.", "You dont hear anything.", "You dont hear anything.", "You hear breathing."]
    Probabilities2=["You dont hear or see anything.", "You dont hear or see anything.", "You dont hear or see anything.", "You dont hear or see anything.", "You dont hear or see anything.", "You dont hear or see anything.", "You dont hear or see anything.", "You dont hear or see anything.", "You see something blurry", "You hear breathing"]
    Closet=["....", "....", "....", "....", "....", "....", "....", "....", "....", "The closet door is slightly open."]
    print("You are awoken in a dark room, you have no idea where you are or how you got there.")
    print("its almost like a nightmare. But you somehow have deja vu, but you know you have never been here.")
    print("Your heart is pounding and it cant be stopped. You tell yourself your okay. Its too bad your doors cant be locked, to keep whatevers there away...")
    print("................. Good luck.")
    print("HOW 2 PLAY: Type 'GoToDoor1' to go to the left door, 'GoToDoor2' to go to the right door. 'GoToCloset' to go to the closet in the middle of the room.")
    print("Type 'LookBehind' to look behind you whenever your in the middle of the room behind thee bed.")
    print("There are 4 main monsters. The first one is Freddy, the second one is Bonnie, the third one is Chica, and the fourth one is Foxy. They will all be trying to get you, so be careful.")
    print("All of them come from the doors, except Foxy. He comes from the closet. If it says somethings breathing, NEVER FLASH YOUR FLASHLIGHT.")
    print("When Foxy is there, do NOT look behind you. You have to go up to him and flash your flashlight till he disappears.")
    print("Flashing your flashlight when the other 3 monsters are there, will make you die. You have to wait till they disappear near the door, otherwise they can sneak into your room.")
    print("Also, you have to look behind you if it says you hear breathing when your not near a door. Not nescessary to flash your flashlight.")
    print("You have to survive till 6 am, which is in 6 hours. Every 5 actions, one hour passes. You can type help for instructions again, but it will not count as an action.")
    print("Also, if you see something blurry when you open a door, SHINE YOUR FLASHLIGHT AT ALL COST TO KEEP IT AWAY.")
    print("GOOD LUCK, FACING YOUR NIGHTMARE.")
    while True:
        if action_amount >= 5:
            TIME += 1
            action_amount = 0
        if TIME == 6:
            print("You have won the game! Good job! If you want to play again, you can recall the function!")
            return
        else:
            print(f"Amount of Actions done: {action_amount}")
            print(f"Time: {TIME} AM.")
            RandomProbability1=random.choice(Probabilities)
            RandomProbability2=random.choice(Probabilities2)
            RandomProbability22=random.choice(Probabilities2)
            closetingit=random.choice(Closet)
            print(RandomProbability1)
            print(closetingit)
            inputX = str(input("Action: ")).lower()
            if inputX == "help":
                print("HOW 2 PLAY: Type 'GoToDoor1' to go to the left door, 'GoToDoor2' to go to the right door. 'GoToCloset' to go to the closet in the middle of the room.")
                print("Type 'LookBehind' to look behind you whenever your in the middle of the room behind the bed.")
                print("There are 4 main monsters. The first one is Freddy, the second one is Bonnie, the third one is Chica, and the fourth one is Foxy. They will all be trying to get you, so be careful.")
                print("All of them come from the doors, except Foxy. He comes from the closet. If it says somethings breathing, NEVER FLASH YOUR FLASHLIGHT.")
                print("When Foxy is there, do NOT look behind you. You have to go up to him and close the closet door to keep him away.")
                print("Flashing your flashlight when the other 3 monsters are there, they will detect your presence and kill you immediately. You have to wait till they disappear near the door, otherwise they can sneak into your room.")
                print("Also, you have to look behind you if it says you hear breathing when your not near a door. Not nescessary to flash your flashlight.")
                print("Also, if you see something blurry when you open a door, SHINE YOUR FLASHLIGHT AT ALL COST TO KEEP IT AWAY.")
                print("Remember, survive till 6 am and help doesnt count as an action!")
                continue
            elif inputX == "gotodoor1":
                print("You are now at the left door. Open door? Y or N to answer.")
                Ans=input("Answer: ").lower()
                if Ans == "y":
                    print("Opened door.")
                    print(RandomProbability2)
                    print("Shine flashlight? Y or N to answer.")
                    Ans2=input("Answer: ").lower()
                    if Ans2 == "y":
                        print("You shined flashlight.")
                        if RandomProbability2 == "You see something blurry":
                            print("The blurry thing is gone.")
                            print("You feel relieved.")
                            print("You go back.")
                            action_amount += 1
                            continue
                        elif RandomProbability2 == "You hear breathing":
                            print("You died!")
                            print("Try again! you shined flashlight when something was breathing.")
                            return
                        else:
                            print("Nothing happens.")
                            print("You go back.")
                            action_amount += 1
                            continue
                    else:
                        print("You decide not to shine flashlight.")
                        if RandomProbability2 == "You see something blurry":
                            print("You get a bad feeling about the blurry thing.")
                            print("You go back.")
                            try:
                                Probabilities2.remove("You dont hear or see anything.")
                            except ValueError:
                                pass
                            action_amount += 1
                            continue
                        elif RandomProbability2 == "You hear breathing":
                            print("You dont shine the flashlight.")
                            print("The breathing is gone. You feel relieved.")
                            action_amount += 1
                            continue
                        else:
                            print("Nothing happens.")
                            print("You go back.")
                            action_amount += 1
                            continue
                else:
                    print("You decide not to open the door.")
                    action_amount += 1
                    try:
                        Probabilities2.remove("You dont hear or see anything.")
                    except ValueError:
                        pass
            elif inputX == "gotodoor2":
                print("You are now at the right door. Open door? Y or N to answer.")
                Ans=input("Answer: ").lower()
                if Ans == "y":
                    print("Opened door.")
                    print(RandomProbability22)
                    print("Shine flashlight? Y or N to answer.")
                    Ans2=input("Answer: ").lower()
                    if Ans2 == "y":
                        print("You shined flashlight.")
                        if RandomProbability22 == "You see something blurry":
                            print("The blurry thing is gone.")
                            print("You feel relieved.")
                            print("You go back.")
                            action_amount += 1
                            continue
                        elif RandomProbability22 == "You hear breathing":
                            print("You died!")
                            print("Try again! you shined flashlight when something was breathing.")
                            return
                        else:
                            print("Nothing happens.")
                            print("You go back.")
                            action_amount += 1
                            continue
                    else:
                        print("You decide not to shine flashlight.")
                        if RandomProbability22 == "You see something blurry":
                            print("You get a bad feeling about the blurry thing.")
                            print("You go back.")
                            try:
                                Probabilities2.remove("You dont hear or see anything.")
                            except ValueError:
                                pass
                            action_amount += 1
                            continue
                        elif RandomProbability22 == "You hear breathing":
                            print("You dont shine the flashlight.")
                            print("The breathing is gone. You feel relieved.")
                            action_amount += 1
                            continue
                        else:
                            print("Nothing happens.")
                            print("You go back.")
                            action_amount += 1
                            continue
                else:
                    print("You decide not to open the door.")
                    action_amount += 1
                    try:
                        Probabilities2.remove("You dont hear or see anything.")
                    except ValueError:
                        pass
            elif inputX == "lookbehind":
                print("You look behind yourself.")
                if RandomProbability1 == Probabilities[4]:
                    print("You just saw a disturbing version of a bear toy. It was disturbing. However its gone now.")
                else:
                    print("Theres nothing.")
                if closetingit == Closet[9]:
                    print("Foxy was in the closet! Looks like he killed you when you werent looking.")
                    print("Good try! If you want to play again, call the function again and goodluck!")
                    return
                else:
                    print("...")
                    action_amount += 1
            elif inputX == "gotocloset":
                print("You head to the closet. Open the closet door?")
                inputY = input("Y or N to answer: ")
                if inputY == "N":
                    print("You decide not to open the closet door. Instead you shut it.")
                    if closetingit == Closet[9]:
                        print("You feel relieved. Like something was in there.")
                    else:
                        print("You shut the closet door. It didnt feel like anything was in there.")
                    action_amount += 1
                elif inputY == "Y":
                    print("You open the closet door.")
                    if closetingit == Closet[9]:
                        print("You see legs stretching down and a sharp hook. You get stabbed.")
                        print("You have died to Foxy! Remember, he slightly leaves the closet open! always close it if it is!")
                        print("Call the function again to play again.")
                        return
                    else:
                        print("Nothing is inside.")
                        action_amount += 1

FNAF()