import random
import console
import time

def createBoard():
	#num = int(input("Please enter a number from 1 to 9. "))
	#board = [[[num, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, num], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, num, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, num, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [num, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, num]]]
	
	
	
	board = [
		
		[5, 3, 0, "|",  0, 7, 0, "|",  0, 0, 0],
		[6, 0, 0, "|",  1, 9, 5, "|",  0, 0, 0],
		[0, 9, 8, "|",  0, 0, 0, "|",  0, 6, 0, "\n------+-------+------"],
		[8, 0, 0, "|",  0, 6, 0, "|",  0, 0, 3],
		[4, 0, 0, "|",  8, 0, 3, "|",  0, 0, 1],
		[7, 0, 0, "|",  0, 2, 0, "|",  0, 0, 6, "\n------+-------+------"],
		[0, 6, 0, "|",  0, 0, 0, "|",  2, 8, 0],
		[0, 0, 0, "|",  4, 1, 9, "|",  0, 0, 5],
		[0, 0, 0, "|",  0, 8, 0, "|",  0, 7, 9],
		
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
		
	"""
	5  3  1  |  9  7  4  |  8  0  0 

	6  7  4  |  1  9  5  |  0  0  0 

	0  9  8  |  0  0  7  |  3  6  0  

	----------+-----------+---------- 

 8  0  0  |  5  6  0  |  1  0  3 

 4  5  9  |  8  0  3  |  7  0  1 

 7  0  5  |  3  2  0  |  4  0  6  

----------+-----------+------------ 

 3  6  0  |  7  0  0  |  2  8  0 

 0  8  0  |  4  1  9  |  6  0  5 

 1  0  3  |  0  8  2  |  0  7  9
 """
	
	
	return board
	

def printBoard(board):
	console.clear()
	for i in range(9//len(board)):
		for part in board:
			parts = ''
			for row in part:
				parts += f"{str(row)} "
			print(parts)
		
	#board → 9×9 list of lists	None	Displays the Sudoku grid neatly with rows, columns, and boxes separated for readability.
	



def findEmpty(board):
	thing = 'hi'
	row = random.randint(0, 8)
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
			
	#board	(row, col) tuple if empty cell found; None if full	Finds the coordinates of the next empty cell (value = 0).




def inRow(board, r, val):
	if val in board[r]:
		return True
	return False
	
	#board, r (row index), val (1–9)	True / False	Checks whether the given number already exists in the specified row.




def inCol(board, c, val):
	for row in board:
		for i in range(len(row)):
			if i == c:
				if row[i] == val:
					return True
	return False
	
	#board, c (column index), val	True / False	Checks whether the given number already exists in the specified column.
	
	


def inBox(board, r, c, val):
	return False
	
	#board, r, c, val	True / False	Checks whether the given number already exists in the 3×3 box that contains that cell.




def isValid(board, r, c, val):
	if inRow(board, r, val):
		return False
	if inCol(board, c, val):
		return False
	if inBox(board, r, c, val):
		return False
	else:
		return True
	
	#board, r, c, val	True / False	Combines the row, column, and box checks to decide if placing a number there is legal.



def solve(board, action):
	if findEmpty(board):
		action.append(board)
	try:
		board = solve(board, action)
		return board
	except:
		return board
	
	#board	True if solved, False otherwise	Recursive function that uses backtracking to fill in all empty cells.
	
	
	
	
	
board = createBoard()
printBoard(board)

action = []
boardSolved = solve(board, action)
time.sleep(4)
console.clear()
print("Final:")
time.sleep(1)
printBoard(boardSolved)
