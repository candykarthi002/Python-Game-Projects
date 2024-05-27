import pygame
from pygame.locals import *
import random


pygame.init()

fps = 60
width, height = (500, 500)
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bingo!")
number_imgs = dict()
crossed_number_imgs = dict()
board = []
crossed_numbers = []
result = ['B', 'I', 'N', 'G', 'O']
r = random.randint(1, 255)
b = random.randint(1, 255)
g = random.randint(1, 255)

clock = pygame.time.Clock()

def on_start():
	global bingo_matched, crossed_numbers, board
	for i in range(1, 26):
		number_imgs[i] = pygame.image.load('numbers/' + str(i) + '.png')

	for i in range(1, 26):
		crossed_number_imgs[i] = pygame.image.load('numbers/crossed_' + str(i) + '.png')

	board = []
	crossed_numbers = []
	bingo_matched = Matched()
	# print(bingo_matched)


def draw_board():
	for i in range(5):
		for j in range(6):
			pygame.draw.rect(WIN, (255, 255, 255), (i * 101, j * 101, width//5, height//5))

def number_generator():
	numbers = list(range(1, 26))
	for i in range(5):
		row = []
		for j in range(5):
			num = random.choice(numbers)
			row.append(num)
			numbers.remove(num)
		board.append(row)

	return board

def Matched():
	match_board = []
	for i in range(5):
		r = []
		for j in range(5):
			r.append(1)
		match_board.append(r)
	return match_board

def draw_window():
	WIN.fill((255, 0, 0))
	draw_board()
	draw_numbers()
	pygame.display.update()

# print(*number_generator(), sep='\n')

def draw_numbers():
	for e, i in enumerate(board):
		for f, j in enumerate(i):
			WIN.blit(pygame.transform.scale(number_imgs[j], (100, 100)), (e * 101, f * 101))

def change_numbers(num):
	number_imgs[num] = crossed_number_imgs[num]

def cross_number(row, col):
	global bingo_matched
	for i in range(5):
		for j in range(5):
			if (row == j and col == i) and board[i][j] not in crossed_numbers:
				crossed_numbers.append(board[i][j])
				bingo_matched[j][i] = 0
				change_numbers(board[i][j])
	# print(*bingo_matched, sep='\n')
	if is_bingo_matched():
		n = is_bingo_matched()
		# print(n)
		if n < 5:
			match = ''.join(result[:n])
			# print(match)
			return match

		else:
			return ''.join(result)

def traverse_horizontal():
	h_count = 0
	for i, row in enumerate(bingo_matched):
		temp_count = 0
		for j, col in enumerate(row):
			if col == 0:
				temp_count += 1
		if temp_count == 5:
			h_count += 1

	# print("Horizontally crossed => ", h_count)
	return h_count

def traverse_vertical():
	v_count = 0
	for i, row in enumerate(bingo_matched):
		temp_count = 0
		for j, col in enumerate(row):
			if bingo_matched[j][i] == 0:
				temp_count += 1

		if temp_count == 5:
			v_count += 1

	# print("Vertically crossed => ", v_count)
	return v_count

def traverse_diagonal():
	d_count = 0
	temp_count = 0
	for i, row in enumerate(bingo_matched):
		if bingo_matched[i][i] == 0:
			temp_count += 1

	if temp_count == 5:
		d_count += 1

	temp_count = 0
	for j, k in enumerate(bingo_matched):
		if bingo_matched[j][len(k) - (j + 1)] == 0:
			temp_count += 1
	if temp_count == 5:
		d_count += 1

	# print("Diagonally crossed => ", d_count)
	return d_count

def is_bingo_matched():
	count = 0
	count += traverse_horizontal()
	count += traverse_vertical()
	count += traverse_diagonal()
	
	return count

bingo_matched = Matched()

def text_objects(text, font, color):
	textSurf = font.render(text, True, color)
	return textSurf, textSurf.get_rect()

def game_intro():
	intro = True
	while intro:
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		WIN.fill((r, g, b))
		LargeText = pygame.font.Font("freesansbold.ttf", 75)
		TextSurface, TextRect = text_objects("Bingo Game!", LargeText, (255, 0, 0))
		TextRect.center = ((width/2, height/2))
		WIN.blit(TextSurface, TextRect)
		MediumText = pygame.font.Font("freesansbold.ttf", 30)
		MTextSurf, MTextRect = text_objects("(Press \"SPACE\" to start...)", MediumText, (255, 255, 255))
		MTextRect.center = ((width/2, height/2 + 60))
		WIN.blit(MTextSurf, MTextRect)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			intro = False
			on_start()
			number_generator()

		pygame.display.update()

def main():
	game_over = False
	while not game_over:
		draw_window()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				# print(pos)
				x, y = pos[0]//100, pos[1]//100
				matches = cross_number(y, x)

				if matches == "BINGO":
					# print("BINGO matched!!")
					game_over = True
					break

def game_outro():
	play_again = "no"
	outro = True
	while outro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				outro = False
				pygame.quit()
				quit()

		WIN.fill((r, g, b))
		LargeText = pygame.font.Font("freesansbold.ttf", 60)
		TextSurface, TextRect = text_objects("Bingo Matched!!", LargeText, (0, 255, 255))
		TextRect.center = ((width/2, height/2))
		WIN.blit(TextSurface, TextRect)
		MediumText = pygame.font.Font("freesansbold.ttf", 30)
		MTextSurf, MTextRect = text_objects("(Press SPACE to play again...)", MediumText, (255, 255, 255))
		MTextRect.center = ((width/2, height/2 + 50))
		WIN.blit(MTextSurf, MTextRect)

		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:
			outro = False
			play_again = "yes"

		pygame.display.update()

	return play_again

start = "yes"
while start == "yes":
	game_intro()
	main()
	start = game_outro()

quit()