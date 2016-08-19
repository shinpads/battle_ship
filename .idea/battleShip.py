"""BattleShip game by Rob Farlow and David MacLean"""

























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