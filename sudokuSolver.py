import random
import console
import time

def createBoard():
	#num = int(input("Please enter a number from 1 to 9. "))
	#board = [[[num, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, num], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, num, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, num, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [num, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, num]]]
	
	
	
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
	"""	row = random.randint(0, 8)
	col = random.randint(0, 8)
	val = random.randint(1, 9)
	#print("Start")
	#print(row)
	#print(col)
	if board[row][col] == 0:
		if isValid(board, row, col, val):
			#print("True")
			#time.sleep(1)
			board[row][col] = val
			#printBoard(board)
			return True
	return False
	"""
	
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
	
	
	
	
	
board = createBoard()
printBoard(board)

works = solve(board)

if works:
	time.sleep(4)
	console.clear()
	print("Final:")
	time.sleep(1)
	printBoard(board)

else:
	print("Board unsolvable!")
