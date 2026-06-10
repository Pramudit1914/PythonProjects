import random, time

# Add this helper function near the top of your file
def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def SRPG():
    OwnTitan=False
    money = 0
    health = 100
    abilitycooldown={}
    cooldowns={}
    dg = 1.0
    abilities = ["punch (p)"]
    Damage = {"p":35}
    EnemyHealth=0
    Lives=1
    Status=""
    RemainingLives=Lives
    defense=1
    EnemyLives=1
    currenttitan=None
    print("Welcome, player, This is the Noob experiment RPG. You are a noob, You have to exterminate all experiments.")
    print("This RPG is long, but doesnt save! Lets start, [THIS GAME MIGHT BE GRINDY AND HARD, SO SORRY, ITS IN ITS ALPHA STAGE ANYWAY]")
    print("You are a noob. You used to work in a facility. Something wrong happened. Something. Happened.")
    print("An experiment? Why are its eyes yellow? What is it doing here? Something is off.")
    print("You see more of the experiments. What is happening? The alarm goes off. The experiments are out of control.")
    print("You run to see your fellow noobs get killed, you run as fast as you can, and ran away from the facility.")
    print("You now have to survive against the invasion. Goodluck.")

    while True:
        print(f"You have {money} money, {health} health, a {dg}x damage boost, and {defense}x defense.")
        C2 = get_valid_input(
            "Do you want to see the update logs, kill experiments or see the upgrade shop? (upd, kill, shop, x to exit)",
            ["upd", "kill", "shop", "x"]
        )
        if C2 == "upd":
            print("Heres the Latest update log.")
            print("// V1.0 Release: Shop mechanic with Upgrades, Mechs, Titans, Experiment Fighting mechanic, and a final wave mechanic (Finale of the entire game).")
            print("// V1.1 First Update: Wars Titans, Defense mechanics, Brickbattler titan buffs but no second life. Also Buffed Finale Wave and some experiments.")
            print("// V1.2 Update: Nerfed titan brickbattler HP and defense but added second life back. Revamped Most of Necro Juggernaut. John doe Titan and above titans are known as 'Special titans'. Nerfed Mech brickbattler's SS ability (Swords) a bit.")
            print("// V1.3 Update: Added a rage mode to Bloxxer titan, Nerfed Titan Guest's Rage mode for balancing. Buffed 1X1X1X1 titan and Upgraded Boss Noob and gave them a second life. Also Reduced the seconds for [EASTER EGG]. Nerfed Necro Juggernaut's Health and defense a bit.")
            print("// V1.3.1 Bug Fixes: Fixed Major bugs, Made some inputs validation robust, Fixed some typos, and Decreased The Chance for Larger experiments (30 -> 25), Also for some people wondering why defense is '0.9' or something like that, its because the damage taken is multiplied by it, decreasing the damage taken.")
            print("// V1.4 Massive Update: Nerfed Blaster's damage a bit for balancing, and to make rocket launcher seem better, Added Cooldowns (A VERY BALANCING CHANGE) to powerful abilities like [___], Removed jetpack cause it is very confusing. Fixed not losing money when buying John doe or Bloxxer titan. Added John doe mech and Bloxxer mech.")
            print("// V1.4.1 Minor Update: Buffed Guest Titan's Rage mode, fixed minor bugs and ACTUALLY added timestop.")
            print("// V1.5 WIP update?! Removed Necro juggernaut temporarily, Map 2 added (Not done yet), with new enemies that are MUCH stronger! However, high risk always means high reward. Also buffed Rage mode for all titans")
            continue

        if C2 == "x":
            print("You quit the game.")
            break

        if C2 == "shop":
            print("Heres the shop!")
            while True:
                C3 = input("Get upgrades, Make a mech or call titan? (Upgrade, Mech, Titan), X to exit!: ").lower()
                if C3 == "x":
                    print("You choose to exit the shop. See you!")
                    break
                if C3 == "upgrade":
                    print("You chose upgrades. Which upgrade?")
                    C4 = input("Blaster, Rocket launcher, become large Or equip armor?(Blaster, Rocket, Large, Armor): ").lower()
                    if C4 in ["blaster", "rocket", "large", "armor"]:
                        print(f"You chose {C4}. Good choice! Its pretty much self explanatory but, (Yes or no to answer the following inputs)")
                        if C4 == "blaster":
                            print("This blaster is fast, but medium damage against any larger experiment.")
                            UP1 = input("Do you want to buy it for 75$?").lower()
                            if UP1 == "yes" and money >= 75:
                               print("You now have a blaster ability.")
                               abilities.append("blaster (B)")
                               Damage["b"] = 75
                               money -= 75
                               abilitycooldown["b"]=0
                            elif UP1 == "yes":
                               print("Not enough money!")
                        elif C4 == "rocket":
                            print("This rocket launcher is slow, but can do high damage against many large experiments.")
                            UP2 = input("Do you want to buy it for 100$?").lower()
                            if UP2 == "yes" and money >= 100:
                               print("You now have a rocket ability.")
                               abilities.append("rocket (R)")
                               Damage["r"] = 150
                               money -= 100
                               abilitycooldown["r"]=1
                            elif UP2 == "yes":
                               print("Not enough money!")
                        elif C4 == "large":
                            print("You can make yourself a large noob! You do better damage, have more health and overall better.")
                            UP4 = input("Become a large noob for 300$! Upgrades you got originally will save. (10% Damage boost, Has 750 Health)").lower()
                            if UP4 == "yes" and money >= 300:
                               print("You now have a slam ability, 1.1x damage boost and 750 hp.")
                               health += 650
                               dg += 0.1
                               defense=1
                               abilities.append("Slam (S)")
                               Damage["s"] = 250
                               abilitycooldown["s"]=2
                               money -= 300
                            elif UP4 == "yes":
                               print("Not enough money!")
                        elif C4 == "armor":
                            print("You can equip armor! It has various benefits, like upgrading weapons a bit, and increasing health.")
                            UP5 = input("Buy and Equip armor for 150$! (Gives you extra 300 Health, 10% Damage boost)").lower()
                            if UP5 == "yes" and money >= 150:
                                print("You now have 10% more damage boost and 300 extra hp.")
                                health += 300
                                dg += 0.1
                                money -= 150
                            elif UP5 == "yes":
                               print("Not enough money!")
                    else:
                        print("Not valid. Please enter something valid.")
                        continue
                elif C3 == "mech":
                    print("You choose to make a mech. Which mech would you like to make and control?")
                    C5 = input("There are blueprints of Noob mech, Guest mech, Builder Mech, and BrickBattler Mech(Noob, Guest, Builder, BrickBattler): ").lower()
                    if C5 in ["noob","guest","builder","brickbattler"]:
                        print(f"You chose {C5} Mech. Good choice! (This replaces yourself. Also answer yes or no to answer the questions below.),")
                        if C5 == "noob":
                            print("The noob mech has guns on its back which launch highly penetrable bullets. Any Damage boost applied will remain the same.")
                            Buy5 = input("Would you like to make this for 650$? (Has 1.75K Hp)").lower()
                            if Buy5 == "yes" and money >= 650:
                               print("You now have guns, stomp and a powerful punch.")
                               abilities.extend(["Guns (G)", "stomp (S)", "Super Punch (SP)"])
                               Damage["g"] = 300
                               Damage["s"] = 150
                               Damage["sp"] = 200
                               abilitycooldown["g"]=2
                               abilitycooldown["sp"]=1
                               abilitycooldown["s"]=0
                               health=1750
                               defense=1
                               abilities=["Guns (G)","stomp (S)","Super Punch (SP)"]
                               money -= 650
                            elif Buy5 == "yes":
                               print("Not enough money!")
                        elif C5 == "guest":
                            print("The Guest mech has rocket shells on its back and has boomboxes. Any Damage boost applied will remain the same.")
                            Buy6 = input("Would you like to make this for 1000$? (Has 2.5k Hp)").lower()
                            if Buy6 == "yes" and money >= 1000:
                               print("You now have rockets, boomboxes and a powerful punch.")
                               abilities.extend(["RocketS (RS)", "Power Punch (OPP)", "BoomBox (BB)"])
                               Damage["rs"]=400
                               Damage["opp"]=200
                               Damage["bb"]=275
                               abilitycooldown["rs"]=2
                               abilitycooldown["bb"]=1
                               abilitycooldown["opp"]=0
                               health=2500
                               defense=1
                               abilities=["RocketS (RS)","Power Punch (OPP)","BoomBox (BB)"]
                               money -= 1000
                            elif Buy6 == "yes":
                               print("Not enough money!")
                        elif C5 == "builder":
                            print("The builder mech has drills and laser blasters, which shoot a constant laser. Any Damage boost applied will remain the same.")
                            Buy7 = input("Would you like to make this for 1650$? (Has 3.75k Hp)").lower()
                            if Buy7 == "yes" and money >= 1650:
                                print("You made the builder mech!")
                                abilities.extend(["Drill (D)", "Laser (L)", "Power Stomp (PS)"])
                                Damage["d"]=350
                                Damage["l"]=500
                                Damage["ps"]=400
                                abilitycooldown["l"]=2
                                abilitycooldown["ps"]=1
                                abilitycooldown["d"]=0
                                health=3750
                                defense=1
                                abilities=["Drill (D)","Laser (L)","Power Stomp (PS)"]
                                money -= 1650
                            elif Buy7 == "yes":
                                print("Not enough money!")
                        elif C5 == "brickbattler":
                            print("The Brickbattler mech has 2 swords and a timestop ability, which can stop time. Any Damage boost applied will remain the same.")
                            Buy8 = input("Would you like to make this for 2500$? (Has 4.5k Hp)").lower()
                            if Buy8 == "yes" and money >= 2500:
                                print("You made the brickbattler mech!")
                                abilities.extend(["Swords (SS)", "TimeStop (TS)", "Sword Spin (SP)"])
                                Damage["ss"]=400
                                Damage["ts"]=100
                                Damage["sp"]=650
                                abilitycooldown["ts"]=5
                                abilitycooldown["sp"]=2
                                abilitycooldown["ss"]=0
                                health=3750
                                abilities=["Swords (SS)","TimeStop (TS)","Sword Spin (SP)"]
                                defense=1
                                money -= 2500
                            elif Buy8 == "yes":
                                print("Not enough money!")
                    else:
                        print("Invalid Mech name, please choose something valid.")
                        continue
                elif C3 == "titan":
                    print("You choose to call a titan. Which titan would you like to call?")
                    C6 = input("Noob titan, Guest titan, Builder Titan, BrickBattler Titan (NT, GT, BT, BBT, They come after mechs die.): ")
                    if C6 in ["NT", "GT", "BT","BBT"]:
                        if C6 == "NT":
                            print("You chose Noob titan! Good choice! But, Incase you dont know what this does, This will be your FIRST ever titan, no matter normal or [_______]")
                            print("He has 2 rocket launchers and can ignite things on flames with his core. He also has a sword.")
                            Buy9 = input("Would you like to call noob titan for 5000$? (Has 5.75K Hp and 10% Defense)").lower()
                            if Buy9 == "yes" and money >= 5000:
                                OwnTitan=True
                                print("You called Noob Titan!")
                                Damage["cf"]=750
                                Damage["rl"]=450
                                Damage["s1"]=350
                                abilitycooldown["cf"]=3
                                abilitycooldown["rl"]=2
                                abilitycooldown["s1"]=1
                                health=5750
                                defense=0.9
                                abilities=["Core Fire (CF)","Rocket Launchers (RL)","Sword (S1)"]
                                money -= 5000
                            elif Buy9 == "yes":
                                print("Not enough money!")
                        elif C6 == "GT":
                            print("You chose Guest titan! Good choice! But, Incase you dont know what this does, Hes your first ever titan to have a rage mode.")
                            print("He has 2 powerful rocket launchers, boomboxes and can laser things with his core. He can also teleport.")
                            Buy10 = input("Would you like to call guest titan for 8665$? (Has 6.655K Hp And 20% Defense)").lower()
                            if Buy10 == "yes" and money >= 8665:
                                OwnTitan=True
                                print("You called Guest Titan!")
                                Damage["b"]=750
                                Damage["cl"]=1000
                                Damage["pbb"]=650
                                Damage["mp"]=300
                                abilitycooldown["cl"]=4
                                abilitycooldown["b"]=3
                                abilitycooldown["pbb"]=2
                                abilitycooldown["mp"]=0
                                health=6650
                                defense=0.8
                                Lives=2
                                RemainingLives=Lives
                                currenttitan="Guest Titan"
                                abilities=["Blasters (B)","Core Laser (CL)","Powerful BoomBoxes (PBB)", "Mega Punch (MP)"]
                                money -= 8665
                            elif Buy10 == "yes":
                                print("Not enough money!")
                        elif C6 == "BT":
                            print("You chose Builder titan! Good choice! But, Incase you dont know what this does, Hes the best normal titan.")
                            print("He uses drills for hands, Can dig into the ground, His core is like a railgun, high damage but lasts for a very short time, you can hook experiments into the drills.")
                            Buy11 = input("Would you like to call builder titan for 13500$? (Has 8K Hp and 35% Defense)").lower()
                            if Buy11 == "yes" and money >= 13500:
                                OwnTitan=True
                                print("You called Builder Titan!")
                                Damage["pd"]=600
                                Damage["cb"]=1250
                                Damage["h"]=1000
                                Damage["jr"]=700
                                abilitycooldown["cb"]=5
                                abilitycooldown["h"]=4
                                abilitycooldown["jr"]=2
                                abilitycooldown["pd"]=0
                                health=8000
                                defense=0.65
                                Lives=1
                                abilities=["Powerful Drills (PD)","Core Blast (CB)","Hook (H)", "Jetpack Rockets (JR)"]
                                money -= 13500
                            elif Buy11 == "yes":
                                print("Not enough money!")
                        elif C6 == "JDT":
                            print("You Chose John Doe Titan! Good choice! But, Incase you dont know what this does, Hes the first special titan.")
                            print("He has Lasers, has a gravity gun, blade and TV's Which emit red light, destroying anything but the strongest.")
                            Buy12=input("Would you like to call John Doe Titan for 20000$? (Has 10K Hp and 45% Defense)").lower()
                            if Buy12 == "yes" and money >= 20000:
                                OwnTitan=True
                                print("You called John Doe Titan!")
                                Damage["lb"]=1150
                                Damage["gg"]=1450
                                Damage["bl"]=700
                                Damage["tv"]=1750
                                abilitycooldown["tv"]=5
                                abilitycooldown["gg"]=4
                                abilitycooldown["lb"]=2
                                abilitycooldown["bl"]=1
                                money -= 20000
                                health=10000
                                defense=0.55
                                Lives=1
                                currenttitan="John doe Titan"
                                abilities=["Laser blasters (LB)", "Gravity Gun (GG)", "Blade (BL)", "Red Screen TV"]
                            elif Buy12 == "yes":
                                print("Not enough money!")
                        elif C6 == "BXT":
                            print("You chose Bloxxer titan! Good choice! But, Incase you dont know what this does,")
                            print("He is the first special titan to have 2 lives. He has a powerful core laser, Powerful blades on both his hands,")
                            print("He can shoot a cannon from his core, He can also do something SPECIAL, but thats only for the rage mode. (Hint- Something.. BIG...)")
                            print("He can also absorb lasers, giving him health.")
                            Buy13 = input("Would you like to call bloxxer titan for 35000$? (Has 15K Hp and 45% Defense)")
                            if Buy13 == "yes" and money >= 35000:
                                print("You called Bloxxer Titan!")
                                OwnTitan=True
                                abilities=["Powerful Core Laser (PCL)", "Blades (BLS)","Core Cannon (CC)", "Energy Absorption (EA) (ONLY WORKS FOR LASERS)"]
                                Damage={"pcl":2500, "bls":1000, "cc":1250, "ea":0}
                                abilitycooldown["pcl"]=4
                                abilitycooldown["bls"]=1
                                abilitycooldown["cc"]=2
                                abilitycooldown["ea"]=5
                                health=15000
                                defense=0.55
                                Lives=2
                                money-=35000
                                RemainingLives=Lives
                                currenttitan="Bloxxer Titan"
                            elif Buy13 == "yes":
                                print("Not enough money!")
                        elif C6 == "BBT":
                            print("You chose BrickBattler titan! Good choice! But, Incase you dont know what this does,")
                            print("He can stop, reverse time, he has 2 blasters with 3 modes, he has many abilities along from that i forgot :trol: but hes pretty much the best special titan.")
                            Buy14 = input("Would you like to call brickbattler titan for 50000$? (Has 20K Hp And 50% Defense)").lower()
                            if Buy14 == "yes" and money >= 50000:
                                OwnTitan=True
                                print("You called Brickbattler Titan!")
                                Damage = {"ts":750, "pcl":5000, "tss":3000, "pbs":2000, "sp":875}
                                abilitycooldown["pcl"]=6
                                abilitycooldown["tss"]=4
                                abilitycooldown["pbs"]=3
                                abilitycooldown["sp"]=0
                                abilitycooldown["ts"]=8
                                health=20000
                                defense=0.5
                                Lives=2
                                RemainingLives=Lives
                                currenttitan="BrickBattler Titan"
                                abilities=["TimeStop (TS)","Powerful Core laser (PCL)","Powerful Blasters (PBS)", "Time Shurikens (TSS)", "Super Punch (SP)"]
                                money -= 50000
                            elif Buy14 == "yes":
                                print("Not enough money!")
                    else:
                        print("Please choose a valid option from the given options above.")
                        continue
                else:
                    print("Please choose a valid option from the given options above.")
                    continue
    
        elif C2 == "kill":
            if OwnTitan==True:
                Map2=input("Do you want to go to the second map? Higher risks, but higher rewards.. (Y or N to answer): ")
                if Map2.lower()=="y":
                    print("You choose to go to the second map.")
                else:
                    population=["The shadow of a giant, a titan.", "An unordinary experiment..", "An ordinary experiment.", "The ruler of them all.........."]
                    list1A=["Titan experiment", "Boss experiment", "Decoy Boss experiment", "Cloned noob mech"]
                    list1B=["Large Blaster Experiment", "Rocket Mutant experiment", "Large Speaker Experiment"]
                    list1C=["Cloned Experiment", "Normal experiment","Large experiment"]
                    list1D=["UPGRADED BOSS EXPERIMENT", "NECRO TITAN"]
                    running=True
                    while running==True:
                        opplist=["Punch"]
                        Say = random.choices(
                            population,
                            weights=[12.5, 22.5, 60, 5],
                            k=1
                            )[0]
                        RemainingLives = Lives
                        print("Alright! Finding an experiment...")
                        time.sleep(5)
                        print("Found an experiment!")
                        print(Say)
                        if Say == population[0]:
                            EnemyHealth=2500
                            A = random.choice(list1A)
                            print(A)
                        elif Say == population[1]:
                            EnemyHealth=500
                            B = random.choice(list1B)
                            print(B)
                        elif Say == population[2]:
                            EnemyHealth=100
                            C = random.choice(list1C)
                            print(C)
                        elif Say == population[3]:
                            EnemyHealth=10000
                            D = random.choice(list1D)
                            print(D)
                        print("You go first!")
                        remaininghealth=health
                        remainingenemy=EnemyHealth
                        Dict={"Punch":25, "Blast":75, "Speakers":100, "Laser":500, "Saw":600, "Guns":750}
                        if Say == population[1]:
                            if B in [list1B[0], list1B[1]]:
                                opplist=["Punch", "Blast"]
                            else:
                                opplist=["Punch", "Speakers"]
                        elif Say == population[0]:
                            if A in [list1A[1], list1A[2]]:
                                opplist=["Punch", "Laser", "Saw"]
                                Dict = {"Punch":250, "Blast":85, "Speakers":100, "Laser":500, "Saw":600, "Guns":750}
                            else:
                                opplist=["Punch", "Guns"]
                                Dict = {"Punch":300, "Blast":85, "Speakers":100, "Laser":500, "Saw":600, "Guns":750}
                        elif Say == population[2]:
                            if C in [list1C[0]]:
                                opplist=["Punch"]
                                Dict = {"Punch":30, "Blast":85, "Speakers":100, "Laser":500, "Saw":600, "Guns":750, "Screens":250}
                            else:
                                opplist=["Punch"]
                                Dict = {"Punch":25, "Blast":85, "Speakers":100, "Laser":500, "Saw":600, "Guns":750, "Screens":250}
                        elif Say == population[3]:
                            if D == list1D[0]:
                                opplist=["Claw", "Laser", "Saw", "Screens"]
                                Dict = {"Claw":400, "Laser":750, "Saw":800, "Screens":250}
                                EnemyLives=2
                            else:
                                opplist=["Blade", "Blast", "AstroClaw"]
                                Dict = {"Blade":400, "Blast":600, "AstroClaw":1000}
                                EnemyLives=2
                        while True:
                            Status=""
                            print("Attack or Run away?")
                            ADR = input("Input Here: ").lower()
                            if ADR == "attack":
                                print("You attack! Choose one ability to use! Their Keybinds are given.")
                                print("Your abilities:")
                                valid_keys = []
                                for ab in abilities:
                                    name, key = ab.split("(")
                                    key = key.replace(")", "").strip().lower()
                                    cd_left = cooldowns.get(key, 0)
                                    cd_text = f" (Cooldown: {cd_left} turn(s) left)" if cd_left > 0 else ""
                                    print(f"- {name.strip()} [{key}]{cd_text}")
                                    if cd_left == 0:
                                        valid_keys.append(key)
    
                                if not valid_keys:
                                    print("All abilities are on cooldown! You must wait or use Punch.")
                                    chosen_key = "p"
                                else:
                                    chosen_key = get_valid_input(
                                    f"Choose ability key ({', '.join(valid_keys)}): ",
                                    valid_keys
                                    )
                            # Find the matching ability name
                                for ab in abilities:
                                    if ab.lower().endswith(f"({chosen_key})"):
                                        Ability = ab
                                        break
                                dmg = Damage.get(chosen_key, 35)
                                print(f"it did {dmg * dg} damage!")
                                remainingenemy -= dmg * dg
                                if chosen_key == "ts":
                                    print("The Enemy has been stopped from the time stop for 1 round!")
                                    Status="TimeStop"
                                if chosen_key in abilitycooldown:
                                    cooldowns[chosen_key] = abilitycooldown[chosen_key]
                                if remainingenemy <= 0 and EnemyLives == 2:
                                    EnemyLives -= 1
                                    if Say == population[3]:
                                        EnemyHealth=2500
                                        if D == list1D[0]:
                                            print("Upgraded Boss noob has lost his armor and is weakened.")
                                            opplist=["Punch", "Laser", "Saw"]
                                            Dict={"Punch":250, "Laser":500, "Saw":375}
                                        elif D == list1D[1]:
                                            print("Necro Titan Reveals to be 1X1X1X1 TITAN..")
                                            opplist=["Blast", "Blade"]
                                            Dict={"Blast":450, "Blade":300}
                                elif remainingenemy <= 10 and EnemyLives == 1:
                                    if Say == population[0]:
                                        print("The final blow has been dealen. Nice on your achievement, You deserve 600$!")
                                        money += 600
                                    elif Say == population[1]:
                                        print("The final blow has been dealen. Nice on your achievement, You deserve 100$!")
                                        money += 100
                                    elif Say == population[2]:
                                        print("The final blow has been dealen. Nice on your achievement, You deserve 25$!")
                                        money += 25
                                    elif Say == population[3]:
                                        print("The final blow has been dealen. Nice on your achievement, You deserve 2500$")
                                        money += 2500
                                    ASK1 = input("Do you want to find experiment again? Y or N to answer: ").lower()
                                    if ASK1 == "n":
                                        print("Cya then!")
                                        running = False
                                        break
                                    elif ASK1 == "y":
                                        print("Continuing!")
                                        break
                                else:
                                    print(f"Now the opponent has {remainingenemy} health left!")
                            elif ADR == "run away":
                                print("You ran away!")
                                print("Since you gave up, you dont get any loot.")
                                A=input("Would you like to continue? enter Y if yes, Type N if no: ")
                                if A=="y":
                                    print("Continuing...")
                                    break
                                elif A=="n":
                                    print("Exiting...")
                                    running=False
                                    break
                                else:
                                    print("Invalid input! Automatically exiting..")
                                    running=False
                                    break
                            else:
                                print("Invalid input, please choose attack or run away.")
                                continue
                            if Status == "TimeStop":
                                    print("The enemy remains stopped...")
                            else:
                                A = random.choice(opplist)
                                print("Your opponent is thinking of an attack...")
                                time.sleep(3)
                                print(f"He uses {A}!")
                                damage_taken = Dict.get(A, 25) * defense
                                print(f"It does {damage_taken} damage!")
                                remaininghealth -= damage_taken
                                if remaininghealth <= 0 and Lives==2 and RemainingLives==2:
                                    RemainingLives=Lives-1
                                    remaininghealth=health
                                    print("You are raged...... Do your best. This is your last life.")
                                    if currenttitan=="Guest Titan":
                                        print("You are now Guest 666 Titan.")
                                        abilities=["Eye Laser (EL)", "Damaged BoomBox (DBB)", "Fast Punches (FPS)"]
                                        Damage={"el":666, "dbb":444, "fps":222}
                                        abilitycooldown["el"]=3
                                        abilitycooldown["dbb"]=1
                                        abilitycooldown["fps"]=0
                                    elif currenttitan=="BrickBattler Titan":
                                        print("You are now Raged Brickbattler titan.")
                                        abilities=["TimeStop (TS)","Powerful Core laser (PCL)", "Time Shurikens (TSS)", "Punch Barrage (PB)", "Ultra Punch (UP)", "Heavy Punch (HP)"]
                                        Damage={"ts":850, "pcl":5750, "tss":3500, "pb":2500, "up":3750, "hp":1000}
                                        abilitycooldown["ts"]=8
                                        abilitycooldown["pcl"]=6
                                        abilitycooldown["tss"]=3
                                        abilitycooldown["pb"]=2
                                        abilitycooldown["up"]=4
                                        abilitycooldown["hp"]=0
                                    elif currenttitan=="Bloxxer Titan":
                                        print("You are now Raged Bloxxer titan.")
                                        Damage={"pcl":3000, "fps":850, "cc":1650, "ea":0, "nuke":10000}
                                        abilities=["Powerful Core Laser (PCL)", "Fast Punches (FPS)", "Core Cannon (CC)", "Energy Absorption (EA)", "do i even have to explain this? (NUKE)"]
                                        abilitycooldown["nuke"]=10
                                        abilitycooldown["pcl"]=3
                                        abilitycooldown["fps"]=0
                                        abilitycooldown["cc"]=1
                                        abilitycooldown["ea"]=4
                                    continue
                                elif remaininghealth <= 0:
                                    print(f"Looks like you died. Better luck next time!")
                                    ASK0 = input("Would you like to do this again? N or Y to answer: ").upper()
                                    if ASK0 == "N":
                                        print("Exiting experiment finding..")
                                        running = False
                                        break
                                    elif ASK0 == "Y":
                                        print("Continuing finding experiments..")
                                        break
                                    
                                else:
                                    print(f"Looks like you have {remaininghealth} health left!")
                                    continue
                                for key in cooldowns:
                                    if cooldowns[key] > 0:
                                        cooldowns[key] -= 1
    
SRPG()  