import sys
import pygame as pg
import colorgame as cg
import mainmenu as mm
import colors as cl

pg.init()

dim = width, height = 900, 600

screen = pg.display.set_mode(dim)
pg.display.set_caption('color game')

mm.setScreen(screen, width, height)
cg.setScreen(screen, width, height)

start = True
while start:
    start = mm.main()

cl.loadLanguages(mm.languagesConfigButtonsSelected)
cg.nextRound()
#cg.countdonw()

while True:
    cg.main()