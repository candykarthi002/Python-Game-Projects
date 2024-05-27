import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
SQUARE_SIZE = WIDTH//ROWS

BG_COLOR = "black"
SQUARE_COLOR = "white"

NUMBER_FONT = pygame.font.SysFont("comicsans", 20)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder")


def draw_grid():
	for i in range(ROWS):
		for j in range(COLS):
			pygame.draw.rect(WIN, SQUARE_COLOR, (i * SQUARE_SIZE + 1, j * SQUARE_SIZE, SQUARE_SIZE - .25, SQUARE_SIZE - .25))

def draw_numbers():
	for i in range(ROWS):
		for j in range(COLS):
			number = NUMBER_FONT.render(f"{100 - (j * 10 + i)}", True, "black")
			WIN.blit(number, (i * SQUARE_SIZE + (SQUARE_SIZE//2), j * SQUARE_SIZE + (SQUARE_SIZE//2)))

def draw():
	WIN.fill(BG_COLOR)
	draw_grid()
	draw_numbers()
	pygame.draw.rect(WIN, "red", (1, 1, WIDTH - 2, HEIGHT - 2), 2)
	pygame.display.update()

def main():
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
				break
		draw()

	pygame.quit()

if __name__ == '__main__':
	main()