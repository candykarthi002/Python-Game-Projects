import pygame
from pygame.locals import *
import random
import numpy as np
from sudoku_solver import validate

pygame.init()
# (20, 152, 177)
WIDTH, HEIGHT = 600, 600
FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, 650))
pygame.display.set_caption("Sudoku game!!")
# fill_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
fill_color = (20, 152, 177)
# print(fill_color)

board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]
main_board = [[0, 3, 4, 0, 7, 8, 0, 1, 0], [6, 0, 2, 1, 9, 0, 0, 4, 8], [1, 9, 0, 0, 4, 2, 0, 0, 0], [0, 5, 9, 0, 6, 0, 4, 2, 0], [4, 0, 6, 0, 5, 0, 0, 0, 0], [7, 1, 0, 9, 2, 4, 0, 0, 6], [0, 6, 0, 5, 3, 0, 2, 8, 0], [2, 0, 0, 4, 1, 9, 0, 3, 0], [3, 4, 0, 2, 8, 0, 1, 0, 0]]
# board = [[0, 3, 4, 0, 7, 8, 0, 1, 0], [6, 0, 2, 1, 9, 0, 0, 4, 8], [1, 9, 0, 0, 4, 2, 0, 0, 0], [0, 5, 9, 0, 6, 0, 4, 2, 0], [4, 0, 6, 0, 5, 0, 0, 0, 0], [7, 1, 0, 9, 2, 4, 0, 0, 6], [0, 6, 0, 5, 3, 0, 2, 8, 0], [2, 0, 0, 4, 1, 9, 0, 3, 0], [3, 4, 0, 2, 8, 0, 1, 0, 0]]

# for i in range(9):
	# board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(np.array(board))

images = {}

for i in range(1, 10):
	images[i] = pygame.transform.scale(pygame.image.load(f"images/{i}.png"), (32, 32))


def draw_grid():
	for i, row in enumerate(board):
		for j, col in enumerate(row):
			pygame.draw.rect(WINDOW, (255, 255, 255), (i * (WIDTH//9 + 1), j * (HEIGHT//9 + 1), (WIDTH//9), (HEIGHT//9)))

def draw_numbers():
	for i, row in enumerate(board):
		for j, col in enumerate(row):
			if col == 0:
				continue
			else:
				WINDOW.blit(images[col], (j * (WIDTH//9 + 1) + 10, i * (HEIGHT//9 + 1) + 10))

def draw_button():
	pygame.draw.rect(WINDOW, (0, 0, 255), (WIDTH//2 - 100, 610, 200, 30))
	text = pygame.font.Font("freesansbold.ttf", 20)
	textSurf = text.render("Check", True, (255, 255, 255))
	textRect = textSurf.get_rect()
	textRect.center = (WIDTH//2, 625)
	WINDOW.blit(textSurf, textRect)

def change_number(row, col):
	board[row][col] = board[row][col] + 1 if board[row][col] < 9 else 0

def handle_click(r, c):
	if main_board[r][c] == 0:
		change_number(r, c)
	else:
		pass

def draw_window():
	WINDOW.fill((0, 0, 0))
	draw_grid()
	draw_numbers()
	draw_button()
	pygame.display.update()

def game():
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = pygame.mouse.get_pos()
				row, col = y//(WIDTH//9), x//(HEIGHT//9)
				if row in range(9) and col in range(9):
					handle_click(row, col)
				else:
					if col in [3, 4, 5]:
						if validate(board):
							game_over = True

		draw_window()

def intro():
	game_intro = True
	while game_intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_intro = False
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game_intro = False

		WINDOW.fill(fill_color)
		Text = pygame.font.Font("freesansbold.ttf", 30)
		TextSurf = Text.render("Press 'SPACE' to start game!!!", True, (255, 255, 255))
		TextRect = TextSurf.get_rect()
		TextRect.center = (WIDTH//2, HEIGHT//2)
		WINDOW.blit(TextSurf, TextRect)
		pygame.display.update()

def outro():
	game_outro = True
	while game_outro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_intro = False
				pygame.quit()
				quit()

		WINDOW.fill(fill_color)
		Text = pygame.font.Font("freesansbold.ttf", 30)
		TextSurf = Text.render("Sudoku Solved!!!", True, (255, 255, 255))
		TextRect = TextSurf.get_rect()
		TextRect.center = (WIDTH//2, HEIGHT//2)
		WINDOW.blit(TextSurf, TextRect)
		pygame.display.update()

def start():
	intro()
	game()
	outro()

start()