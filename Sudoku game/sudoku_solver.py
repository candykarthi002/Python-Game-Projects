import random
# import numpy as np

# sudoku_board = []

# for r in range(9):
# 	digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 	row = []
# 	for c in range(9):
# 		elem = random.choice(digits)
# 		row.append(elem)
# 		digits.remove(elem)
# 	sudoku_board.append(row)

# print(sudoku_board, sep='\n')

# To check the board
 # -> By checking the respective row.
 # -> By checking the respective column.
 # -> By checking the corresponding box.

# sudoku_board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# print(np.array(sudoku_board))

# is_valid_board = False

def row_check(b):
	checked = []
	for row in b:
		if len(list(set(row))) == 9 and 0 not in row:
			checked.append(True)
		else:
			checked.append(False)
	return all(checked)

def col_check(b):
	checked = []
	for i, j in enumerate(b):
		r = []
		for k, l in enumerate(j):
			r.append(b[k][i])
		if len(list(set(r))) == 9 and 0 not in r:
			checked.append(True)
		else:
			checked.append(False)
	return all(checked)

def checking(row, col, b):
	box = []
	for i in range((row * 3), (row * 3) + 3):
		for j in range((col * 3), (col * 3) + 3):
			box.append(b[i][j])
	return len(set(box)) == 9 and 0 not in box

def box_check(b):
	boxes = []
	for i in range(3):
		for j in range(3):
			boxes.append(checking(i, j, b))
	return all(boxes)

def validate(board):
	validation = []
	validation.append(row_check(board))
	validation.append(col_check(board))
	validation.append(box_check(board))
	print(validation)
	return all(validation)

# is_valid_board = validate()
# print(is_valid_board)