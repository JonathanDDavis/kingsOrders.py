#Import random for the Gems function
import time
import random
import sys

# delclare all cariables and arrays
prompt = ">> "
gemsLocation = ""
playerLocation = ""
locations = ["river", "mountain", "cave", "forest"]
inventory = []

def invalidInput():
	delayPrint("\nInvalid Input")

def printInventory(x):
	print("||" + ("-" * 45) + "||")
	delayPrint("\nYou are carrying: " + '%s' % ', '.join(map(str, inventory)))
	print("\n||" + ("-" * 45) + "||")

def delayPrint(x):
	for i in x:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.1)

def gems():
	global gemsLocation
	gemsLocation = random.choice(locations).lower()

# asking player for there name
delayPrint("\nWhat is your name")
name = input(prompt)
delayPrint("\nIt is nice to meet you " + name)
ready = False

# asking the player if they are ready
while ready == False:
	delayPrint("\nAre you ready to play?")
	choice = input(prompt)
	if choice.lower() == "yes":
		delayPrint("\nOkay we will start")
		ready = True
	elif choice.lower() == "no":
		delayPrint("\nJust tell me when you are ready")
		ready == False
	else:
		invalidInput()

newGame = True
while newGame == True:

# moves the gems around randomly
	gems()

# begining of game
# comment the next line out in the final verison
	#print("\n" + gemsLocation)
	delayPrint("\n" + name + ": The king summoned you and want you to go look for the royal gems that someone has stolen. He said that you have to go to the north, south, east, or west.")

	validInput = False
	while validInput == False:
		delayPrint("\nPlease pick a location: River, Forest, Mountain, Cave.")
		playerChoice = input(prompt).lower()
		playerLocation = playerChoice
		if playerChoice == "forest":
			delayPrint("\nYou walk into the forest.")
			if playerLocation == gemsLocation:
				delayPrint("\nYou found the gems.")
				delayPrint("\nWould you like to pick them up?")
				getGems = False
				while getGems == False:
					playerChoice = input(prompt).lower()
					if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get gems":
						inventory.append("Gems")
						printInventory(inventory)
						getGems = True
						ValidInput = True
					elif playerChoice == "No" or playerChoice =="n":
						delayPrint("\nOkay then. If you change your mind, just type 'GET GEMS'.")
					else:
						invalidInput()
			else:
				delayPrint("\nSorry, the gems weren't there!")
		elif playerChoice == "cave":
			delayPrint("\nYou walk into the cave.")
			if playerLocation == gemsLocation:
				delayPrint("\nYou found the gems.")
				delayPrint("\nWould you like to pick them up?")
				getGems = False
				while getGems == False:
					playerChoice = input(prompt).lower()
					if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get gems":
						inventory.append("Gems")
						printInventory(inventory)
						getGems = True
						ValidInput = True
					elif playerChoice == "No" or playerChoice =="n":
						delayPrint("\nOkay then. If you change your mind, just type 'GET GEMS'.")
					else:
						invalidInput()
			else:
				delayPrint("\nSorry, the gems weren't there!")
		elif playerChoice == "river":
			delayPrint("\nYou walk into the river. ")
			if playerLocation == gemsLocation:
				delayPrint("\nYou found the gems.")
				delayPrint("\nWould you like to pick them up?")
				getGems = False
				while getGems == False:
					playerChoice = input(prompt).lower()
					if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get gems":
						inventory.append("Gems")
						printInventory(inventory)
						getGems = True
						ValidInput = True
					elif playerChoice == "No" or playerChoice =="n":
						delayPrint("\nOkay then. If you change your mind, just type 'GET GEMS'.")
					else:
						invalidInput()
			else:
				delayPrint("\nSorry, the gems weren't there!")
		elif playerChoice == "mountain":
			delayPrint("\nYou walk into the mountain.")
			if playerLocation == gemsLocation:
				delayPrint("\nYou found the gems.")
				delayPrint("\nWould you like to pick them up?")
				getGems = False
				while getGems == False:
					playerChoice = input(prompt).lower()
					if playerChoice == "yes" or playerChoice == "y" or playerChoice =="get gems":
						inventory.append("Gems")
						printInventory(inventory)
						getGems = True
						ValidInput = True
					elif playerChoice == "No" or playerChoice =="n":
						delayPrint("\nOkay then. If you change your mind, just type 'GET GEMS'.")
					else:
						invalidInput()
			else:
				delayPrint("\nSorry, the gems weren't there!")
	delayPrint("\nYou returned to the castle and gave the gems back to the king")
	delayPrint("\nWould you want to play again")
	playerResponse = input(prompt)
	if playerResponse == "yes":
		delayPrint("\nFanstastic!")
	elif playerResponse == "no":
		delayPrint("\nWhat a shame, See you next time.")
		newGame = False
	else:
		invalidInput()
		response = input(prompt).lower()
delayPrint("\nThanks for playing")
