from datetime import date as __dt, datetime as __dtime
from .__errors__ import CommitError as __CErr
from github import Github as __G
from itertools import permutations as __perm
from json import load as __load, dumps as __dumps
from os import remove as __rem, mkdir as __md
from os.path import abspath as __abs, exists as __exs
from pathlib import Path as __p
from random import shuffle as __shuf
from socket import gethostbyname as __GHN, create_connection as __CC, gaierror as __GE

# Can a Trio Occur in the Grid
def __canTrioOccur(grid, value):
	rows = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
	cols = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
	diags = [(1, 5, 9), (3, 5, 7)]
	coorDict = {1:(0, 0), 2:(0, 1), 3:(0, 2),
					4:(1, 0), 5:(1, 1), 6:(1, 2),
					7:(2, 0), 8:(2, 1), 9:(2, 2)}
	resCoors = []

	# Checking if a trio can be formed in any of the rows
	for row in rows:
		checkRows = [i for i in __perm(row, 2)]

		for Rows in checkRows:
			pos1, pos2 = coorDict[Rows[0]], coorDict[Rows[1]]

			if (grid[pos1[0]][pos1[1]] == value) and (grid[pos2[0]][pos2[1]] == value):

				for i in row:
					if (i != Rows[0]) and (i != Rows[1]):
						checkPos = coorDict[i]

						if grid[checkPos[0]][checkPos[1]] is None:
							resCoors.append(i)
							break

	# Checking if a trio can be formed in any of the columns
	for col in cols:
		checkCols = [i for i in __perm(col, 2)]

		for Cols in checkCols:
			pos1, pos2 = coorDict[Cols[0]], coorDict[Cols[1]]

			if (grid[pos1[0]][pos1[1]] == value) and (grid[pos2[0]][pos2[1]] == value):

				for i in col:
					if (i != Cols[0]) and (i != Cols[1]):
						checkPos = coorDict[i]

						if grid[checkPos[0]][checkPos[1]] is None:
							resCoors.append(i)
							break

	# Checking if a trio can be formed in any of the diagonals
	for diag in diags:
		checkDiags = [i for i in __perm(diag, 2)]

		for Diags in checkDiags:
			pos1, pos2 = coorDict[Diags[0]], coorDict[Diags[1]]

			if (grid[pos1[0]][pos1[1]] == value) and (grid[pos2[0]][pos2[1]] == value):

				for i in diag:
					if (i != Diags[0]) and (i != Diags[1]):
						checkPos = coorDict[i]

						if grid[checkPos[0]][checkPos[1]] is None:
							resCoors.append(i)
							break
	return resCoors

# Commiting to Grid
def commitToGrid(grid, row, col, value):
	if grid[row][col] is None:
		grid[row][col] = value
	else:
		raise __CErr(f"Move can't be commited as some value is already present at the location.")

# Computer's Move
def comptrMove(grid, playerChoice, comptrChoice):
	coorDict = {1:(0, 0), 2:(0, 1), 3:(0, 2),
					4:(1, 0), 5:(1, 1), 6:(1, 2),
					7:(2, 0), 8:(2, 1), 9:(2, 2)}
	comprRes = __canTrioOccur(grid, comptrChoice)
	playerRes = __canTrioOccur(grid, playerChoice)

	if any(comprRes):
		row, col = coorDict[comprRes[0]]

		# Commiting Computer's Move
		commitToGrid(grid, row, col, comptrChoice)

		return (row, col)
	elif any(playerRes):
		row, col = coorDict[playerRes[0]]

		# Commiting Computer's Move
		commitToGrid(grid, row, col, comptrChoice)

		return (row, col)
	else:
		availPos = [i for i in __isNotFilled(grid)]
		__shuf(availPos)
		row, col = availPos[0]

		# Commiting Computer's Move
		commitToGrid(grid, row, col, comptrChoice)

		return (row, col)

# Grid Representation
def gridRepr(grid, moves=None):
	result = ""

	for flatSplits in range(13):
		result += "-"

	result += f"\t\tMoves Commited : {moves}\n"

	for rows in grid:
		result += "| "

		for colVal in rows:
			if colVal is None:
				result += "  | "
			else:
				result += f"{colVal} | "

		result += "\n"

		for flatSplits in range(13):
			result += "-"

		result += "\n"

	return result

# Function to Check if all the Value in the Grid is Filled i.e No more Moves can be commited
def __isAllFilled(grid):
	for rows in grid:
		for colVal in rows:
			if colVal is None:
				return False
	else:
		return True

# Function to Check if all the Value in the Grid is None i.e No Move has been commited
def __isAllNone(grid):
	for rows in grid:
		for colVal in rows:
			if colVal is not None:
				return False
	else:
		return True

# Checking of Game Over State
def isGameOver(grid, playerChoice, comptrChoice):
	if __isAllNone(grid):
		return False
	else:
		# Checking for a trio in a row
		for i in range(3):
			row = grid[i]

			if row.count(comptrChoice) == 3:
				return "comptr"
			elif row.count(playerChoice) == 3:
				return "player"
		else:

			# Checking for a trio in a column
			for i in range(3):
				col = []

				for j in range(3):
					col.append(grid[j][i])

				if col.count(comptrChoice) == 3:
					return "comptr"
				elif col.count(playerChoice) == 3:
					return "player"
			else:

				# Checking for a trio in the Main Diagonal
				mainDiag = []

				for i in range(3):
					for j in range(3):
						if i == j:
							mainDiag.append(grid[i][j])

					if mainDiag.count(comptrChoice) == 3:
						return "comptr"
					elif mainDiag.count(playerChoice) == 3:
						return "player"
				else:

					# Checking for a trio in the Secondary Diagonal
					secDiag = []

					for i in range(3):
						for j in range(3):
							if i+j == 2:
								secDiag.append(grid[i][j])

						if secDiag.count(comptrChoice) == 3:
							return "comptr"
						elif secDiag.count(playerChoice) == 3:
							return "player"
					else:

						# Checking for a DRAW
						if __isAllFilled(grid):
							return "draw"
						else:
							return False

# Function to check if any place is not filled
def __isNotFilled(grid):
	for i in range(3):
		for j in range(3):
			if grid[i][j] is None:
				yield (i, j)

def log(value=None, showpath=False):
	if not __exs(f"{__p.home()}/Python TicTacToe3 Logs"):
		__md(f"{__p.home()}/Python TicTacToe3 Logs")

	filename = f"{__p.home()}/Python TicTacToe3 Logs/Tic Tac Toe {__dt.today()}.log"

	if showpath:
		return __abs(filename)
	else:
		time = __dtime.now().strftime("%H:%M:%S")

		if __exs(filename):
			file = open(filename, "a")
			data = f"\n\nNew Match played at {time}\n"

			file.write(data + "-"*len(data) + f"\n{value}")
			file.close()
		else:
			file = open(filename, "w")
			data = f"New Match played at {time}\n"

			file.write(data + "-"*len(data) + f"\n{value}")
			file.close()

# Displaying the Probability
def showProb():
	""" Displays the Probability recorded so far"""

	fileprob = f"{__abs('.')}/prob.json"

	try:
		file1 = open(fileprob)
	except FileNotFoundError:
		with open(fileprob, "w") as file:
			newData = {"Total Games Played": 0,
						"Total Computer Wins": 0,
						"Total Player Wins": 0,
						"Total Draws": 0,
						"Computer Winning Probability": 0,
						"Player Winning Probability": 0,
						"Game Drawing Probability": 0}
			file.write(__dumps(newData, indent=4))

		file1 = open(f)

	data = __load(file1)

	compProb = round(data["Computer Winning Probability"]*100, 2)
	playerProb = round(data["Player Winning Probability"]*100, 2)
	drawProb = round(data["Game Drawing Probability"]*100, 2)

	data["Computer Winning Probability"] = f"{compProb}%"
	data["Player Winning Probability"] = f"{playerProb}%"
	data["Game Drawing Probability"] = f"{drawProb}%"

	print()
	print(__dumps(data, indent=4))

# Updating the Probability
def updateProb(win=None):
	fileprob = f"{__abs('.')}/prob.json"
	fileLocal = f"{__abs('.')}/.local.json"

	if __exs(fileprob):
		file1 = open(fileprob)
	else:
		with open(fileprob, "w") as file:
			newData = {"Total Games Played": 0,
						"Total Computer Wins": 0,
						"Total Player Wins": 0,
						"Total Draws": 0,
						"Computer Winning Probability": 0,
						"Player Winning Probability": 0,
						"Game Drawing Probability": 0}
			file.write(__dumps(newData, indent=4))

	if __exs(fileLocal):
		with open(fileLocal) as RFile:
			LData = __load(RFile)
	else:
		with open(fileLocal, "w") as WFile:
			newData = {"Total Games Played": 0,
						"Total Computer Wins": 0,
						"Total Player Wins": 0,
						"Total Draws": 0,
						"Computer Winning Probability": 0,
						"Player Winning Probability": 0,
						"Game Drawing Probability": 0}
			WFile.write(__dumps(newData, indent=4))

	file1, RFile = open(fileprob), open(fileLocal)
	data, LData = __load(file1), __load(RFile)

	data["Total Games Played"] += 1
	LData["Total Games Played"] += 1

	if win == "comptr":
		data["Total Computer Wins"] += 1
		LData["Total Computer Wins"] += 1
	elif win == "player":
		data["Total Player Wins"] += 1
		LData["Total Player Wins"] += 1
	else:
		data["Total Draws"] += 1
		LData["Total Draws"] += 1

	data["Computer Winning Probability"] = round(data["Total Computer Wins"]/data["Total Games Played"], 2)
	LData["Computer Winning Probability"] = round(LData["Total Computer Wins"]/LData["Total Games Played"], 2)

	data["Player Winning Probability"] = round(data["Total Player Wins"]/data["Total Games Played"], 2)
	LData["Player Winning Probability"] = round(LData["Total Player Wins"]/LData["Total Games Played"], 2)

	data["Game Drawing Probability"] = round(data["Total Draws"]/data["Total Games Played"], 2)
	LData["Game Drawing Probability"] = round(LData["Total Draws"]/LData["Total Games Played"], 2)

	with open(fileprob, "w") as file2:
		file2.write(__dumps(data, indent=4))

	with open(fileLocal, "w") as WFile1:
		WFile1.write(__dumps(LData, indent=4))

def uploadProb():
	fileLocal = f"{__abs('.')}/.local.json"

	try:
		host = __GHN("1.1.1.1")
		s = __CC((host, 80), 2)
		s.close()

		print("Please Wait a While")

		GitClient = __G("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")
		LData = __load(open(fileLocal))

		repo = GitClient.get_user().get_repo("TicTacToe3-cli")

		file = repo.get_contents("prob.json")
		SContent = file.decoded_content.decode()

		with open(f"{__abs('.')}/new.json", "w") as WFile:
			WFile.write(SContent)

		with open(f"{__abs('.')}/new.json") as RFile:
			data = __load(RFile)

		data["Total Games Played"] += LData["Total Games Played"]
		data["Total Computer Wins"] += LData["Total Computer Wins"]
		data["Total Player Wins"] += LData["Total Player Wins"]
		data["Total Draws"] += LData["Total Draws"]

		data["Computer Winning Probability"] = round(data["Total Computer Wins"]/data["Total Games Played"], 2)

		data["Player Winning Probability"] = round(data["Total Player Wins"]/data["Total Games Played"], 2)

		data["Game Drawing Probability"] = round(data["Total Draws"]/data["Total Games Played"], 2)

		SData = __dumps(data, indent=4)

		repo.update_file(path = "prob.json",
						message = "Updated Probability Stats",
						content = SData,
						sha = file.sha)

		__rem(f"{__abs('.')}/new.json")
		__rem(fileLocal)
	except (__GE, OSError) as exception:
		pass