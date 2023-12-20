import sys
import arabic_reshaper
import random as rd
import pygame as pg
import colors as cl
from bidi.algorithm import get_display

clock = pg.time.Clock()
currentRoundTime = 0
previousRoundTime = 0

score = 0
totalTime = 0

nButtons = 5
l = 100
gap = 0
p = 0

def main():
    global mouse, currentRoundTime

    mouse = pg.mouse.get_pos()

    for event in pg.event.get():
        if (event.type == pg.QUIT): sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
    
            for i in range(nButtons):
                x = p[0] + i * (gap + l)
                y = p[1]
            
                if (x <= mouse[0] <= x + l and y <= mouse[1] <= y + l):
                    checkResult(i)
                    nextRound()

    screen.fill((100,100,100))

    printScore()
    printTimer()
    printButtons()
    msg = cl.names[currentLanguage][currentRound1]
    size = 200 - 10 * (len(msg) - 4)
    printText(msg, cl.languages[currentLanguage], width // 2, height // 2, cl.colorList[currentRound2], size)

    currentRoundTime = pg.time.get_ticks() - previousRoundTime
    clock.tick(60)

    pg.display.update()

def printText(msg, lng, x, y, color, size):

    if (lng == 'hindi'):
        font = 'fonts/mangal.ttf'
    elif (lng == 'chinese' or lng == 'japanese'):
        font = 'fonts/heiti.otf'
    elif (lng == 'arabic'):
        font = 'fonts/suighub.ttf'
        msg = get_display(arabic_reshaper.reshape(msg[::-1]))
    else:
        font = 'fonts/verdana.ttf'

    mainText = pg.font.Font(font, size)
    text = mainText.render(msg, True, color)
    textRect = text.get_rect(center = (x, y))
    screen.blit(text, textRect)

def nextRound():
    global currentRound1, currentRound2, currentLanguage, previousRoundTime, totalTime

    totalTime += currentRoundTime
    previousRoundTime = pg.time.get_ticks()

    currentRound1 = rd.randint(0,9)
    currentRound2 = rd.randint(0,9)
    currentLanguage = rd.randint(0,len(cl.names)-1)

    setButtons()

def setButtons():
    global buttonsColors, buttonsLanguages

    buttonsColors = [currentRound2]
    buttonsLanguages = [rd.randint(0,len(cl.names)-1) for i in range(nButtons)]

    while (len(buttonsColors) < nButtons):
        c = rd.randint(0,9)
        if (c not in buttonsColors): buttonsColors.append(c)

    rd.shuffle(buttonsColors)

def printButtons():

    for i in range(nButtons):

        x = p[0] + i * (gap + l)
        y = p[1]
        
        if (x <= mouse[0] <= x + l and y <= mouse[1] <= y + l):
            pg.draw.rect(screen,(170,170,170),[x,y,l,l])
        else:
            pg.draw.rect(screen,(255,255,255),[x,y,l,l])

        msg = cl.names[buttonsLanguages[i]][buttonsColors[i]]
        size = l//5 - l//100 * (len(msg) - 5)
        printText(msg, cl.languages[buttonsLanguages[i]], x + l/2, y + l/2, (0,0,0), size)

def printScore():

    mainText = pg.font.Font('fonts/verdana.ttf', 40)
    text = mainText.render(f'Score: {score}', True, (0,0,0))
    textRect = text.get_rect(topleft = (10, 10))
    screen.blit(text, textRect)

def printTimer():

    mainText = pg.font.Font('fonts/verdana.ttf', 40)
    text = mainText.render(f'Time: {currentRoundTime/1000}', True, (0,0,0))
    textRect = text.get_rect(topleft = (10, 60))
    screen.blit(text, textRect)

def checkResult(res):
    global score

    if (buttonsColors[res] == currentRound2): score += 1

def countdonw():
    global previousRoundTime

    for i in range(5,0,-1):
        if (i == 5): screen.fill((255,0,0))
        elif (i == 4): screen.fill((255,255,0))
        elif (i == 3): screen.fill((0,255,0))
        elif (i == 2): screen.fill((0,255,255))
        elif (i == 1): screen.fill((0,0,255))

        printText(str(i), '', width//2, height//2, (0,0,0), 200)
        pg.display.update()
        pg.time.wait(1000)

    previousRoundTime = pg.time.get_ticks()

def setScreen(s, w, h):
    global screen, width, height, gap , p

    screen, width, height = s, w, h

    gap = (width - nButtons * l)/nButtons
    p = (gap/2, height - (width - 5 * l)/10 - l)