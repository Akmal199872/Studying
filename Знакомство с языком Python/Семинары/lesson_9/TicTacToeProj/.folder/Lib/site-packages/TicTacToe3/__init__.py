"""
TTT Package :-
	- Plays the Game
	- Records the Probability of Winning and Drawing
"""

from .__errors__ import ChoiceError as __ChErr
from .__functions__ import commitToGrid as __CTG, comptrMove as __CM
from .__functions__ import gridRepr as __GR, isGameOver as __IGO
from .__functions__ import log as __log, showProb as showProbability
from .__functions__ import updateProb as __UP, uploadProb as __UplP
from tempfile import TemporaryFile as __TF

def play():
	""" Play the Game"""

	# Starting Grid, No. of Moves and tempfile variables
	grid, moves, tmpfile = [
			[None, None, None],
			[None, None, None],
			[None, None, None]
			], 0, __TF("w+t")

	# Title
	print("Tic Tac Toe\n3 in a Row\n")

	# Displaying Starting Grid
	print(__GR(grid))

	# Getting Player's Choice
	playerChoice = input("Choose between 'X' or 'O' :")

	if playerChoice.upper() not in ('X', 'O'):
		raise __ChErr(f"Invalid Choice : '{playerChoice}'")
	else:
		playerChoice = playerChoice.upper()
		tmpfile.write(f"Your Choice : {playerChoice}\n")

	# Setting Computer's Choice based on Player's Choice
	comptrChoice = 'O' if playerChoice == 'X' else "X"

	# Temporarily Logging the choice
	tmpfile.write(f"My Choice : {comptrChoice}\n\n")

	GameOverState, playerMove = __IGO(grid, playerChoice, comptrChoice), True

	# Main Game Starts
	while not bool(GameOverState):

		if playerMove:
			print("\nYour Move")
			tmpfile.write("Your Move\n")

			# Getting Row, Col Value for Player's Move
			row = int(input(f"Enter the Row Number in which you would like to place {playerChoice} : "))

			if row not in (1, 2, 3):
				raise ValueError(f"{row}th Row DOESN'T EXIST")
			else:
				pRow = row - 1

			col = int(input(f"Enter the Column Number in which you would like to place {playerChoice} : "))

			if col not in (1, 2, 3):
				raise ValueError(f"{col}th Column DOESN'T EXIST")
			else:
				pCol = col - 1

			# Commiting Player's Move
			__CTG(grid, pRow, pCol, playerChoice)

			playerMove = False
		else:
			print("\nMy Move")
			tmpfile.write("My Move\n")

			# Making Computer's Move
			cRow, cCol = __CM(grid, playerChoice, comptrChoice)

			playerMove = True

		# Updating Moves
		moves += 1

		# Representing Grid
		print(__GR(grid, moves))

		# Temporarily Logging the Moves
		tmpfile.write(f"{__GR(grid, moves)}\n")

		# Updating GameOverState
		GameOverState = __IGO(grid, playerChoice, comptrChoice)
	else:
		if GameOverState == "comptr":
			print("Hurray!!! I Won.")
			tmpfile.write("Result : I Won!!!\n")
			__UP("comptr")
		elif GameOverState == "draw":
			print("Game Draw!!!")
			tmpfile.write("Result : Draw\n")
			__UP("draw")
		else:
			print("Congratulations!!! You Won.")
			tmpfile.write("Result : You Won!!!\n")
			__UP("player")

		__UplP()

		# Asking for Logging the Output of the game...
		logChoice = input("\nDo You Want to Log the Game (Y/[N]) : ")

		if logChoice.lower() == "y":
			tmpfile.seek(0)
			__log(value=tmpfile.read())
			print(f"Game Logged at {__log(showpath=True)}")
		elif logChoice.lower() == "n":
			tmpfile.close()
		else:
			raise __ChErr(f"Invalid Choice : {logChoice}")

		# Asking for Displaying the Probability
		probChoice = input("\nDo You Want to see the Recorded Probability of Winning (Y/[N]) : ")

		if probChoice.lower() == "y":
			showProbability()
		elif probChoice.lower() == "n":
			exit(0)
		else:
			raise __ChErr(f"Invalid Choice : {probChoice}")