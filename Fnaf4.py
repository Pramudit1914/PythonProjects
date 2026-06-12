import time, random

class FNAFEngine:
    def __init__(self):
        self.time = 0
        self.action_amount = 0
        self.probabilities = [
            "You dont hear anything.", 
            "You dont hear anything.", 
            "You dont hear anything.", 
            "You dont hear anything.", 
            "You hear breathing."
        ]
        self.probabilities2 = [
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You dont hear or see anything.", 
            "You see something blurry", 
            "You hear breathing"
        ]
        self.closet = [
            "....", "....", "....", "....", "....", 
            "....", "....", "....", "....", 
            "The closet door is slightly open."
        ]
        self.game_over = False
        self.won = False
        self.death_reason = ""
        self.messages = []
        self.door1_ignored_actions = 0
        self.door2_ignored_actions = 0
        self.freddy_ignored_actions = 0
        
        # Turn-specific rolled states
        self.random_probability1 = ""
        self.random_probability2 = ""
        self.random_probability22 = ""
        self.closet_state = ""
        
        self.roll_turn()

    def roll_turn(self):
        if self.action_amount >= 5:
            self.time += 1
            self.action_amount = 0
            
        if self.time == 6:
            self.won = True
            self.game_over = True
            return

        self.random_probability1 = random.choice(self.probabilities)
        self.random_probability2 = random.choice(self.probabilities2)
        self.random_probability22 = random.choice(self.probabilities2)
        self.closet_state = random.choice(self.closet)

    def execute_action(self, action_type):
        """
        Executes a game action. Returns a dictionary of results.
        action_type can be:
        - "gotodoor1_close"
        - "gotodoor1_open_flashlight"
        - "gotodoor1_open_noflashlight"
        - "gotodoor2_close"
        - "gotodoor2_open_flashlight"
        - "gotodoor2_open_noflashlight"
        - "gotocloset_close"
        - "gotocloset_open"
        - "lookbehind"
        """
        if self.game_over:
            return {
                "status": "game_over" if not self.won else "won", 
                "time": self.time,
                "action_amount": self.action_amount,
                "messages": ["The game is already over."]
            }

        self.messages = []

        # Check if Freddy was breathing on the bed and we ignored it
        if action_type != "lookbehind":
            if self.random_probability1 == "You hear breathing.":
                self.freddy_ignored_actions += 1
                if self.freddy_ignored_actions >= 2:
                    self.game_over = True
                    self.death_reason = "Freddy jumpscared you because you ignored the breathing on the bed for too long!"
                    self.messages.append("Freddy got you! The bed was ignored for too long.")
                    return {
                        "status": "dead",
                        "time": self.time,
                        "action_amount": self.action_amount,
                        "messages": self.messages,
                        "death_reason": self.death_reason,
                        "random_probability1": self.random_probability1,
                        "random_probability2": self.random_probability2,
                        "random_probability22": self.random_probability22,
                        "closet_state": self.closet_state
                    }
            else:
                self.freddy_ignored_actions = 0
        else:
            self.freddy_ignored_actions = 0

        # Check if a monster was at Left Door and we ignored it
        if not action_type.startswith("gotodoor1"):
            if self.random_probability2 in ["You see something blurry", "You hear breathing"]:
                self.door1_ignored_actions += 1
                if self.door1_ignored_actions >= 2:
                    self.game_over = True
                    self.death_reason = "Bonnie broke in from the left door because you ignored it for too long!"
                    self.messages.append("Bonnie got you! The left door was ignored.")
                    return {
                        "status": "dead",
                        "time": self.time,
                        "action_amount": self.action_amount,
                        "messages": self.messages,
                        "death_reason": self.death_reason,
                        "random_probability1": self.random_probability1,
                        "random_probability2": self.random_probability2,
                        "random_probability22": self.random_probability22,
                        "closet_state": self.closet_state
                    }
        else:
            self.door1_ignored_actions = 0

        # Check if a monster was at Right Door and we ignored it
        if not action_type.startswith("gotodoor2"):
            if self.random_probability22 in ["You see something blurry", "You hear breathing"]:
                self.door2_ignored_actions += 1
                if self.door2_ignored_actions >= 2:
                    self.game_over = True
                    self.death_reason = "Chica broke in from the right door because you ignored it for too long!"
                    self.messages.append("Chica got you! The right door was ignored.")
                    return {
                        "status": "dead",
                        "time": self.time,
                        "action_amount": self.action_amount,
                        "messages": self.messages,
                        "death_reason": self.death_reason,
                        "random_probability1": self.random_probability1,
                        "random_probability2": self.random_probability2,
                        "random_probability22": self.random_probability22,
                        "closet_state": self.closet_state
                    }
        else:
            self.door2_ignored_actions = 0
        
        if action_type == "gotodoor1_close":
            self.messages.append("You decide not to open the door.")
            self.action_amount += 1
            try:
                self.probabilities2.remove("You dont hear or see anything.")
            except ValueError:
                pass

        elif action_type == "gotodoor1_open_flashlight":
            self.messages.append("Opened door.")
            self.messages.append(self.random_probability2)
            self.messages.append("You shined flashlight.")
            if self.random_probability2 == "You see something blurry":
                self.messages.append("The blurry thing is gone.")
                self.messages.append("You feel relieved.")
                self.messages.append("You go back.")
                self.action_amount += 1
            elif self.random_probability2 == "You hear breathing":
                self.game_over = True
                self.death_reason = "You shined the flashlight at the left door when something was breathing!"
                self.messages.append("You died!")
                self.messages.append("Try again! you shined flashlight when something was breathing.")
            else:
                self.messages.append("Nothing happens.")
                self.messages.append("You go back.")
                self.action_amount += 1

        elif action_type == "gotodoor1_open_noflashlight":
            self.messages.append("Opened door.")
            self.messages.append(self.random_probability2)
            self.messages.append("You decide not to shine flashlight.")
            if self.random_probability2 == "You see something blurry":
                self.messages.append("You get a bad feeling about the blurry thing.")
                self.messages.append("You go back.")
                try:
                    self.probabilities2.remove("You dont hear or see anything.")
                except ValueError:
                    pass
                self.action_amount += 1
            elif self.random_probability2 == "You hear breathing":
                self.messages.append("You dont shine the flashlight.")
                self.messages.append("The breathing is gone. You feel relieved.")
                self.action_amount += 1
            else:
                self.messages.append("Nothing happens.")
                self.messages.append("You go back.")
                self.action_amount += 1

        elif action_type == "gotodoor2_close":
            self.messages.append("You decide not to open the door.")
            self.action_amount += 1
            try:
                self.probabilities2.remove("You dont hear or see anything.")
            except ValueError:
                pass

        elif action_type == "gotodoor2_open_flashlight":
            self.messages.append("Opened door.")
            self.messages.append(self.random_probability22)
            self.messages.append("You shined flashlight.")
            if self.random_probability22 == "You see something blurry":
                self.messages.append("The blurry thing is gone.")
                self.messages.append("You feel relieved.")
                self.messages.append("You go back.")
                self.action_amount += 1
            elif self.random_probability22 == "You hear breathing":
                self.game_over = True
                self.death_reason = "You shined the flashlight at the right door when something was breathing!"
                self.messages.append("You died!")
                self.messages.append("Try again! you shined flashlight when something was breathing.")
            else:
                self.messages.append("Nothing happens.")
                self.messages.append("You go back.")
                self.action_amount += 1

        elif action_type == "gotodoor2_open_noflashlight":
            self.messages.append("Opened door.")
            self.messages.append(self.random_probability22)
            self.messages.append("You decide not to shine flashlight.")
            if self.random_probability22 == "You see something blurry":
                self.messages.append("You get a bad feeling about the blurry thing.")
                self.messages.append("You go back.")
                try:
                    self.probabilities2.remove("You dont hear or see anything.")
                except ValueError:
                    pass
                self.action_amount += 1
            elif self.random_probability22 == "You hear breathing":
                self.messages.append("You dont shine the flashlight.")
                self.messages.append("The breathing is gone. You feel relieved.")
                self.action_amount += 1
            else:
                self.messages.append("Nothing happens.")
                self.messages.append("You go back.")
                self.action_amount += 1

        elif action_type == "gotocloset_close":
            self.messages.append("You decide not to open the closet door. Instead you shut it.")
            if self.closet_state == "The closet door is slightly open.":
                self.messages.append("You feel relieved. Like something was in there.")
            else:
                self.messages.append("You shut the closet door. It didnt feel like anything was in there.")
            self.action_amount += 1

        elif action_type == "gotocloset_open":
            self.messages.append("You open the closet door.")
            if self.closet_state == "The closet door is slightly open.":
                self.game_over = True
                self.death_reason = "Foxy jumpscared you from the closet because you opened it when he was inside!"
                self.messages.append("You see legs stretching down and a sharp hook. You get stabbed.")
                self.messages.append("You have died to Foxy! Remember, he slightly leaves the closet open! always close it if it is!")
            else:
                self.messages.append("Nothing is inside.")
                self.action_amount += 1

        elif action_type == "lookbehind":
            self.messages.append("You look behind yourself.")
            if self.random_probability1 == self.probabilities[4]:
                self.messages.append("You just saw a disturbing version of a bear toy. It was disturbing. However its gone now.")
            else:
                self.messages.append("Theres nothing.")
                
            if self.closet_state == "The closet door is slightly open.":
                self.game_over = True
                self.death_reason = "Foxy snuck out and killed you when you turned your back while the closet was open!"
                self.messages.append("Foxy was in the closet! Looks like he killed you when you werent looking.")
                self.messages.append("Good try! If you want to play again, call the function again and goodluck!")
            else:
                self.messages.append("...")
                self.action_amount += 1
        
        # Roll variables for next turn
        self.roll_turn()

        status = "alive"
        if self.won:
            status = "won"
        elif self.game_over:
            status = "dead"

        return {
            "status": status,
            "time": self.time,
            "action_amount": self.action_amount,
            "messages": self.messages,
            "death_reason": self.death_reason,
            "random_probability1": self.random_probability1,
            "random_probability2": self.random_probability2,
            "random_probability22": self.random_probability22,
            "closet_state": self.closet_state
        }

def FNAF():
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
    
    engine = FNAFEngine()
    
    while True:
        if engine.won:
            print("You have won the game! Good job! If you want to play again, you can recall the function!")
            return
        if engine.game_over:
            return
            
        print(f"Amount of Actions done: {engine.action_amount}")
        print(f"Time: {engine.time} AM.")
        print(engine.random_probability1)
        print(engine.closet_state)
        
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
            Ans = input("Answer: ").lower()
            if Ans == "y":
                print("Opened door.")
                print(engine.random_probability2)
                print("Shine flashlight? Y or N to answer.")
                Ans2 = input("Answer: ").lower()
                if Ans2 == "y":
                    res = engine.execute_action("gotodoor1_open_flashlight")
                    for m in res["messages"][3:]:
                        print(m)
                else:
                    res = engine.execute_action("gotodoor1_open_noflashlight")
                    for m in res["messages"][3:]:
                        print(m)
            else:
                res = engine.execute_action("gotodoor1_close")
                for m in res["messages"][1:]:
                    print(m)
                    
        elif inputX == "gotodoor2":
            print("You are now at the right door. Open door? Y or N to answer.")
            Ans = input("Answer: ").lower()
            if Ans == "y":
                print("Opened door.")
                print(engine.random_probability22)
                print("Shine flashlight? Y or N to answer.")
                Ans2 = input("Answer: ").lower()
                if Ans2 == "y":
                    res = engine.execute_action("gotodoor2_open_flashlight")
                    for m in res["messages"][3:]:
                        print(m)
                else:
                    res = engine.execute_action("gotodoor2_open_noflashlight")
                    for m in res["messages"][3:]:
                        print(m)
            else:
                res = engine.execute_action("gotodoor2_close")
                for m in res["messages"][1:]:
                    print(m)
                    
        elif inputX == "lookbehind":
            res = engine.execute_action("lookbehind")
            # print outcomes (first is lookbehind print, second is bed contents print, third is closet foxy check)
            for m in res["messages"][1:]:
                print(m)
                
        elif inputX == "gotocloset":
            print("You head to the closet. Open the closet door?")
            inputY = input("Y or N to answer: ").upper()
            if inputY == "N":
                res = engine.execute_action("gotocloset_close")
                for m in res["messages"][1:]:
                    print(m)
            elif inputY == "Y":
                res = engine.execute_action("gotocloset_open")
                for m in res["messages"][1:]:
                    print(m)

if __name__ == "__main__":
    FNAF()