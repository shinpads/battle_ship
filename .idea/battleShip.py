"""BattleShip game by Rob Farlow and David MacLean"""
from random import randint
aiboat = [randint(0, 5), randint(0, 5)]
aiboard = []
playerguess = [1,3]
row = ["0","0","0","0","0"]
def aiboard():
    for i in range(5):
        aiboard.append(row)
        print(" ".join(aiboard[i]))

def aiguess():
    aiguess = [randint(0, 5),randint(0, 5)]
    if userBoat == aiguess :
        print("Fuck you! You Lost")
    else:
        p
    return aiguess

userBoard = [["◻" for x in range(5)]for k in range(5)]
userBoat = []
def getUserPlacement(x,y):
    userBoat = [x,y]
    userBoard[x][y] = "X"

def userGuess():
    for x in range(5):
            print("  ".join(userBoard[x]))
    print("guess a position")
    guess = input().split()
    guess = [int(p) for p in guess]
    if guess == aiboat:
        print("Game Over you win")
    else:
        userBoard[guess[0],guess[1]] = "0"

userGuess()