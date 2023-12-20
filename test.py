# import sys module
import pygame
import sys


# pygame.init() will initialize all
# imported module
pygame.init()

clock = pygame.time.Clock()

# it will display on screen
screen = pygame.display.set_mode([600, 500])

inputBoxWidth = 60
inputBoxHeight = 50

dx = 10
dy = 10
rects = [pygame.Rect(10 + i * (dx + inputBoxWidth), 10 + j * (dy + inputBoxHeight), inputBoxWidth, inputBoxHeight) for i in range(3) for j in range(8)]
active = [False for i in rects]
texts = ['' for i in rects]

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive

def printInputBox(rect,active,text):
	if (active):
		pygame.draw.rect(screen, pygame.Color('lightskyblue3'), rect)
	else:
		pygame.draw.rect(screen, pygame.Color('chartreuse4'), rect)

	mainText = pygame.font.Font('fonts/verdana.ttf', 25)
	text = mainText.render(text, True, (255, 255, 255))
	screen.blit(text, rect)

while True:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			print(texts)
			for i, r in enumerate(rects):
				active[i] = r.collidepoint(event.pos)

		if event.type == pygame.KEYDOWN:
			for i, t in enumerate(texts):
				if (active[i]):
					if event.key == pygame.K_BACKSPACE:
						texts[i] = t[:-1]
					else:
						texts[i] += event.unicode
	
	# it will set background color of screen
	screen.fill((255, 255, 255))

	for i, rect in enumerate(rects):
		printInputBox(rect, active[i], texts[i])
		
	
	pygame.display.update()
	clock.tick(60)
