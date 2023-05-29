# The purpose of this program is to test the user's hand eye coordination, at any difficulty, whether that be the user is experienced or new. The audience is people of any age that have any level of hand-eye coordination.
# Imports
import pygame as pyg
import random as rnd
from pygame import mixer as mix
#base
mix.init()
# window code
screen = pyg.display.set_mode((800, 600))

clock = pyg.time.Clock()
#class. class is a group of objects
class Key():
#defined a function here with the group of objects that will be used to create the keys
  def __init__(self, x, y, color1, color2, key):
    self.x = x
    self.y = y
    self.color1 = color1
    self.color2 = color2
    self.key = key
    self.rect = pyg.Rect(self.x, self.y, 50, 20)
#key buttons
keys = [
  Key(100, 500,(255, 0, 0), (220, 0, 0), pyg.K_LEFT),
  Key(200, 500, (0, 255, 0), (0, 220, 0), pyg.K_UP),
  Key(300, 500,(0, 0, 255), (0, 0, 220), pyg.K_DOWN),
  Key(400, 500,(255, 255, 0), (220, 220, 0), pyg.K_RIGHT)
]

def load(map):
  rects = []
  f = open(map + ".txt", 'r')
  data = f.readlines()
 # mix.music.load(map + ".mp3")
 # mix.music.play()
  for y in range(len(data)):
    for x in range(len(data[y])):
      if data[y][x] == '0':
          rects.append(pyg.Rect(keys[x].rect.x - 25, y*100, 50, 25))
          pyg.display.flip()
  return rects
map_rect = load("testmap")
# iteration. when key is pressed, it will darken
k = pyg.key.get_pressed()
for key in keys:
  if k[key.key]:
    pyg.draw.rect(screen, key.color1, key.rect)
  if not k[key.key]:
    pyg.draw.rect(screen, key.color2, key.rect)

for rect in map_rect:
  pyg.draw.rect(screen, (200,0,0), rect)
  rect.y += 1

clock.tick(60)
pyg.display.flip()

# to close window
while True:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            quit()