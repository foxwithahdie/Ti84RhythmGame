import pygame as pyg
import random as rand
import time
import numpy as np
import math
from pygame import mixer as mix
import sys

pyg.display.init()

display = pyg.display.set_mode((800, 600))
width = display.get_width()
height = display.get_height()
clock = pyg.time.Clock()

class PlayerKey(pyg.sprite.Sprite):
    def __init__(self, x, y, rect, filename, button):
        self.x = x
        self.y = y #need to create a variable with a sort of section. then further subtract from it (PERCENTAGE)
        image = pyg.image.load(filename + ".png").convert()
        rect = image.get_rect()
        self.button = button
    def c
# window
while True:
    for event in pyg.event.get():
        if event.type == pyg.constants.QUIT:
            sys.exit()
