import sys
import math
import pygame as pg
from colors import *

rules = []
with open(f'rules.txt', encoding='utf-8') as f:
    rules = [i.replace('\n', '') for i in f]

mainMenuButtonsNames = ['Start Game','Rules','Settings','Quit']
rulesButtonsNames = ['Back']
configButtonsNames = ['Colors', 'Languages', 'Back']
colorsButtonsNames = ['Back']
languagesConfigButtonsNames = allLanguages + ['Back']

mainMenuButtonSelected = [False for i in mainMenuButtonsNames]
configButtonSelected = [False for i in configButtonsNames]
languagesConfigButtonsSelected = [False for i in allLanguages] + [False]

buttonWidth = 200
buttonHeight = 50

inputBoxWidth = 60
inputBoxHeight = 50

def main():
    global mouse

    mouse = pg.mouse.get_pos()

    for event in pg.event.get():
        if (event.type == pg.QUIT): sys.exit()

        if event.type == pg.KEYDOWN:
            if (configButtonSelected[0]):
                for i, t in enumerate(colorInputBoxesText):
                    if (colorInputBoxSelected[i]):
                        if event.key == pg.K_BACKSPACE:
                            colorInputBoxesText[i] = t[:-1]
                        else:
                            if (len(colorInputBoxesText[i]) < 3 and event.unicode.isnumeric() and colorInputBoxesText[i] != '0' and int(colorInputBoxesText[i] + event.unicode) <= 255):
                                colorInputBoxesText[i] += event.unicode

        if event.type == pg.MOUSEBUTTONDOWN:
            if (True not in mainMenuButtonSelected):
                for i in range(len(mainMenuButtonsNames)):
                    mainMenuButtonSelected[i] = mainMenuButtons[i].collidepoint(event.pos)

            if (mainMenuButtonSelected[1]):
                mainMenuButtonSelected[1] = not rulesButtons[0].collidepoint(event.pos)

            if (mainMenuButtonSelected[2]):
                if (True not in configButtonSelected):
                    for i in range(len(configButtonsNames)):
                        configButtonSelected[i] = configButtons[i].collidepoint(event.pos)

                if (configButtonSelected[0]):
                    configButtonSelected[0] = not colorsButtons[-1].collidepoint(event.pos)

                    for i, box in enumerate(colorInputBoxs):
                        colorInputBoxSelected[i] = box.collidepoint(event.pos)
                        
                if (configButtonSelected[1]):
                    configButtonSelected[1] = not languagesConfigButtons[-1].collidepoint(event.pos)

                    for i, msg in enumerate(languagesConfigButtonsNames[:-1]):
                        if (languagesConfigButtons[i].collidepoint(event.pos)):
                            languagesConfigButtonsSelected[i] = not languagesConfigButtonsSelected[i]

    screen.fill((100,100,100))

    if (mainMenuButtonSelected[0]): 
        return False
    elif (mainMenuButtonSelected[1]):
        rulesScreen()  
    elif (mainMenuButtonSelected[2]):
        configScreen()
    elif (mainMenuButtonSelected[-1]):
        sys.exit()

    if (True not in mainMenuButtonSelected): 
        for i, msg in enumerate(mainMenuButtonsNames): 
            printButton(msg, mainMenuButtons[i], False)

    pg.display.update()
    return True

def printLables(msg, label, color):
    pg.draw.rect(screen,color,label)

    size = 20
    font = 'fonts/verdana.ttf'
    mainText = pg.font.Font(font, size)
    text = mainText.render(msg, True, (0,0,0))
    textRect = text.get_rect(center = label.center)
    screen.blit(text, textRect)

def printButton(msg, button, selected):
        
    if (button.collidepoint(mouse) and selected):
        pg.draw.rect(screen,(170,255,170),button)
    elif (not button.collidepoint(mouse) and selected):
        pg.draw.rect(screen,(0,255,0),button)
    elif (button.collidepoint(mouse) and not selected):
        pg.draw.rect(screen,(170,170,170),button)
    else:
        pg.draw.rect(screen,(255,255,255),button)

    size = 20
    font = 'fonts/verdana.ttf'
    mainText = pg.font.Font(font, size)
    text = mainText.render(msg, True, (0,0,0))
    textRect = text.get_rect(center = button.center)
    screen.blit(text, textRect)

def printInputBox(msg, box, selected):
    if (selected):
        pg.draw.rect(screen, (200,200,200), box)
    else:
        pg.draw.rect(screen, (150,150,150), box)

    size = 25
    font = 'fonts/verdana.ttf'
    mainText = pg.font.Font(font, size)
    text = mainText.render(msg, True, (0,0,0))
    textRect = text.get_rect(center = box.center)
    screen.blit(text, textRect)

def rulesScreen():

    msg = ''
    for i, msg in enumerate(rules):
        
        if (len(rules) % 2 == 0): g = (i - len(rules)/2 + 1/2) * 30
        else: g = math.floor(i - len(rules)/2 + 1) * 30

        font = 'fonts/verdana.ttf'
        mainText = pg.font.Font(font, 20)
        text = mainText.render(msg, True, (0,0,0))
        textRect = text.get_rect(center = (width//2, height//2 + g))
        screen.blit(text, textRect)
    
    printButton(rulesButtonsNames[0], rulesButtons[0], False)

def configScreen():
        
    if (configButtonSelected[0]):
        
        printButton(colorsButtonsNames[0], colorsButtons[-1], False)
        
        n = getNames('english')
        for i in range(len(colorList)):
            printLables(n[i],colorNamesButtons[i],(255,255,255))

        for i, box in enumerate(colorInputBoxs):
            printInputBox(colorInputBoxesText[i], box, colorInputBoxSelected[i])

        setColors(colorInputBoxesText)
            
        for i, color in enumerate(colorList):
            pg.draw.rect(screen, color, colorsButtons[i])

    elif (configButtonSelected[1]):

        for i, msg in enumerate(languagesConfigButtonsNames):
            printButton(msg, languagesConfigButtons[i], languagesConfigButtonsSelected[i])

    elif (configButtonSelected[-1]):

        configButtonSelected[-1] = False
        mainMenuButtonSelected[2] = False

    else:
        for i, msg in enumerate(configButtonsNames):
            printButton(msg, configButtons[i], False)

def setScreen(s, w, h):
    global screen, width, height
    global mainMenuButtons
    global rulesButtons
    global configButtons
    global colorNamesButtons, colorInputBoxs, colorInputBoxSelected, colorInputBoxesText, colorsButtons
    global languagesConfigButtons

    screen, width, height = s, w, h

    gap1 = (height - len(mainMenuButtonsNames) * buttonHeight)//len(mainMenuButtonsNames)
    mainMenuPos = (10, gap1//2)
    mainMenuButtons = [pg.Rect(mainMenuPos[0], mainMenuPos[1] + i * (gap1 + buttonHeight), buttonWidth, buttonHeight) for i in range(len(mainMenuButtonsNames))]

    rulesPos = ((width - buttonWidth)//2, height - 10 - buttonHeight)
    rulesButtons = [pg.Rect(rulesPos[0], rulesPos[1], buttonWidth, buttonHeight)]

    gap2 = (height - len(configButtonsNames) * buttonHeight)//len(configButtonsNames)
    configPos = (10, gap2//2)
    configButtons = [pg.Rect(configPos[0], configPos[1] + i * (gap2 + buttonHeight), buttonWidth, buttonHeight) for i in range(len(configButtonsNames))]

    gap3 = (height - len(colorList) * buttonHeight)//len(colorList)
    colorPos = (10, gap3//2)
    colorNamesButtons = [pg.Rect(colorPos[0], colorPos[1] + i * (gap3 + buttonHeight), buttonWidth, buttonHeight) for i in range(len(colorList))]

    colorInputBoxs = [pg.Rect(colorPos[0] + 10 + buttonWidth + i * (10 + inputBoxWidth), colorPos[1] + j * (10 + inputBoxHeight), inputBoxWidth, inputBoxHeight) for j in range(len(colorList)) for i in range(3)]
    colorInputBoxSelected = [False for i in colorInputBoxs]
    colorInputBoxesText = [str(j) for i in colorList for j in i]

    colorsButtons = [pg.Rect(colorPos[0] + 10 + buttonWidth + 3 * (10 + inputBoxWidth), colorPos[1] + i * (gap3 + buttonHeight), buttonWidth, buttonHeight) for i in range(len(colorList))] + [pg.Rect(width - 10 - buttonWidth, height - 10 - buttonHeight, buttonWidth, buttonHeight)]

    
    qnth = width//buttonWidth
    qntv = math.ceil(len(allLanguages)/qnth)
    gaph = (width - qnth * buttonWidth)//qnth
    gapv = ((height - 10 - buttonHeight) - qntv * buttonHeight)//qntv
    gap4 = (gaph,gapv)
    languagesPos = (gaph//2, gapv//2)
    languagesConfigButtons = [pg.Rect(languagesPos[0] + i * (gap4[0] + buttonWidth), languagesPos[1] + j * (gap4[1] + buttonHeight), buttonWidth, buttonHeight) for j in range(qntv) for i in range(qnth) if (i + j * qnth < len(allLanguages))] + [pg.Rect(10, height - 10 - buttonHeight, buttonWidth, buttonHeight)]
