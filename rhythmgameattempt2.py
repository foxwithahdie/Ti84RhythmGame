import pygame as pyg
import random as rand
import time
import numpy as np
import math
from pygame import mixer as mix
import sys

pyg.display.init()

screen = pyg.display.set_mode((800, 600))
width = screen.get_width()
height = screen.get_height()
clock = pyg.time.Clock()

# background1 = pyg.image.load("backgr0.png").convert()
# screen.blit(background1, (0,0))
framerate = 60

class PlayerKey(pyg.sprite.Sprite):
    def __init__(self, x, y, filename, button):
        self.x = x
        self.y = y #need to create a variable with a sort of section. then further subtract from it PERCENTAGE
        image = pyg.image.load(filename + ".png").convert()
        rect = image.get_rect()
        self.button = button
# window
pyg.display.flip()
clock.tick(framerate)
while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            print(2)