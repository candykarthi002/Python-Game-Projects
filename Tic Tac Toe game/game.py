print("Tic Tac Toe Game")

board = []

def init_board():
	for i in range(3):
		row = []
		for j in range(3):
			row.append(' ')
		board.append(row)

init_board()

def change_turn(current_turn):
	if current_turn == 'X':
		return 'O'
	else:
		return 'X'

def draw_board():
	print(' ---   ---   --- ')
	for i, row in enumerate(board):
		for j, e in enumerate(row):
			if j != len(row) - 1:
				print(f"| {e} |", end=' ')
			else:
				print(f"| {e} |")
				print(' ---   ---   --- ')

def get_user_input():
	row = 0
	col = 0
	while row not in ['1', '2', '3'] and col not in ['1', '2', '3']:
		row = input("Select a row from the above board(1/2/3): ")
		if not row.isdigit() or row not in ['1', '2', '3']:
			print("Please select a valid row in range of 1 to 3!!!")
			continue

		col = input("Select a column from the above board(1/2/3): ")
		if not col.isdigit() or col not in ['1', '2', '3']:
			print("Please select a valid column in range of 1 to 3!!!")
			continue

		row = int(row) - 1
		col = int(col) - 1

		if board[row][col] != " ":
			print("Select the empty square only!!!")
			continue
		return row, col

def update_board(row, col, move):
	board[row][col] = move

def row_check(a):
	matched = list(filter(lambda x: x==[a, a, a], board))
	return len(matched) >= 1

def col_check(b):
	new = []
	for i, e in enumerate(board):
		row = []
		for j, k in enumerate(e):
			row.append(board[j][i])
		new.append(row)

	matched = list(filter(lambda x: x==[b, b, b], new))
	return len(matched) >= 1

def diagonal_check(c):
	diagonal = []
	for i in range(3):
		diagonal.append(board[i][i])

	if diagonal == [c, c, c]:
		return True

	rev_board = [x[::-1] for x in board]

	diagonal = []
	for i in range(3):
		diagonal.append(rev_board[i][i])

	if diagonal == [c, c, c]:
		return True

	return False

def validate_board(t):
	check = []
	check.append(row_check(t))
	check.append(col_check(t))
	check.append(diagonal_check(t))
	return any(check)

turns = ['X', 'O']

empty_board = 0

for i in board:
	for j in i:
		if j == " ":
			empty_board += 1

game_over = False

pos = 0

while not game_over:
	draw_board()

	for i in board:
		for j in i:
			if j != " ":
				empty_board -= 1

	if empty_board == 0:
		game_over = True

	r, c = get_user_input()
	update_board(r, c, turns[pos%2])

	player1 = validate_board('X')
	player2 = validate_board('O')

	if player1:
		print("Player X won the match...")
		display_board()
		game_over = True

	if player2:
		print("Player O won the match...")
		display_board()
		game_over = True

	if len(list(filter(lambda x: ' ' in x, board))) == 0:
		print("Match Tied....")
		game_over = True
	pos += 1