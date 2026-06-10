import random

def RPS():
    print("Welcome to Rock paper scissors! All you have to do is type 'rock', 'paper',")
    print("or scissors, you will try to keep up against me so goodluck! Score will also be counted.")
    print("Let's start!")
    Score = 0
    ComputerScore = 0
    RPS_choices = ["rock", "paper", "scissors"]
    while True:
        Computer = random.choice(RPS_choices)
        inputX = input("Type Rock, Paper or Scissors, Otherwise type X to quit: ").lower()
        if inputX == "x":
            print("Are you sure you want to quit? You have a high score of", Score, ".")
            inputY = input("Type Y to confirm or N to continue playing: ").lower()
            if inputY == "y":
                print("Thanks for playing! Check out my other projects like this!")
                break
            elif inputY == "n":
                print("If you say so, let's continue!")
                continue
            else:
                print("Invalid input, continuing the game.")
                continue
        if inputX not in RPS_choices:
            print("Invalid input and not part of rock paper scissors, try again.")
            continue
        print("You chose", inputX)
        print("While I chose", Computer)
        if inputX == Computer:
            print("It's a tie! Try again.")
            continue
        elif (inputX == "rock" and Computer == "scissors") or \
            (inputX == "paper" and Computer == "rock") or \
            (inputX == "scissors" and Computer == "paper"):
            Score += 1
            print("You won this round! Nice! Now your score is", Score, ", And my score is", ComputerScore)
        else:
            ComputerScore += 1
            print("I won this round! Better luck next time! Now your score is", Score, ", And my score is", ComputerScore)
        print("Final Score: You =", Score, ", Computer =", ComputerScore, ".")
        if Score >= 10:
            print("Congratulations! You reached a score of 10 first, so you win! Call the function again to play again!")
            break
        elif ComputerScore >= 10:
            print("I reached a score of 10 first, so I win! Call the function again to play again!")
            break
RPS()