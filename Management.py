def ManageCountry(Name):
    EnemyPower = 0
    Countrieslist1 = {"Sagitaria": 50000, "Narlosia": 45000, "Faziland": 45000, "2nd Republic of Yugoslavia": 40000, "Slavic Union Of Rasonia": 40000, "Republic Of Menlo": 30000, "The Iron Empire (Fourth Reich)": 30000}
    Countrieslist2 = {"French Empire": 20000, "The Confederacy of Soviet America": 20000, "California": 20000, "The State of America": 20000, "The United Kingdom": 20000, "Empire of Japan": 15000, "The People's Republic of China": 15000, "Farasiania": 15000, "Bharat": 15000, "Union Of South America": 30000, "Oceanian Empire": 30000, "Quebec": 10000, "Aztec Mexico": 25000, "Canada": 20000, "Rome": 30000, "Macedonia": 30000}
    Countrieslist3 = {"Central Asian Union": 30000, "The Southwest African Federation": 30000, "The Islamic State of Arabia": 30000}
    Relationlist = ["Allies", "Friendly", "Neutral", "Rivals", "Enemy", "At War"]
    Traitlist = ["Military Expert", "Balanced", "Expansionist", "Isolationist", "Groundkeeper", "Naval Power"]
    ResourceTrade = 0
    EconomicTrade = 0
    Z = 100000
    XYZ = 10000
    Getnukes = False
    BaseMilitarySpending = 1000000
    BasePopulation = 100000000
    BaseManpower = 1000000
    ManpowerGain = 10000
    BaseEconomy = 10000000000
    BaseResources=1000
    ResourceGain= 10
    NuclearEnergy = 0
    NuclearEnergyGain = 0
    Nukes = 0
    FactoryAmount= 0
    CityAmount= 0
    BarracksAmount= 0
    ResearchCenterAmount= 0
    BaseRP = 10
    EconomyGain = 10000000
    RPGain = 1
    PermenantTradeMultiplier = 1
    Formula = ((((BaseEconomy * 2) + (BaseManpower + BasePopulation)) / Z ) + (BaseMilitarySpending / XYZ))
    print("Lore: In an alternate universe, the Cold War ended in a communist victory, but the world was yet to see the future.")
    print("In the 21st century, many countries have risen and fallen, but new colonies from outside of earth have landed, and are invading our land.")
    print("However, some countries and colonies managed to coexist, while some are still at war.")
    print("However, during 2050, a new world war has started, and a new powerful nation has formed. Your nation, " + Name + ".")
    print("You are a leader of a country, and you must manage your country to make it a global superpower, and defeat everyone!")
    print("Welcome to the country management simulator! In this game, you manage a country!")
    print("Your country's name is decided by you, like the name being " + Name + "!")
    print("You will be given a few options to choose from, and every turn (3 actions in each turn) a random event happens, while also doing your actions per turn!")
    print("A turn is ended after 3 actions are taken. You can also type 'help' to get help on the actions.")
    print("The goal of the game is to make your country a global superpower! (Requirements will be displayed) This is a very tricky game though. Goodluck!")
    print("Heavily based on Pax historia, but only the events and actions part!")
    print("Starting wars depends on your economy, manpower and military spending! (Formula: (((Economy x 2) + (Manpower + Population)) / 100000 ) + (Military spending / 10000)= Military Tier)")
    print("Also, requirements to win: 1B population, 100B economy, 100M manpower, 1000 research points (and all research upgrades), 2000 resources, 5 nukes, and being one of the top 3 countries.")
    print("There is also a hard mode after you beat the game! however it is optional. it is much harder, as you start off with worse stats (everything is divided by 10) and the requirements are 5B population, 1T economy, 500M manpower, 10000 research points, 10000 resources, 25 nukes, and being the top country.")
    print("Goodluck!")
    # Turn counter to allow breaking after the first completed turn
    turn_count = 0
    while True:
        NuclearEnergy += NuclearEnergyGain
        if NuclearEnergy == 500:
            print("You have gotten 500+ nuclear energy. 1 Nuke is awarded.")
            Nukes += 1
            NuclearEnergy -= 500
        while True:
            Actionlist = ["Build", "Trade", "Research", "Military Spending", "War", "Exit", "Help", "Country Stats"]
            print("Country name: " + Name)
            print("Base Population = " + str(BasePopulation))
            print("Base Manpower = " + str(BaseManpower))
            print("Base Economy = " + str(BaseEconomy))
            print("Base Research Points = " + str(BaseRP))
            print("Nuclear bombs amount: " + str(Nukes))
            print("Action list:", Actionlist)
            FirstAction = input("Do your first action: ").lower()
            if FirstAction == "exit":
                print("Thanks for playing! Goodbye!")
                return
            if FirstAction == "help":
                print("Build: Build different types of buildings, factories (to produce consumer goods and trade)," \
                "cities (to produce food, make housing space and increase population), barracks (to increase manpower)," \
                "and research centers (to increase research points and unlock new technologies) but spend some economic funds.")
                print("Trade: Trade with other countries for quick economic boosts and relationship boosts.")
                print("Research: Invest in research to unlock new technologies and improve your country's capabilities.")
                print("Military Spending: Allocate resources to your military to defend your country and expand your influence.")
                print("War: Engage in conflicts with other countries to expand your territory and influence.")
                print("Country Stats: View your country's current stats, including all of the statistics and your territorial influence! (Base stats of territory are 5.)")
            elif FirstAction == "build":
                print("You chose to build! You can build factories, cities, barracks and research centers!")
                print("Choose what to build. F = factory, C = city, B = barracks, R = research center, N = nuke if you have researched nuclear bombs.")
                while True:
                    BuildInfastructure = input("What do you want to build?").lower()
                    if BuildInfastructure == "f":
                        print("You built a factory! Your resource production has increased, and your trading capabilities have improved!")
                        ResourceGain += 10
                        FactoryAmount += 1
                        BaseEconomy -= 200000
                        break
                    elif BuildInfastructure == "c":
                        print("You built a city! Your population increases drastically!")
                        CityPopulation = 1000000
                        BasePopulation += CityPopulation
                        CityAmount += 1
                        BaseEconomy -= 500000
                        break
                    elif BuildInfastructure == "b":
                        print("You built a barracks! You can store more manpower!")
                        BaseManpower += 10000
                        BarracksAmount += 1
                        BaseEconomy -= 125000
                        break
                    elif BuildInfastructure == "r":
                        print("You built a research center! You can gain more research points and unlock new technologies!")
                        RPGain += 1
                        ResearchCenterAmount += 1
                        BaseEconomy -= 250000
                        break
                    else:
                        print("Invalid input! Try again.")
                break
            elif FirstAction == "trade":
                print("You chose to trade! Decide how much resources you want to trade, or decide how much gold you want to trade!")
                print("Trading resources gives you an economic boost, while trading gold gives you resources! This can be used for profits!")
                while True:
                    TradeChoice = input("Do you want to trade resources or gold? Type R for resources, G for gold.").lower()    
                    if TradeChoice == "r":
                        print("You chose to trade resources! You can only trade from 1 to the amount of resource gain you have, otherwise",
                        "you will go in debt of resources! But its your choice. Choose how much resources you want to trade! (1 = 100k economy, 25 resource trade max.) (1 = 200K WITH RESEARCH UPGRADE 'WE BANKING!')")
                        while True:
                            ResourceTrade = int(input("How much resources do you want to trade? (Number): "))
                            try:
                                ResourceTrade = int(ResourceTrade)
                                if ResourceTrade > 0 and ResourceTrade <= ResourceGain:
                                    print("You trade", ResourceTrade, "resources! You now gain, each day, a bonus", ResourceTrade * 100000 * PermenantTradeMultiplier, "economy!" )
                                    EconomyGain += ResourceTrade * 100000 * PermenantTradeMultiplier
                                    ResourceGain -= ResourceTrade
                                    break
                                else:
                                    print("Invalid input! You can only trade from 1 to your current resource gain.")
                            except ValueError:
                                print("Invalid input! Trade with an integer.")
                    if TradeChoice == "g":
                        print("You chose to trade gold! You can only trade from 1 to the amount of economy you have, otherwise",
                        "you will go in debt of gold! But its your choice. Choose how much gold you want to trade! (100k = +1 resourcegain, max 2.5M, minimum 10k economy)")
                        while True:
                            EconomicTrade = int(input("How much gold do you want to trade? (Number): "))
                            try:
                                EconomicTrade = int(EconomicTrade)
                                if EconomicTrade > 99999 and EconomicTrade < 2500001:
                                    print("You trade", EconomicTrade, "gold! You now gain a bonus of", EconomicTrade / 100000, "resources!" )
                                    ResourceGain += EconomicTrade / 100000
                                    EconomyGain -= EconomicTrade
                                    break
                                else:
                                    print("Invalid input! you can only trade fom 10k to 250k economy.")
                            except ValueError:
                                print("Invalid input! Trade with an integer.")
                    if TradeChoice == "g":
                        print("You chose to trade gold! You can only trade from 1 to the amount of economy you have, otherwise",
                        "you will go in debt of gold! But its your choice. Choose how much gold you want to trade! (100k = +1 resourcegain, max 2.5M, minimum 10k economy)")
                        while True:
                            EconomicTrade = int(input("How much gold do you want to trade? (Number): "))
                            try:
                                EconomicTrade = int(EconomicTrade)
                                if EconomicTrade > 99999 and EconomicTrade < 2500001:
                                    print("You trade", EconomicTrade, "gold! You now gain a bonus of", EconomicTrade / 100000, "resources!" )
                                    ResourceGain += EconomicTrade / 100000
                                    EconomyGain -= EconomicTrade
                                    break
                                else:
                                    print("Invalid input! you can only trade fom 10k to 250k economy.")
                            except ValueError:
                                print("Invalid input! Trade with an integer.")
                    else:
                        print("Invalid Input! try again.")
            elif FirstAction == "research":
                print("You chose to research! You can invest in research to unlock new technologies and improve your country's capabilities!")
                print("You can only research certain things with the sufficient amount of research points. Only once per one action! Limit can be increased")
                print("with research points aswell.")
                DictOfResearchUpgrades = {
                    "More research, more technologies!": 10,
                    "We banking!": 10,
                    "Resourceful!": 10,
                    "How much did you spend on military?": 10,
                    "Bigger cities": 15,
                    "Factory frenzy!!": 20,
                    "Order the TANKS!!": 35,
                    "Manpower is key!": 35,
                    "Uranium enrichment": 100,
                    "Nuclear weapons": 150,
                    "World Domination":1000
                }
                DictofUpgrades = {
                    "More research, more technologies!": "Increases your research point gain by 1!",
                    "We banking!": "Trades are much more efficient, x2 for trades.",
                    "Resourceful!": "Increases your resource gain per factory by +5!",
                    "How much did you spend on military?": "Increases your military spending without wasting economy and also boosts manpower gain.",
                    "Bigger cities": "Cities can hold more population, x2.5 population per city.",
                    "Factory frenzy!!": "Factories produce x2 more resources!",
                    "Order the TANKS!!": "Militay spending gets an even bigger boost, and so does manpower.",
                    "Manpower is key!": "Manpower gain is 2x now!",
                    "Uranium enrichment": "Unlocks the nuclear power plant, enriching uranium to produce nuclear energy.",
                    "Nuclear weapons": "Unlock a new section, NUKE. send nuclear missiles to other nations and weaken them! However only 1 nuclear weapon per 3 actions is possible.",
                    "World Domination": "Rule the world... all in your hands......"
                }
                print("Research Upgrades:")
                for key, value in DictOfResearchUpgrades.items():
                    print(key + ": " + str(value) + " RP - " + DictofUpgrades[key])

                # build case-insensitive lookup
                lookup = {k.lower(): k for k in DictOfResearchUpgrades}
                while True:
                    ResearchChoiceRaw = input("Which upgrade do you want to research? Type the name of the upgrade: ").strip()
                    ResearchChoice = ResearchChoiceRaw.lower()
                    if ResearchChoice not in lookup:
                        print("Invalid input! Try again.")
                        continue
                    key = lookup[ResearchChoice]
                    cost = DictOfResearchUpgrades[key]
                    if BaseRP < cost:
                        print("You don't have enough research points to research this! Try again.")
                        continue

                    # apply research effects
                    print("You researched", key, "!", DictofUpgrades[key])
                    BaseRP -= cost
                    kl = key.lower()
                    if kl == "more research, more technologies!":
                        RPGain += 1
                    elif kl == "we banking!":
                        PermenantTradeMultiplier += 1
                    elif kl == "resourceful!":
                        ResourceGain += FactoryAmount * 5
                    elif kl == "how much did you spend on military?":
                        BaseMilitarySpending += 500000
                        ManpowerGain += 1000
                    elif kl == "bigger cities":
                        BasePopulation = int(BasePopulation * 2.5)
                        BasePopulation += CityAmount * 4000000
                    elif kl == "factory frenzy!!":
                        ResourceGain += FactoryAmount * 10
                    elif kl == "order the tanks!!":
                        BaseMilitarySpending += 1000000
                        ManpowerGain += 3000
                        Z -= 20000
                    elif kl == "manpower is key!":
                        ManpowerGain *= 2
                    elif kl == "uranium enrichment":
                        NuclearEnergyGain += 100
                    elif kl == "nuclear weapons":
                        Getnukes = True
                    elif kl == "world domination":
                        NuclearEnergyGain += 150
                        Nukes += 1
                        ManpowerGain *= 3
                        BaseMilitarySpending += 5000000
                        ResourceGain += FactoryAmount * 25
                        CityPopulation = 5000000
                        PermenantTradeMultiplier += 3
                        RPGain += ResearchCenterAmount * 3
                        Z -= 20000
                        XYZ -= 2000

                    # remove researched upgrade
                    DictOfResearchUpgrades.pop(key, None)
                    DictofUpgrades.pop(key, None)
                    break
                # end research action
                break
            elif FirstAction == "military spending":
                print("You chose to spend on the military! You can allocate resources to your military to defend your country and expand your influence!")
                print("Military Spending increases your military tier's strength (in the formula, military spending is a part) and also increases manpower!")
                print("Based on every 10M dollars you spend, you get +100 manpower gain and a permenant manpower boost (Up to 250000 manpower)")
                print("Also, based on every 100M dollars you spend, your formula is better. So you technically get a better chance at defeating others.")
                while True:
                    MilitarySpending = input("How much do you want to spend on the military? (Number):")
                    if MilitarySpending == int:
                        MilitarySpending = int(MilitarySpending)
                    elif MilitarySpending == float:
                        MilitarySpending = float(MilitarySpending)
                    elif MilitarySpending != int and MilitarySpending != float:
                        print("Invalid input! Try again.")
                    if MilitarySpending == int or MilitarySpending == float:                    
                        MilitarySpending += BaseMilitarySpending
                        MilitarySpending -= BaseEconomy
                        if MilitarySpending <= 10000000:
                            ManpowerGain += MilitarySpending / 100000
                            break
                        elif MilitarySpending >= 100000000:
                            for _ in range(int(MilitarySpending / 100000000)):
                                Z -= 2500
                                XYZ -= 250
                            break
                        else:
                            break
                break
            elif FirstAction == "war":
                print("You chose to go to war! Engaging in conflicts with other countries lets you expand territory and get bonuses!")
                print("However, some countries are stronger than you, but some are weaker! Each country has a certain amount of territories, you start with 3.")
                print("Your formula is complex, but it is based on your economy, manpower and military spending! (Formula: (((Economy x 2) + (Manpower + Population)) / 100000 ) + (Military spending / 10000)= Military Tier)")
                print("You can attack any country you want! However, if you attack a country stronger than you, you may lose all your progress!")
                print("However, nukes can counter that, because they weaken the military tiers in territories!" \
                "(Yes, territories have their own military tiers, but for you, it is YOUR military tier / 3 per territory.)")
                print("However, if your in an alliance, every country in your alliance declares war on the country you attack, giving you advantages!")
                print("Also, if you declare war on a country, there will be no actions! first you must defeat the country ittself. You can decide which territory to attack first!")
                print("Goodluck, and choose wisely!")
                print(str(Countrieslist1))
                print(str(Countrieslist2))
                print(str(Countrieslist3))
                print("You decide which country to attack from the list of countries! (IF YOUR CONFUSED ON THE NAME, IT IS THE LORE OF THE GAME WHICH IS GIVEN IN THE BEGINNING)")







ManageCountry("Russia")