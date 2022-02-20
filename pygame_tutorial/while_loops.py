repeat = True

while True:
	while repeat:
		word = input("enter the magic word: ")
		if word == "please":
			print("you win!")
			break
		elif word == "quit":
			repeat  = False
			print("HA! HA! I beat you!")
			break
		else:
			print("ah, ah, ah... try again...")
			break
	word = input("type 'again' to retry: ")
	if word != "again":
		break
print("thanks for playing!")