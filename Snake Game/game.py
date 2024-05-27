import pygame
from pygame.locals import *
import numpy as np
import random
import time



ground = [[0 for i in range(30)] for _ in range(30)]

print(np.array(ground))

class Fruit:
	def __init__(self, row, col):
		print("New fruit!!!")
		self.row = row
		self.col = col
		self.color = (255, 0, 0)

	def draw(self, surf):
		pygame.draw.rect(surf, self.color, (self.row * 20, self.col * 20, 20, 20))

class Player:
	def __init__(self, x, y):
		print("Player created")
		self.x = x
		self.y = y
		self.score = 0
		self.width = 20
		self.height = 20
		self.direction = "r"
		self.color = (0, 255, 0)
		self.body = [[0, 0]]
		self.length = len(self.body)

	def draw(self, sur):
		for i, seg in enumerate(self.body):
			pygame.draw.rect(sur, self.color, (self.x - (seg[0] * 20), self.y - (seg[1] * 20), self.width, self.height))

	def movement(self):
		new_body = []
		for i in range(len(self.body)):
			if i == 0:
				new_body.append(self.body[i])
			else:
				new_body.append([self.body[i][0] - (1 if self.direction == "r" else 0) , self.body[i][1] - (1 if self.direction == "u" else 0)])

		return new_body

	def move(self):
		if self.direction == "u":
			if self.y > 0:
				self.y -= 20
				pygame.time.delay(50)
			else:
				self.direction = 'r' if self.x > 0 else 'l'

		if self.direction == "d":
			if self.y < 580:
				self.y += 20
				pygame.time.delay(50)
			else:
				self.direction = 'r' if self.x > 0 else 'l'

		if self.direction == "r":
			if self.x > 0:
				self.x += 20
				pygame.time.delay(50)
			else:
				self.direction = 'u' if self.y > 0 else 'd'

		if self.direction == 'l':
			if self.x < 580:
				self.x -= 20
				pygame.time.delay(50)
			else:
				self.direction = 'u' if self.y > 0 else 'd'

		self.body = self.movement()

def intro():
	game_intro = True

	while game_intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.MOUSEBUTTONUP:
				game_intro = False

		WIN.fill((0, 255, 255))
		text = pygame.font.SysFont("Comic Sans MS", 60)
		textSurf = text.render("Snake Game", True, (0, 0, 0))
		textRect = textSurf.get_rect()
		textRect.center = (WIDTH//2, HEIGHT//2)
		WIN.blit(textSurf, textRect)
		pygame.display.update()

def draw_window(player, fruit):
	WIN.fill((255, 255, 255))
	for i, row in enumerate(ground):
		for j, col in enumerate(row):
			if col == 0:
				pygame.draw.rect(WIN, (0, 0, 0), (j *20, i * 20, 20, 20), 1)
			if col == 1:
				player.draw(WIN)
				pygame.draw.rect(WIN, (0, 0, 0), (j *20, i * 20, 20, 20), 1)
			if col == 2:
				fruit.draw(WIN)
				pygame.draw.rect(WIN, (0, 0, 0), (j *20, i * 20, 20, 20), 1)
	pygame.display.update()

def check_boundary(x, y):
	if x > 0 and x < 580:
		if y > 0 and y < 580:
			return True
	return False


def is_ate(player_pos, fruit_pos):
	if player_pos[0] == fruit_pos[0] and player_pos[1] == fruit_pos[1]:
		return True
	return False

def game():
	game_over = False
	p_x = random.randint(5, 25)
	p_y = random.randint(5, 25)
	player = Player(p_x * 20, p_y * 20)
	print(p_x, p_y)
	ground[p_y][p_x] = 1

	f_x = random.randint(1, 28)
	f_y = random.randint(1, 28)
	fruit = Fruit(f_x, f_y)
	print(f_x, f_y)
	ground[f_y][f_x] = 2
	print(np.array(ground))
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP] and player.direction != "d":
			player.direction = "u"

		if keys[pygame.K_DOWN] and player.direction != "u":
			player.direction = "d"

		if keys[pygame.K_LEFT] and player.direction != "r":
			player.direction = "l"

		if keys[pygame.K_RIGHT] and player.direction != "l":
			player.direction = "r"


		if not check_boundary(player.x, player.y):
			game_over = True

		if is_ate((player.x//20, player.y//20), (fruit.row, fruit.col)):
			print(fruit.row, fruit.col)
			ground[fruit.row][fruit.col] = 0
			player.score += 1
			player.body.append([1 if player.direction == "r" else 0, 1 if player.direction == "u" else 0])
			fruit.row, fruit.col = random.randint(1, 28), random.randint(1, 28)
			ground[fruit.col][fruit.row] = 2

		draw_window(player, fruit)
		player.move()

def outro():
	game_outro = True

	retry = False
	while game_outro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					retry = True
					game_outro = False

		text = pygame.font.SysFont("Comic Sans MS", 60)
		textSurf = text.render("Game Over", True, (255, 0, 0))
		textRect = textSurf.get_rect()
		textRect.center = (WIDTH//2, HEIGHT//2)
		WIN.blit(textSurf, textRect)
		pygame.display.update()
	return retry

def main():
	playing = True
	intro()
	time.sleep(1)
	while playing:
		game()
		playing = outro()
		ground = [[0 for i in range(30)] for _ in range(30)]

if __name__ == '__main__':
	main()