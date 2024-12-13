import random

colors = ["BLUE", "RED", "YELLOW", "WHITE"]
colorCode = random.sample(colors, 2)
life = 12

def isChoiceValid (playerChoice, colors):
    for c in playerChoice:
        if c not in colors:
            return False
    return True

def isChoiceRight(colorCode, playerChoice):
    if playerChoice == colorCode:
        return True
    return False

def mastermind():
    print("Welcome to the Mastermind")
    print("Guess the secret two colors combination")
    print("The colors are BLUE, RED, YELLOW and WHITE")
    print("You have 12 try")
    
    for tryNum in range(1, life + 1):
        print("Try", tryNum, "/", life, ":", life - tryNum, "lives left")
        playerChoice = input("Choose two colors : ").split()    
        if isChoiceValid(playerChoice, colors) == False:
            print("Invalid choice, please use two of these colors: BLUE, RED, YELLOW, or WHITE")
            continue
        if isChoiceRight(colorCode,playerChoice) == True:
            print("You win, you find the right color combination")
            return
    print("You loose, the right color combination was:",colorCode)

mastermind()

