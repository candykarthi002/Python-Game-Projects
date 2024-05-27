import pygame
import random
import numpy as np

pygame.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Candy crush mini saga")

game_over = False

#"🍬", "🍭", "🍫",

# fruits = [ "🥕", "🍎", "🍇", "🍊", "🍍", "🍒"]
fruits = ["red", "orange", "blue", "green", "yellow", "violet"]
fruits_index = [i for i in range(0, 6)]

class Board:
	def __init__(self):
		self.board = [[[random.randint(0, 5), 0] for i in range(9)] for _ in range(9)]
		self.selected_fruits = []
		self.red_fruits_pos = []
		self.orange_fruits_pos = []
		self.blue_fruits_pos = []
		self.green_fruits_pos = []
		self.yellow_fruits_pos = []
		self.violet_fruits_pos = []

	def __repr__(self):
		return str(np.array(self.board))

	def _remove_all_selected(self):
		for i in range(9):
			for j in range(9):
				self.board[i][j][1] = 0

	def _filter_fruit_pos(self):
		self.red_fruits_pos = []
		self.orange_fruits_pos = []
		self.blue_fruits_pos = []
		self.green_fruits_pos = []
		self.yellow_fruits_pos = []
		self.violet_fruits_pos = []
		for i, row in enumerate(self.board):
			for j, col in enumerate(row):
				if col[0] == 0:
					self.red_fruits_pos.append([j, i])
				elif col[0] == 1:
					self.orange_fruits_pos.append([j, i])
				elif col[0] == 2:
					self.blue_fruits_pos.append([j, i])
				elif col[0] == 3:
					self.green_fruits_pos.append([j, i])
				elif col[0] == 4:
					self.yellow_fruits_pos.append([j, i])
				elif col[0] == 5:
					self.violet_fruits_pos.append([j, i])
				else:
					pass

		return {"red": self.red_fruits_pos, "orange": self.orange_fruits_pos, "blue": self.blue_fruits_pos, "green": self.green_fruits_pos, "yellow": self.yellow_fruits_pos, "violet": self.violet_fruits_pos}

	def change_matched_fruits(self):
		changed = False
		for f, pos in self._filter_fruit_pos().items():
				row = []
				for x in pos:
					for j in range(0, 10):
						if x[0] == j:
							row.append(x)

				print(row)
				if len(row) >= 3:
					for p, i in enumerate(row):
						# print(pos, i)
						# print(row[pos + 1])
						if i[1] < 6 and len(row[p:]) >= 3:
							if i[1] + 1 == row[p + 1][1] and i[1] + 2 == row[p + 2][1]:
								# print(i, row[pos+1], row[pos+2])
								print(f"Matched!!! :) {f} -> {row}")
								next_fruits = fruits_index.copy()
								next_fruits.pop(self.board[i[0]][i[1]][0])
								# random.shuffle(next_fruits)
								for n in range(0, 3):
									print(f"Next Fruits: {next_fruits}")
									fruit = random.choice(next_fruits)
									print(f"{self.board[i[0]][i[1]][0]} -> {fruit}")
									self.board[i[0]][i[1] + n] = [fruit, 0]
									changed = True

				else:
					print(f"{f} -> {row}")

				col = []
				for x in pos:
					for j in range(0, 10):
						if x[1] == j:
							col.append(x)

				if len(col) >= 3:
					for pos, i in enumerate(col):
						# print(pos, i)
						# print(col[pos + 1])
						if i[1] < 6 and len(col[pos:]) >= 3:
							if i[1] + 1 == col[pos + 1][1] and i[1] + 2 == col[pos + 2][1]:
								# print(i, col[pos+1], col[pos+2])
								print(f"Matched!!! :) {f} -> {col}")
								next_fruits = fruits_index.copy()
								next_fruits.pop(self.board[i[0]][i[1]][0])
								# random.shuffle(next_fruits)
								for n in range(0, 3):
									print(f"Next Fruits: {next_fruits}")
									fruit = random.choice(next_fruits)
									print(f"{self.board[i[0]][i[1]][0]} -> {fruit}")
									self.board[i[0]][i[1] + n] = [fruit, 0]
									changed = True

				else:
					print(f"{f} -> {col}")

		# if changed:
		# 	self.change_matched_fruits()

	def select_fruit(self, x, y):
		# self.selected_fruits.append(self.board[x][y])
		# if len(self.selected_fruits) <= 1:
		# 	self.board[x][y][1] = 1
		# else:
		# 	for i in range(len(self.selected_fruits) - 1):
		# 		self.board[self.selected_fruits[0][0]][self.selected_fruits[0][1]][1] = 0
		# 		del self.selected_fruits[0]
		# 	self.board[x][y][1] = 1

		if len(self.selected_fruits) > 0:
			if self.selected_fruits[0][1] == y and (self.selected_fruits[0][0] + 1 == x or self.selected_fruits[0][0] - 1 == x):
				print(x, y)
				self.board[self.selected_fruits[0][0]][self.selected_fruits[0][1]], self.board[x][y] = self.board[x][y], self.board[self.selected_fruits[0][0]][self.selected_fruits[0][1]]

			elif self.selected_fruits[0][0] == x and (self.selected_fruits[0][1] + 1 == y or self.selected_fruits[0][1] - 1 == y):
				print(x, y)
				self.board[self.selected_fruits[0][0]][self.selected_fruits[0][1]], self.board[x][y] = self.board[x][y], self.board[self.selected_fruits[0][0]][self.selected_fruits[0][1]]

			else:
				print("Invalid swap!!!")

			self.change_matched_fruits()
			self.selected_fruits = []
			self._remove_all_selected()
		else:
			self._remove_all_selected()
			self.board[x][y][1] = 1
			self.selected_fruits.append([x, y])

		# for k, v in self._filter_fruit_pos().items():
		# 	print(f"{k} -> {v}", end="\n")

def draw_grid():
	for i in range(9):
		for j in range(9):
			pygame.draw.rect(WIN, (255, 255, 255), (i * (WIDTH//9 + 1), j * (HEIGHT//9 + 1), WIDTH//9 - 1, HEIGHT//9 - 1))

def draw_fruits(b):
	for i, r in enumerate(b.board):
		for j, e in enumerate(r):
			if e[1] == 1:
				pygame.draw.rect(WIN, (0, 0, 128), (i * (WIDTH//9 + 1), j * (HEIGHT//9 + 1), WIDTH//9 - 1, HEIGHT//9 - 1))
			pygame.draw.circle(WIN, fruits[e[0]], (i * (WIDTH//9 + 1) + (WIDTH//18), j * (HEIGHT//9 + 1) + (HEIGHT//18)), 20)
			# fnt = pygame.font.SysFont("comicsans", 20)
			# fruit = fnt.render(fruits[e], True, (0, 0, 0))

def draw_window(b):
	WIN.fill((0, 255, 255))
	draw_grid()
	draw_fruits(b)
	pygame.display.update()

b = Board()
# print(b)

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True

		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			x, y = pos[0]//(WIDTH//9), pos[1]//(HEIGHT//9)
			# print(x, y)
			if x < 9 and y < 9:
				b.select_fruit(x, y)
				print(b.selected_fruits)
			
	draw_window(b)

pygame.quit()