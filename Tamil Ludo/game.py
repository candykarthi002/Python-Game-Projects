import pygame
import random
import numpy as np
import time

pygame.init()

FPS = 1000
WIDTH, HEIGHT = 700, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dhayam")

game_over = False

class Player:
	def __init__(self, name, turn):
		self.name = name
		self.got_one = False
		self.turn = turn
		self.starting_pieces = []
		self.on_board_pieces = []
		self.valid_board = []
		if self.turn:
			self.valid_board = [
			[[], [], [], [], [], [], [], -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1], 
			[[], 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, []], 
			[0, -1, -1, -1, -1, [], 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, [], [], [], -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, [], -1, [], -1, 0, -1, -1, -1, -1, -1, 0], 
			[[], -1, [], -1, [], [], [], -1, -1, -1, -1, -1, []], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[[], 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, []]]
			self.valid_moves = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 5), (6, 4), (6, 3), (6, 2), (6, 1), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (18, 1), (18, 2), (18, 3), (18, 4), (18, 5), (18, 6), (18, 7), (18, 8), (18, 9), (18, 10), (18, 11), (18, 12), (17, 12), (16, 12), (15, 12), (14, 12), (13, 12), (12, 12), (11, 12), (10, 12), (9, 12), (8, 12), (7, 12), (6, 12), (6, 11), (6, 10), (6, 9), (6, 8), (6, 7), (7, 5), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (12, 5), (12, 4), (11, 4), (10, 4), (10, 3), (10, 2), (11, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2)]
		else:
			self.valid_board = [[-1, -1, -1, -1, -1, -1, [], [], [], [], [], [], []],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1], 
			[[], 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, []], 
			[0, -1, -1, -1, -1, -1, 0, [], -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, [], [], [], -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, [], -1, [], -1, 0], 
			[[], -1, -1, -1, -1, -1, [], [], [], -1, [], -1, []], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[[], 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, []]]
			self.valid_moves = [(0, 12), (0, 11), (0, 10), (0, 9), (0, 8), (0, 7), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (6, 7), (6, 8), (6, 9),(6, 10), (6, 11), (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (13, 12), (14, 12), (15, 12), (16, 12), (17, 12), (18, 12), (18, 11), (18, 10), (18, 9), (18, 8), (18, 7), (18, 6), (18, 5), (18, 4), (18, 3), (18, 2), (18, 1), (18, 0), (17, 0), (16, 0), (15, 0), (14, 0), (13, 0), (12, 0), (11, 0), (10, 0), (9, 0), (8, 0), (7, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (7, 7), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (12, 7), (12, 8), (11, 8), (10, 8), (10, 9), (10, 10), (11, 10), (12, 10),(13, 10), (14, 10), (15, 10), (16, 10)]

	def change_turn(self):
		self.turn = False if self.turn else True

class Board:
	def __init__(self):
		self.board = [[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
		[-1, -1, 2, 2, 2, -1, 0, -1, 3, 3, 3, -1, -1],
		[-1, -1, 2, 2, 2, -1, 0, -1, 3, 3, 3, -1, -1],
		['b1', -1, 2, 2, 2, -1, 0, -1, 3, 3, 3, -1, 'b2'],
		[-1, -1, 2, 2, 2, -1, 0, -1, 3, 3, 3, -1, -1],
		[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1], 
		[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1], 
		[0, -1, -1, -1, -1, 1, 0, 1, -1, -1, -1, -1, 0], 
		[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
		[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
		[0, -1, 1, 0, 0, -1, 0, -1, 0, 0, 1, -1, 0], 
		[0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0, -1, 0], 
		[1, -1, 0, -1, 0, 0, 1, 0, 0, -1, 0, -1, 1], 
		[0, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0], 
		[0, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0], 
		[0, -1, 0, -1, -1, -1, -1, -1, -1, -1, 0, -1, 0], 
		[0, -1, 1, -1, -1, -1, "d1", "d2", -1, -1, 1, -1, 0], 
		[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
		[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]]
		self.valid_board = [[[], [], [], [], [], [], [], [], [], [], [], [], []],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1],
			[-1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1], 
			    [[], 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, []], 
			[0, -1, -1, -1, -1, [], 0, [], -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1, -1, 0], 
			[0, -1, [], [], [], -1, 0 , -1, [], [], [], -1, 0], 
			[0, -1, [], -1, [], -1, 0 , -1, [], -1, [], -1, 0], 
		   [[], -1, [], -1, [], [], [], [], [], -1, [], -1, []], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, [], -1, -1, -1, -1, -1, -1, -1, [], -1, 0], 
			[0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0], 
			[[], 0, 0, 0, 0, 0, [], 0, 0, 0, 0, 0, []]]

	def draw(self, surf):
		for i, row in enumerate(self.board):
			for j, sq in enumerate(row):
				is_mount = False
				if sq == 0:
					color = (255, 255, 255)
				elif sq == -1:
				 	color = (1, 1, 1)
				elif sq == 1:
				 	color = (0, 255, 0)
				 	is_mount = True
				else:
				 	pass
				pygame.draw.rect(surf, color, (j * (WIDTH//13 + 1), i * (HEIGHT//19 + 1), (WIDTH//13), (HEIGHT//19)))
				if is_mount:
					pygame.draw.line(surf, (0, 0, 0), (j * (WIDTH//13 + 1), i * (HEIGHT//19 + 1)), (j * (WIDTH//13 + 1) + (WIDTH//13), i * (HEIGHT//19 + 1) + (HEIGHT//19)), 2)
					pygame.draw.line(surf, (0, 0, 0), (j * (WIDTH//13 + 1) + (WIDTH//13), i * (HEIGHT//19 + 1)), (j * (WIDTH//13 + 1), i * (HEIGHT//19 + 1) + (HEIGHT//19)), 2)


class Piece:
	def __init__(self, pos, color, row, col):
		self.pos = pos
		self.color = color
		self.row, self.col = row, col
		self.sq_row, self.sq_col = row, col
		self.at_starting = True
		self.at_end = False

	def draw(self, surf):
		pygame.draw.rect(surf, (128, 128, 128), (self.sq_col * (WIDTH//13 + 1), self.sq_row * (HEIGHT//19 + 2) + 16, (WIDTH//13), (HEIGHT//19)))
		if (self.row == 0 and self.col == 0) or (self.row == 0 and self.col == 12) or self.at_starting:
			pygame.draw.circle(surf, self.color, (self.col * (WIDTH//13 + 1) + ((self.pos - 1)%6 * 4 if not self.at_starting else 0) + ((WIDTH//13 - 24) if self.at_starting else (WIDTH//52)), self.row * (HEIGHT//19 + 3) + (32 if self.at_starting else (HEIGHT//38 * ((self.pos - 1)//6) + 9))), 16)
			pygame.draw.circle(surf, (0, 0, 0), (self.col * (WIDTH//13 + 1) + ((self.pos - 1)%6 * 4 if not self.at_starting else 0) + ((WIDTH//13 - 24) if self.at_starting else (WIDTH//52)), self.row * (HEIGHT//19 + 3)+ (32 if self.at_starting else (HEIGHT//38 * ((self.pos - 1)//6) + 9))), 16, 2)

		else:
			pygame.draw.circle(surf, self.color, (self.col * (WIDTH//13 + 1) + ((WIDTH//13 - 24) if self.at_starting else (WIDTH//26)), self.row * (HEIGHT//19 + 1) + (HEIGHT//38)), 16)
			pygame.draw.circle(surf, (0, 0, 0), (self.col * (WIDTH//13 + 1) + ((WIDTH//13 - 24) if self.at_starting else (WIDTH//26)), self.row * (HEIGHT//19 + 1) + (HEIGHT//38)), 16, 2)

		# piece_img = pygame.transform.scale(pygame.image.load(f"./{self.name}_piece.png"), ((WIDTH//13), (HEIGHT//19)))
		# surf.blit(piece_img, (self.col * (WIDTH//13 + 1), self.row * (HEIGHT//19 + 2) + 16))

	def move(self, new_row, new_col):
		self.row, self.col = new_row, new_col
		self.at_starting = False

	def __str__(self):
		return f"A Piece at row {self.row} and column {self.col}."

	def __repr__(self):
		return f"A Piece at row {self.row} and column {self.col}."

class Dice:
	def __init__(self):
		self.faces = [0, 1, 2, 3]
		self.current_face = 0
		self.sound = pygame.mixer.Sound('COIN.wav')

	def roll(self):
		return random.choice(self.faces)

	def draw(self, surf, board, row, col):
		img_width, img_height = (WIDTH//13), (HEIGHT//19 * 3)
		img = pygame.transform.scale(pygame.image.load(f"./{self.faces[self.current_face]}.png"), (img_width, img_height))
		img_x = col * (WIDTH//13 + 1) - 20
		img_y = row * (HEIGHT//19) - 75
		# pygame.draw.rect(surf, (255, 255, 255), (img_x, img_y, img_width, img_height))
		surf.blit(img, (img_x, img_y))

class Button:
	def __init__(self, turn):
		self.color = (0, 0, 255)
		self.is_enabled = turn

	def draw(self, surf, row, col):
		if self.is_enabled:
			pygame.draw.rect(surf, self.color, (col * (WIDTH//13) + 5, row * (HEIGHT//19), (WIDTH//13), (HEIGHT//19) * 2))
			if ludo_board.board[row][col] == 'b1':
				btn_img = pygame.transform.scale(pygame.image.load('./btn1.png'), ((WIDTH//13), (HEIGHT//19) * 2))
			else:
				btn_img = pygame.transform.scale(pygame.image.load('./btn2.png'), ((WIDTH//13), (HEIGHT//19) * 2))
			surf.blit(btn_img, (col * (WIDTH//13) + 5, row * (HEIGHT//19)))
		else:
			pygame.draw.rect(surf, (128, 128, 128), (col * (WIDTH//13) + 5, row * (HEIGHT//19), (WIDTH//13), (HEIGHT//19) * 2))

def draw_dice(board):
	for i, row in enumerate(board):
		for j, e in enumerate(row):
			if e == "d1":
				# pygame.draw.rect(WIN, (255, 255, 255), ((j * (WIDTH//13 + 1) - 20, i * (HEIGHT//19) - 75, (WIDTH//13), (HEIGHT//19 * 3))))
				dice1.draw(WIN, board, i, j)
			if e == "d2":
				# pygame.draw.rect(WIN, (255, 255, 255), ((j * (WIDTH//13 + 1) - 20, i * (HEIGHT//19) - 75, (WIDTH//13), (HEIGHT//19 * 3))))
				dice2.draw(WIN, board, i, j)

def draw_button(board):
	for i, row in enumerate(board):
		for j, e in enumerate(row):
			if e == "b1":
				button1.draw(WIN, i, j)
			if e == "b2":
				button2.draw(WIN, i, j)

def draw_game():
	WIN.fill((0, 0, 0))
	ludo_board.draw(WIN)
	for piece in pieces:
		piece.draw(WIN)
		# print(piece)
	draw_dice(ludo_board.board)
	draw_button(ludo_board.board)
	pygame.display.update()

player1 = Player("Karthik", True)
player2 = Player("Akash", False)

ludo_board = Board()

dice1 = Dice()
dice2 = Dice()

button1 = Button(player1.turn)
button2 = Button(player2.turn)

intro_bg = pygame.transform.scale(pygame.image.load("./Wallpaper.png"), (WIDTH, HEIGHT))

pieces = []

player1_pos = 0
player2_pos = 0
for i, row in enumerate(ludo_board.board):
	for j, e in enumerate(row):
		if e == 2:
			player1_pos += 1
			pc = Piece(player1_pos, (255, 255, 0), i, j)
			player1.starting_pieces.append(pc)
			pieces.append(pc)

		if e == 3:
			player2_pos += 1
			pc = Piece(player2_pos, (0, 255, 255), i, j)
			player2.starting_pieces.append(pc)
			pieces.append(pc)

clock = pygame.time.Clock()

def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				intro = False

		WIN.blit(intro_bg, (0, 0))
		font = pygame.font.SysFont("Comic Sans MS", 60)
		textSurf = font.render("Dhayam", True, (255, 255, 245))
		textRect = textSurf.get_rect()
		textRect.center = (WIDTH//2, HEIGHT//2)
		WIN.blit(textSurf, textRect)
		pygame.display.update()

def game():
	while not game_over:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				button_pressed = True
				while button_pressed:
					x, y = pygame.mouse.get_pos()
					print(f"Row -> {y//(WIDTH//19)} Column -> {x//(HEIGHT//13)}.")
					if player1.turn:
						if x in range(5, 60):
							if y in range(108, 179):
								dice1.current_face = dice1.roll()
								dice2.current_face = dice2.roll()
								dice1.sound.play()
								print(dice1.current_face)
								print(dice2.current_face)
								drawn_value = dice1.current_face + dice2.current_face
								if not dice1.current_face and not dice2.current_face:
									drawn_value = 12
								print(drawn_value)
								if drawn_value == 1 and not player1.got_one:
									player1.got_one = True
									new_piece = player1.starting_pieces.pop(0)
									player1.on_board_pieces.append(new_piece)
									print(player1.valid_board[0][0])
									player1.valid_board[0][0].append(new_piece)
									print(player1.valid_board[0][0])
									new_piece.move(0, 0)
									draw_game()
									break

								if player1.got_one:
									if (drawn_value == 1 or drawn_value == 5) and len(player1.starting_pieces) >= 1:
										new_piece = player1.starting_pieces.pop(0)
										player1.on_board_pieces.append(new_piece)
										player1.valid_board[0][0].append(new_piece)
										print(player1.valid_board[0][0])
										new_piece.move(0, 0)
										draw_game()
										break

									if drawn_value not in [2, 3, 4]:
										draw_game()
										move_making = True

										while move_making:
											for event in pygame.event.get():
												if event.type == pygame.MOUSEBUTTONDOWN:
													x, y = pygame.mouse.get_pos()
													row, col = y//(WIDTH//19), x//(HEIGHT//13)
													# print(row, col)
											
													if type(player1.valid_board[row][col]) == type([]):
														if len(player1.valid_board[row][col]) > 0:
															drawn_piece = player1.valid_board[row][col].pop(0)
															print(player1.valid_board[row][col])
															chosen_row, chosen_col = row, col
															move_making = False
														else:
															continue

													elif player1.valid_board[row][col] not in [0, -1] and not type(player1.valid_board[row][col]) == type([]):
														drawn_piece, player1.valid_board[row][col] = player1.valid_board[row][col], 0
														chosen_row, chosen_col = row, col
														move_making = False

													else:
														pass

										print(drawn_piece)
										print(np.array(player1.valid_board))
										for i, e in enumerate(player1.valid_moves):
											if e == (chosen_row, chosen_col):
												current_sq = i
										dest_sq = player1.valid_moves[current_sq + drawn_value]

										if type(player1.valid_board[dest_sq[0]][dest_sq[1]]) == type([]):
											player1.valid_board[dest_sq[0]][dest_sq[1]].append(drawn_piece)
											drawn_piece.move(dest_sq[0], dest_sq[1])

										else:
											player1.valid_board[dest_sq[0]][dest_sq[1]] = drawn_piece
											drawn_piece.move(dest_sq[0], dest_sq[1])

										draw_game()
										print(drawn_value)
										break

									else:
										draw_game()
										move_making = True

										while move_making:
											for event in pygame.event.get():
												if event.type == pygame.MOUSEBUTTONDOWN:
													x, y = pygame.mouse.get_pos()
													row, col = y//(WIDTH//19), x//(HEIGHT//13)
													print(player1.valid_board[row][col])
													# print(row, col)
											
													if type(player1.valid_board[row][col]) == type([]):
														if len(player1.valid_board[row][col]) > 0:
															drawn_piece = player1.valid_board[row][col].pop(0)
															print(player1.valid_board[row][col])
															chosen_row, chosen_col = row, col
															move_making = False
														else:
															continue

													elif player1.valid_board[row][col] not in [0, -1] and not type(player1.valid_board[row][col]) == type([]):
														drawn_piece, player1.valid_board[row][col] = player1.valid_board[row][col], 0
														chosen_row, chosen_col = row, col
														print(chosen_row, chosen_col)
														move_making = False

													else:
														pass

										print(drawn_piece)

										for i, e in enumerate(player1.valid_moves):
											if e == (chosen_row, chosen_col):
												print(e)
												current_sq = i
												break

										if current_sq == len(player1.valid_moves) - 1:
											drawn_piece.at_end = True


										if len(player1.valid_moves) - (current_sq + drawn_value) > 0: 
											dest_sq = player1.valid_moves[current_sq + drawn_value]
											if type(player1.valid_board[dest_sq[0]][dest_sq[1]]) == type([]):
												player1.valid_board[dest_sq[0]][dest_sq[1]].append(drawn_piece)
												drawn_piece.move(dest_sq[0], dest_sq[1])

											else:
												player1.valid_board[dest_sq[0]][dest_sq[1]] = drawn_piece
												drawn_piece.move(dest_sq[0], dest_sq[1])

										draw_game()
										print(drawn_value)

										player1.change_turn()
										player2.change_turn()
										button1.is_enabled = False
										button2.is_enabled = True
										button_pressed = False
										break

								else:
									player1.change_turn()
									player2.change_turn()
									button1.is_enabled = False
									button2.is_enabled = True
									button_pressed = False
							else:
								button_pressed = False
						else:
							button_pressed = False

					elif player2.turn:
						if x in range(641, 695):
							if y in range(108, 179):
								dice1.current_face = dice1.roll()
								dice2.current_face = dice2.roll()
								dice1.sound.play()

								print(dice1.current_face)
								print(dice2.current_face)
								if not dice1.current_face and not dice2.current_face:
									drawn_value = 12
								else:
									drawn_value = dice1.current_face + dice2.current_face
								print(drawn_value)
								if drawn_value == 1 and not player2.got_one:
									player2.got_one = True
									new_piece = player2.starting_pieces.pop(0)
									player2.on_board_pieces.append(new_piece)
									player2.valid_board[0][12].append(new_piece)
									new_piece.move(0, 12)
									draw_game()
									break

								if player2.got_one:
									if (drawn_value == 1 or drawn_value == 5) and len(player2.starting_pieces) >= 1:
										new_piece = player2.starting_pieces.pop(0)
										player2.on_board_pieces.append(new_piece)
										player2.valid_board[0][12].append(new_piece)
										new_piece.move(0, 12)
										draw_game()
										break

									if drawn_value not in [2, 3, 4]:
										draw_game()
										move_making = True

										while move_making:
											for event in pygame.event.get():
												if event.type == pygame.MOUSEBUTTONDOWN:
													x, y = pygame.mouse.get_pos()
													row, col = y//(WIDTH//19), x//(HEIGHT//13)
													# print(row, col)
											
													if type(player2.valid_board[row][col]) == type([]):
														if len(player2.valid_board[row][col]) > 0:
															drawn_piece = player2.valid_board[row][col].pop(0)
															print(player2.valid_board[row][col])
															chosen_row, chosen_col = row, col
															move_making = False
														else:
															continue

													elif player2.valid_board[row][col] not in [0, -1] and not type(player2.valid_board[row][col]) == type([]):
														drawn_piece, player2.valid_board[row][col] = player2.valid_board[row][col], 0
														chosen_row, chosen_col = row, col
														move_making = False

													else:
														pass

										print(drawn_piece)
										print(np.array(player2.valid_board))
										for i, e in enumerate(player2.valid_moves):
											if e == (chosen_row, chosen_col):
												current_sq = i
										dest_sq = player2.valid_moves[current_sq + drawn_value]

										if type(player2.valid_board[dest_sq[0]][dest_sq[1]]) == type([]):
											player2.valid_board[dest_sq[0]][dest_sq[1]].append(drawn_piece)
											drawn_piece.move(dest_sq[0], dest_sq[1])

										else:
											player2.valid_board[dest_sq[0]][dest_sq[1]] = drawn_piece
											drawn_piece.move(dest_sq[0], dest_sq[1])

										draw_game()
										print(drawn_value)
										break

									else:
										draw_game()
										move_making = True

										while move_making:
											for event in pygame.event.get():
												if event.type == pygame.MOUSEBUTTONDOWN:
													x, y = pygame.mouse.get_pos()
													row, col = y//(WIDTH//19), x//(HEIGHT//13)
													print(player2.valid_board[row][col])
													# print(row, col)
											
													if type(player2.valid_board[row][col]) == type([]):
														if len(player2.valid_board[row][col]) > 0:
															drawn_piece = player2.valid_board[row][col].pop(0)
															print(player2.valid_board[row][col])
															chosen_row, chosen_col = row, col
															move_making = False
														else:
															continue

													elif player2.valid_board[row][col] not in [0, -1] and not type(player2.valid_board[row][col]) == type([]):
														drawn_piece, player2.valid_board[row][col] = player2.valid_board[row][col], 0
														chosen_row, chosen_col = row, col
														print(chosen_row, chosen_col)
														move_making = False

													else:
														pass

										print(drawn_piece)

										for i, e in enumerate(player2.valid_moves):
											if e == (chosen_row, chosen_col):
												print(e)
												current_sq = i
												break

										if current_sq == len(player2.valid_moves) - 1:
											drawn_piece.at_end = True


										if len(player2.valid_moves) - (current_sq + drawn_value) > 0: 
											dest_sq = player2.valid_moves[current_sq + drawn_value]
											if type(player2.valid_board[dest_sq[0]][dest_sq[1]]) == type([]):
												player2.valid_board[dest_sq[0]][dest_sq[1]].append(drawn_piece)
												drawn_piece.move(dest_sq[0], dest_sq[1])

											else:
												player2.valid_board[dest_sq[0]][dest_sq[1]] = drawn_piece
												drawn_piece.move(dest_sq[0], dest_sq[1])

										draw_game()
										print(drawn_value)

										player1.change_turn()
										player2.change_turn()
										button1.is_enabled = True
										button2.is_enabled = False
										button_pressed = False

								else:
									player1.change_turn()
									player2.change_turn()
									button1.is_enabled = True
									button2.is_enabled = False
									button_pressed = False

							else:
								button_pressed = False

						else:
							button_pressed = False

					else:
						button_pressed = False

		draw_game()

def main():
	game_intro()
	game()

if __name__ == '__main__':
	main()