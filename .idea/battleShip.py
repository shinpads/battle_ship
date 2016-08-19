"""BattleShip game by Rob Farlow and David MacLean"""
from random import randint
aiBoard = [["◻" for x in range(5)]for k in range(5)]
userBoard = [["◻" for x in range(5)]for k in range(5)]
userBoat = []
aiBoat = [randint(0, 5), randint(0, 5)]
print(aiBoat)
gameOver = False
def aiGuess():

    aiguess = [randint(0, 4),randint(0, 4)]
    if userBoat == aiguess :
        print("You Lost")
        gameOver = True
    else:
        userBoard[aiguess[0]][aiguess[1]] = "0"
        for i in range(5):
            print("  ".join(userBoard[i]))
    return

def userGuess():
    print("----------------------------------------------------------------------------------------")
    for x in range(5):
            print("  ".join(aiBoard[x]))
    print("guess a position")
    guess = input().split()
    guess = [int(p) for p in guess]
    if guess == aiBoat:
        print("You win")
        gameOver = True
    else:
        aiBoard[guess[0]][guess[1]] = "0"
    return

print("Enter the location of your boat:")
userBoat = input().split()
userBoat = [int(k) for k in userBoat]
print(userBoat)
userBoard[userBoat[0]][userBoat[1]]= "B"


while gameOver == False:
    userGuess()

    aiGuess()
