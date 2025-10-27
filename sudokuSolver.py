import random
import console
import time

def createBoard():	
	board = [
		
		[5, 3, 0, 0, 7, 0, 0, 0, 0],
		[6, 0, 0, 1, 9, 5, 0, 0, 0],
		[0, 9, 8, 0, 0, 0, 0, 6, 0],
		
		[8, 0, 0, 0, 6, 0, 0, 0, 3],
		[4, 0, 0, 8, 0, 3, 0, 0, 1],
		[7, 0, 0, 0, 2, 0, 0, 0, 6],
		
		[0, 6, 0, 0, 0, 0, 2, 8, 0],
		[0, 0, 0, 4, 1, 9, 0, 0, 5],
		[0, 0, 0, 0, 8, 0, 0, 7, 9],
		
		]
	
	
	
	"""
	
	5 3 0 | 0 7 0 | 0 0 0
	6 0 0 | 1 9 5 | 0 0 0
	0 9 8 | 0 0 0 | 0 6 0
	------+------+------
	8 0 0 | 0 6 0 | 0 0 3
	4 0 0 | 8 0 3 | 0 0 1
	7 0 0 | 0 2 0 | 0 0 6
	------+------+------
	0 6 0 | 0 0 0 | 2 8 0
	0 0 0 | 4 1 9 | 0 0 5
	0 0 0 | 0 8 0 | 0 7 9
	
	"""

	
	return board
	

def makeCustomBoard():
	boardFirst = input("Please enter your board without any spaces or symbols, and 0 for nothing.")
	if len(boardFirst) != 81:
		print("Incorrect board size! Boards must be 9x9.")
		time.sleep(3)
		return None
	try:
		boardTwo = int(boardFirst)
	except:
		print("Your board has symbols or letters in it! ")
		time.sleep(3)
		return None
	board = formatBoard(boardFirst)
	return board
	
def formatBoard(board):
	boardList = []
	boardRow = []
	for i in range(9):
		for j in range(9):
			boardRow.append(board[j])
		boardList.append(boardRow)
	
	return boardList


def printBoard(board):
	console.clear()
	for r in range(9):
		if r % 3 == 0 and r != 0:
			print("-" * 21)
		rowStr = []
		for c in range(9):
			if c % 3 == 0 and c != 0:
				rowStr.append("|")
			val = board[r][c]
			rowStr.append(str(val) if val != 0 else ".")
		print(" ".join(rowStr))
		
	#board → 9×9 list of lists	None	Displays the Sudoku grid neatly with rows, columns, and boxes separated for readability.
	



def findEmpty(board):
	for r in range(9):
		for c in range(9):
			if board[r][c] == 0:
				return r, c
	return None	
	#board	(row, col) tuple if empty cell found; None if full	Finds the coordinates of the next empty cell (value = 0).




def inRow(board, r, val):
	return val in board[r]
	
	#board, r (row index), val (1–9)	True / False	Checks whether the given number already exists in the specified row.


def inCol(board, c, val):
	for r in range(9):
		if board[r][c] == val:
			return True
	return False
	
	#board, c (column index), val	True / False	Checks whether the given number already exists in the specified column.
	
	


def inBox(board, r, c, val):
	boxRow = (r//3)*3
	boxCol = (c//3)*3
	for i in range(3):
		for j in range(3):
			if board[boxRow+i][boxCol+j] == val:
				return True
	return False
	
	#board, r, c, val	True / False	Checks whether the given number already exists in the 3×3 box that contains that cell.




def isValid(board, r, c, val):
	if board[r][c] != 0:
		return False
	if inRow(board, r, val):
		return False
	if inCol(board, c, val):
		return False
	if inBox(board, r, c, val):
		return False
	return True
	
	#board, r, c, val	True / False	Combines the row, column, and box checks to decide if placing a number there is legal.



def solve(board):
	emptyTrue = findEmpty(board)
	if not emptyTrue:
		return True, board
	else:
		r, c = emptyTrue
		for i in range(1, 10):
			if isValid(board, r, c, i):
				board[r][c] = i
				if solve(board):
					return True
				board[r][c] = 0
	return False
		
	
	#board	True if solved, False otherwise	Recursive function that uses backtracking to fill in all empty cells.
	
	
	
customBoard = input("Would you like to make your own board? (y/n)").lower()
if 'y' in customBoard:
	board = makeCustomBoard()
	if not board:
		print("Board does not work!")
		print("Using different board...")
		time.sleep(4)
		board = createBoard()
else:	
	board = createBoard()
printBoard(board)
time.sleep(2)

works = solve(board)
	
if works:
	console.clear()
	print("Final:")
	time.sleep(1)
	printBoard(board)
	
else:
	print("Board unsolvable!")
