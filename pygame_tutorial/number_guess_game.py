import random

# https://www.patternsgameprog.com/series/discover-python-and-patterns/
# @ end of post 7 "Functions", ready to start post 8 "Game Loop pattern"

def askPlayer():
	while True:
		word = input("what is the magic number? ")
		if word == "quit":
			return None

		try:
			playerNumber = int(word)
			break
		except ValueError:
			print("No decimals! Only integers!")
			continue

	return playerNumber	

def runGame():
	magicNumber = random.randint(1, 10)
	guessCount = 0
	while True:
		playerNumber = askPlayer()
		if playerNumber is None:
			break

		guessCount += 1

		if playerNumber == magicNumber:
			print("you guessed it! congratulations")
			print("you guessed it in {} attempts".format(guessCount))
			break
		elif magicNumber < playerNumber:
			print("...lower...")
		elif magicNumber > playerNumber:
			print("...higher...")

		print("Wrong, guess again!")


def gameMenu():
	while True:
		print("GAME MENU:")
		print("1) New Game")
		print("2) Exit")

		choice = input("Select option: ")
		if choice == "1":
			runGame()
		elif choice == "2":
			break
		else:
			print("Invalid selection. Please type either 1 or 2 and press Enter to choose an option")


gameMenu()