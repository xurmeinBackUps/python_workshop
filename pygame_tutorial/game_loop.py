import random


def init():
	return None, random.randint(1,10)


def processInput():
	while True:
		word = input("what's the magic number? ")
		if word == "quit":
			return None

		try:
			playerNumber = int(word)
			break
		except ValueError:
			print("only integers between 1 and 10!")
			continue

	return playerNumber

def update(gameStatus, magicNumber, playerNumber):
	if playerNumber is None:
		gameStatus = "end"
	elif playerNumber == magicNumber:
		gameStatus = "win"
	elif magicNumber < playerNumber:
		gameStatus = "lower"
	elif magicNumber > playerNumber:
		gameStatus = "higher"
		
	return gameStatus, magicNumber

def render(gameStatus,magicNumber):
    if gameStatus == "win":
        print("This is correct! You win!")
    elif gameStatus == "end":
        print("Bye!")
    elif gameStatus == "lower":
        print("The magic number is lower")
    elif gameStatus == "higher":
        print("The magic number is higher")
    else:
        raise RuntimeError("Unexpected game status {}".format(gameStatus))

def runGame():
    gameStatus, magicNumber = init()
    while gameStatus != "win" and gameStatus != "end":
        playerNumber = processInput()
        gameStatus, magicNumber = update(gameStatus,magicNumber,playerNumber)
        render(gameStatus,magicNumber)


# Launch the game
runGame()
