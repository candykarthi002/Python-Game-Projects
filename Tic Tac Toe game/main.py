import pygame

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Tic Tac Toe game!!")


class Board():
	def __init__(self):
		self.board = self.init_board()

	def init_board(self):
		board = []
		for i in range(3):
			row = []
			for j in range(3):
				row.append(' ')
			board.append(row)
		return board

	def draw_markers(self):
		for i, e in enumerate(self.board):
			for j, f in enumerate(e):
				if f == ' ':
					pass
				else:
					marker = pygame.font.SysFont("Comic Sans MS", 100)
					markerSurf = marker.render(f.upper(), True, (0, 0, 0))
					markerRect = markerSurf.get_rect()
					markerRect.center = (i * (WIDTH//3 + 1) + WIDTH//6), (j * (HEIGHT//3 + 1) + HEIGHT//6)
					WIN.blit(markerSurf, markerRect)

	def update(self, row, col, marker):
		if self.board[row][col] == " ":
			self.board[row][col] = marker
		else:
			pass

	def row_check(self, r):
		matched = list(filter(lambda x: x==[r, r, r], self.board))
		return len(matched) >= 1

	def col_check(self, c):
		new = []
		for i, e in enumerate(self.board):
			row = []
			for j, k in enumerate(e):
				row.append(self.board[j][i])
			new.append(row)

		matched = list(filter(lambda x: x==[c, c, c], new))
		return len(matched) >= 1

	def diagonal_check(self, d):
		diagonal = []
		for i in range(3):
			diagonal.append(self.board[i][i])

		if diagonal == [d, d, d]:
			return True

		rev_board = [x[::-1] for x in self.board]

		diagonal = []
		for i in range(3):
			diagonal.append(rev_board[i][i])

		return diagonal == [d, d, d]

	def validate_board(self, marker):
		check = []
		check.append(self.row_check(marker))
		check.append(self.col_check(marker))
		check.append(self.diagonal_check(marker))
		return any(check)


def draw_board(board):
	for i, e in enumerate(board):
		for j, f in enumerate(e):
			pygame.draw.rect(WIN, (255, 255, 255), (i * (WIDTH//3 + 1), j * (HEIGHT//3 + 1), WIDTH//3, HEIGHT//3))

def draw_game():
	WIN.fill((0, 0, 0))
	draw_board(bo.board)
	bo.draw_markers()
	pygame.display.update()

def update_empty_squares(board):
	empty = 9
	for i in board:
		for j in i:
			if j != " ":
				empty -= 1
	return empty

bo = Board()

turns = ['X', 'O']

pos = 0

empty_squares = 9

def main():
	global empty_squares, pos
	game_over = False
	while not game_over:
		draw_game()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				row, col = x//(WIDTH//3), y//(HEIGHT//3)
				if row in [0, 1, 2] and col in [0, 1, 2] and bo.board[row][col] == " ":
					mark = pos % 2
					bo.update(row, col, turns[mark])
					draw_game()
					empty_squares = update_empty_squares(bo.board)
					pos += 1
				else:
					pass

		for t in turns:
			if bo.validate_board(t):
				res = f"Player {t} won the match"
				game_over = True
				return res

		if empty_squares == 0:
			res = "Match tie!!!"
			game_over = True
			return res

def intro():
	game_intro =  True
	while game_intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_intro = True
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				game_intro = False

		WIN.fill((255, 255, 0))
		intro_text = pygame.font.SysFont("Comic Sans MS", 50)
		textSurf = intro_text.render("Tic Tac Toe game!!", True, (0, 0, 0))
		textRect = textSurf.get_rect()
		textRect.center = WIDTH//2, HEIGHT//2
		WIN.blit(textSurf, textRect)
		pygame.display.update()

def outro(text):
	game_outro =  True
	while game_outro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_outro = True
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				game_outro = False

		WIN.fill((255, 255, 0))
		outro_text = pygame.font.SysFont("Comic Sans MS", 40)
		textSurf = outro_text.render(text, True, (255, 0, 0))
		textRect = textSurf.get_rect()
		textRect.center = WIDTH//2, HEIGHT//2
		WIN.blit(textSurf, textRect)
		pygame.display.update()

	return True

def restart_board():
	global empty_squares, pos, bo
	pos = 0
	empty_squares = 9
	bo = Board()

def game():
	intro()
	playing = True
	while playing:
		result = main()
		playing = outro(result)
		restart_board()

if __name__ == "__main__":
	game()