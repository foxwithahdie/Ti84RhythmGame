import pygame as pyg
import random as rand
import time
import numpy as np
import math
from pygame import mixer as mix
import sys






# window
while True:
    for event in pyg.event.get():
        if event.type == pyg.constants.QUIT:
            sys.exit()
