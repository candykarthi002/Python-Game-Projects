import pygame
import random

pygame.init()

WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!!")

all_words =  []
with open("hard_words.txt", "r") as f:
	for feed in f:
		all_words.append(feed.rstrip())

ans = random.choice(all_words)

alphabets = {0: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 1: ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'], 2: ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}

hangman_images = ['']
for i in range(7):
	img = pygame.image.load("images/" + str(i) + ".png")
	hangman_images.append(img)

def draw_lives():
	letter = pygame.font.Font("freesansbold.ttf", 18)
	letter_surf = letter.render(f"Lives Left: {7 - lives_lost}", True, (0, 0, 255))
	letter_rect = letter_surf.get_rect()
	letter_rect.center = (100, 50)
	WIN.blit(letter_surf, letter_rect)

def draw_field():
	for i in range(len(word)):
		pygame.draw.rect(WIN, (0, 0, 0), (WIDTH//4 + (i * 30) - 100, HEIGHT//4 - 25, 25, 25), 5)
		letter = pygame.font.Font("freesansbold.ttf", 18)
		letter_surf = letter.render(new[i], True, (0, 0, 255))
		letter_rect = letter_surf.get_rect()
		letter_rect.center = (WIDTH//4 + (i * 30) - 88, HEIGHT//4 - 12.5)
		WIN.blit(letter_surf, letter_rect)

def draw_alphabet():
	count = 0
	for e, i in enumerate([9, 9, 8]):
		if i == 9:
			for j in range(i):
				circle_x = (j%9) * 100 + 50
				circle_y = HEIGHT//2 + (1 if i%9==0 else 2) * (100 * count)
				pygame.draw.circle(WIN, (0, 0, 0), (circle_x, circle_y), 25, 3)
				letter = pygame.font.Font("freesansbold.ttf", 30)
				letter_surf = letter.render(alphabets[e][j], True, (0, 0, 0))
				letter_rect = letter_surf.get_rect()
				letter_rect.center = (circle_x, circle_y)
				WIN.blit(letter_surf, letter_rect)
			count += 1

		else:
			for j in range(i):
				circle_x = (j%9) * 100 + 100
				circle_y = HEIGHT//2 + (1 if i%9==0 else 2) * 100
				pygame.draw.circle(WIN, (0, 0, 0), (circle_x, circle_y), 25, 3)
				letter = pygame.font.Font("freesansbold.ttf", 30)
				letter_surf = letter.render(alphabets[e][j], True, (0, 0, 0))
				letter_rect = letter_surf.get_rect()
				letter_rect.center = (circle_x, circle_y)
				WIN.blit(letter_surf, letter_rect)

def draw_hangman():
	if hangman_images[lives_lost] != '':
		WIN.blit(pygame.transform.scale(hangman_images[lives_lost], (225, 225)), (WIDTH - WIDTH//4, 0))
	else:
		pass

def draw_window():
	WIN.fill((255, 255, 255))
	draw_lives()
	draw_field()
	draw_alphabet()
	draw_hangman()
	pygame.display.update()

def get_key(e):
	for i in alphabets:
		if e in alphabets[i]:
			return i

def answer_check(given):
	global new, lives_lost
	if given in word:
		n = word.count(given)
		x = word
		for a in range(n):
			for i, e in enumerate(x):
				if e == given:
					ls = list(new)
					del ls[i]
					ls.insert(i, given)
					new = ''.join(ls)
	else:
		if lives_lost <= 7:
			lives_lost += 1
		else:
			lives_lost = 7

def letter_pressed(k):
	key = chr(k).upper()
	for i, l in enumerate(alphabets.values()):
		if key in l:
			answer_check(key)
			s = ''.join(alphabets[i])
			s = s.replace(key, ' ')
			alphabets[i] = list(s)

FPS = 60
clock = pygame.time.Clock()

def game_intro():
	intro = True
	while intro:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					intro = False

		WIN.fill((20, 152, 177))
		LText = pygame.font.Font("freesansbold.ttf", 60)
		LTextSurf = LText.render("Hangman Game", True, (255, 255, 255))
		LTextRect = LTextSurf.get_rect()
		LTextRect.center = (WIDTH//2, HEIGHT//2)
		WIN.blit(LTextSurf, LTextRect)
		MText = pygame.font.Font("freesansbold.ttf", 30)
		MTextSurf = MText.render("Press 'SPACE' to start game!!!", True, (255, 255, 255))
		MTextRect = MTextSurf.get_rect()
		MTextRect.center = (WIDTH//2, HEIGHT//2 + 60)
		WIN.blit(MTextSurf, MTextRect)
		pygame.display.update()

word = ans.upper()
new = " "*len(word)
lives_lost = 0

pygame.mixer.init()

pygame.mixer.music.load("Wasted-MassTamilan.so.mp3")

pygame.mixer.music.set_volume(100.0)

pygame.mixer.music.play(100)

def main():
	global new, lives_lost
	game_over = False
	while not game_over:
		draw_window()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key in range(97, 123):
					letter_pressed(event.key)

		if word == new:
			draw_window()
			return True

		if lives_lost > 7:
			new = word
			lives_lost = 7
			draw_window()
			return False

def game_outro():
	outro = True
	i = 0
	while outro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				outro = False
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					outro = False
					return True

		LText = pygame.font.Font("freesansbold.ttf", 60)
		LTextSurf = LText.render("Hangman Saved!!!", True, (i, 255, 255))
		LTextRect = LTextSurf.get_rect()
		LTextRect.center = (WIDTH//2, HEIGHT//2)
		WIN.blit(LTextSurf, LTextRect)
		MText = pygame.font.Font("freesansbold.ttf", 30)
		MTextSurf = MText.render("(Press SPACE to play again...)", True, (i, 255, 255))
		MTextRect = MTextSurf.get_rect()
		MTextRect.center = (WIDTH//2, HEIGHT//2 + 100)
		WIN.blit(MTextSurf, MTextRect)
		if i < 255:
			i += 1
		else:
			i = 0
		pygame.display.update()

def alter_outro():
	over = True
	i = 0
	while over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				over = False
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					outro = False
					return True

		LText = pygame.font.Font("freesansbold.ttf", 60)
		LTextSurf = LText.render("Game Over!!", True, (i, 0, 0))
		LTextRect = LTextSurf.get_rect()
		LTextRect.center = (WIDTH//2, HEIGHT//2)
		WIN.blit(LTextSurf, LTextRect)
		MText = pygame.font.Font("freesansbold.ttf", 30)
		MTextSurf = MText.render("(Press SPACE to try again...)", True, (i, 0, 0))
		MTextRect = MTextSurf.get_rect()
		MTextRect.center = (WIDTH//2, HEIGHT//2 + 60)
		WIN.blit(MTextSurf, MTextRect)
		if i < 255:
			i += 1
		else:
			i = 0
		pygame.display.update()

def game():
	status = True
	game_intro()
	while status:
		global alphabets, q, ans, word, new, lives_lost
		alphabets = {0: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], 1: ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'], 2: ['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}
		word = ans.upper()
		new = " "*len(word)
		lives_lost = 0
		x = main()
		ans = random.choice(all_words)
		status = game_outro() if x else alter_outro()

game()