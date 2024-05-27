import pygame
from pygame.locals import *
import numpy as np
import random
import time

print("Snake Game")

pygame.init()

ROWS = COLS = 10
WIDTH, HEIGHT = 600, 600
TILE_SIZE = WIDTH // ROWS
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")


class Board:
    def __init__(self):
        self.board = [[0 for i in range(COLS)] for _ in range(ROWS)]

    def update(self, row, col):
        self.board[row][col] = 1


class Player:
    def __init__(self, board, x=0, y=0):
        self.x = x
        self.y = y
        self.board = board
        self.direction = {'x': 1, 'y': 0}
        self.color = (255, 0, 0)
        self.initialize_board()

    def initialize_board(self):
        self.board.update(self.x, self.y)

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.y * TILE_SIZE,
                                           self.x * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def update(self):
        if self.direction['x'] == 1:
            self.y += 1
        else:
            self.x += 1


b = Board()
player = Player(b)


def draw_window(player=None, fruit=None):
    WIN.fill((255, 255, 255))
    for i, row in enumerate(b.board):
        for j, col in enumerate(row):
            if col == 0:
                pygame.draw.rect(WIN, (0, 0, 0), (j * TILE_SIZE,
                                                  i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
            if col == 1:
                player.draw()
                pygame.draw.rect(WIN, (0, 0, 0), (j * TILE_SIZE,
                                                  i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
            if col == 2:
                # fruit.draw(WIN)
                pygame.draw.rect(WIN, (0, 0, 0), (j * TILE_SIZE,
                                                  i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    pygame.display.update()


game_intro = True

while game_intro:
    # time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    draw_window(player=player)
    player.update()
