import pygame as pyg
import random as rand
import time
from pygame import mixer as mix
import os


pyg.display.init()
pyg.font.init()
mix.init()

screen = pyg.display.set_mode((800, 600))
width = screen.get_width()
height = screen.get_height()
clock = pyg.time.Clock()

framerate = 60

worldFont = pyg.font.SysFont("Monospace", 20)

selectorFont = pyg.font.SysFont("Cambria", 32)

color_base = pyg.Color(200, 200, 200)
color_clicked = pyg.Color(255, 192, 203)



def distance(rect1, rect2):
    x1, y1 = rect1.center
    x2, y2 = rect2.center
    return ( (x1 - x2) ** 2 + (y1 - y2) ** 2 ) ** 0.5

class KeybindChanger:
    def __init__(self, left, top):
        self.active = False
        self.value = ""
        self.rect = pyg.Rect(left, top, 50, 30)

    def update(self, event, playerkey):
        if event.type == pyg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pyg.KEYDOWN:
            if self.active:
                if event.key == pyg.K_BACKSPACE:
                    self.value = self.value[:-1]
                else:
                    self.value = event.unicode.upper()
                    key_value = pyg.key.key_code(self.value)
                    playerkey.update_button(key_value)
                if len(self.value) > 1:
                    self.value = self.value[0]
    def draw(self, screen):
        color = color_clicked if self.active else color_base

        pyg.draw.rect(screen, color, self.rect)

        if self.value != "":
            text_surface = worldFont.render(self.value, True, (0, 0, 0))
            screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
            self.rect.w = max(50, text_surface.get_width())

class Note(pyg.sprite.Sprite):
    """
    Falling notes.
    """

    def __init__(self, left, top, image, list):
        super().__init__()
        self.image = pyg.image.load(image).convert_alpha()
        self.image = pyg.transform.scale(
            self.image, (self.image.get_size()[0] / 1.5, self.image.get_size()[1] / 1.5)
        )
        self.rect = self.image.get_rect()
        self.rect.top = top
        self.rect.left = left
        list.append([self.image, self.rect])

    def update(self):
        self.rect.top += scroll_speed
        
    def draw(self, screen, note):
        screen.blit(note[0], note[1])

class PlayerKey(pyg.sprite.Sprite):
    def __init__(self, x, y, filename, filenameDull, button):
        super().__init__()
        self.x = x
        self.y = y  # need to create a variable with a sort of section. then further subtract from it PERCENTAGE
        self.image = pyg.image.load(filename + ".png").convert_alpha()
        self.image = pyg.transform.scale(
            self.image, (self.image.get_size()[0] / 1.5, self.image.get_size()[1] / 1.5)
        )
        self.imageDull = pyg.image.load(filenameDull + ".png").convert_alpha()
        self.imageDull = pyg.transform.scale(
            self.imageDull, (self.imageDull.get_size()[0] / 1.5, self.imageDull.get_size()[1] / 1.5)
        )
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.button = button
        self.is_pressed = False
        self.counter = worldFont.render("0", True, (0, 0, 0))
        #self.perfectCounter = worldFont.render("Perfect", True, (0,0,0))
        #self.goodCounter = worldFont.render("Good", True, (0,0,0))
        #self.okCounter  = worldFont.render("Ok", True, (0,0,0))
        #self.worldFont.render("Bad", True, (0,0,0))
        #worldFont.render("Miss", True, (0,0,0))

    def update_button(self, button):
        self.button = button
    def press_button(self, event, list, group):
        if event.type == pyg.KEYDOWN:
            if event.key == self.button:
                self.is_pressed = True
                self.rect = self.imageDull.get_rect()
                self.rect.left = self.x
                self.rect.top = self.y
                pyg.sprite.spritecollide(self, group, True)
        if event.type == pyg.KEYUP:
            self.is_pressed = False
            self.rect = self.image.get_rect()
            self.rect.left = self.x
            self.rect.top = self.y
    def judgement(self, group):
        for note in group.sprites:
            pass
    """
                
    Continue with this idea.
                
    Perfect if timer =  when they are totally touching
    Good - if timer = when is half way touching - scale with scroll speed
    Bad - if timer = when they are close to not touching - scale with scroll speed
    Miss -  if self.rect.collidepoint(fallingrect) == False: miss counter +1
    """

    """
    use / abuse pyg.time.Clock code, that way you can track timings not based on numbers but rather the actual timing of the client.
    """
    
    def draw(self, screen):
        if self.is_pressed:
            image = self.imageDull
            screen.blit(image, self.rect)
        else:
            image = self.image
            screen.blit(image, self.rect)
            
class MenuSelector(pyg.sprite.Sprite):
    
    def __init__(self, x, y, select):
        super().__init__()
        self.x = x
        self.y = y
        self.selectorRender = selectorFont.render(select, True, (0,0,0))
        self.rect = self.selectorRender.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.is_pressed = False
        self.surface = pyg.Surface((self.rect.width*2, self.rect.height*1.2))
        #if self.rect.collidepoint(pyg.mouse.get_pos()):
            #self.surface.fill((255, 192, 203))
    def draw(self, screen):
       # screen.blit(self.surface, self.rect)
        screen.blit(self.selectorRender, self.rect)
       # if self.rect.collidepoint(pyg.mouse.get_pos()) and pyg.mouse.get_pressed()[0]:
        #    self.surface.fill((252, 149, 167))
        
    # def is_clicked(self, group):
    #     self.is_pressed = False
    #     if pyg.mouse.get_pressed()[0]:
    #         if self.rect.collidepoint(pyg.mouse.get_pos()):
    #             print(4)
    #             self.is_pressed = True
    #             pyg.sprite.spritecollide(self, group, True)
    #             return True
        
    # def is_clicked_event(self, event, group):
    #     self.is_pressed = False
    #     if event.type == pyg.MOUSEBUTTONDOWN:
    #         if self.rect.collidepoint(event.pos):
    #             self.is_pressed = True
    #             pyg.sprite.spritecollide(self, group, True)
    #             return True
    
notesGroup = pyg.sprite.Group()

def load(map):
    global notes
    notes = []
    global notesCall
    notesCall = []
    f = open(map, "r")
    data = f.readlines()
    # data.reverse()
    #mix.music.load("Music\91 Battle! (Elite Four).mp3")
    #mix.music.set_volume(2)
    #mix.music.play()
    for y in range(len(data)):
        if len(data[y]) >= 1 and data[y][0] == "0":
            yellow = Note(150, 150 - y*65, os.path.join("Assets", "Yellowcircle.png"), notes)
            notesCall.append(yellow)
            notesGroup.add(yellow)
        if len(data[y]) >= 2 and data[y][1] == "0":
            purple = Note(275, 150 - y*65, os.path.join("Assets", "Purplecircle.png"), notes)
            notesCall.append(purple)
            notesGroup.add(purple)
        if len(data[y]) >= 3 and data[y][2] == "0":
            red = Note(400, 150 - y*65, os.path.join("Assets", "Redcircle.png"), notes)
            notesCall.append(red)
            notesGroup.add(red)
        if len(data[y]) >= 4 and data[y][3] == "0":
            blue = Note(525, 150 - y*65, os.path.join("Assets", "Bluecircle.png"), notes)
            notesCall.append(blue)
            notesGroup.add(blue)
    
    return notes

map_1 = load(os.path.join("Assets", "testmap.txt"))

clock.tick(framerate)

keybind_changers = []
player_keys = []

for i in range(4):
    keybind_changers.append(KeybindChanger(225 + 100 * i, 300))

player_keys.append(PlayerKey(150, 475, os.path.join("Assets", "greyscalecircle"), os.path.join("Assets", "yellowcircleDull"), pyg.K_d))
player_keys.append(PlayerKey(275, 475, os.path.join("Assets", "greyscalecircle"), os.path.join("Assets", "purplecircleDull"), pyg.K_f))
player_keys.append(PlayerKey(400, 475, os.path.join("Assets", "greyscalecircle"), os.path.join("Assets", "redcircleDull"), pyg.K_j))
player_keys.append(PlayerKey(525, 475, os.path.join("Assets", "greyscalecircle"), os.path.join("Assets", "bluecircleDull"), pyg.K_k))

scroll_speed = 10   

MenuGroup = pyg.sprite.Group()

playButton = MenuSelector(300, 300, "Play")
optionsButton = MenuSelector(300, 400, "Options")
backButton = MenuSelector(50, 50, "Back")

MenuGroup.add(playButton)
MenuGroup.add(optionsButton)

currentPage = "start"

# print(str(MenuGroup))
while True:
    
    screen.fill((255,255,255))   

    if currentPage == "start":
        playButton.draw(screen)
        optionsButton.draw(screen)
    
        if pyg.mouse.get_pressed()[0] and playButton.rect.collidepoint(pyg.mouse.get_pos()):
            currentPage = "game"
            continue
        
        if pyg.mouse.get_pressed()[0] and optionsButton.rect.collidepoint(pyg.mouse.get_pos()):
            currentPage = "options"
            continue
        

    if currentPage == "game":
        for i in range(len(player_keys)):
            player_keys[i].draw(screen)

        notesGroup.draw(screen)
        notesGroup.update()

    if currentPage == "options":
        for keybind_changer in keybind_changers:
            keybind_changer.draw(screen)
            backButton.draw(screen)
        
        if pyg.mouse.get_pressed()[0] and backButton.rect.collidepoint(pyg.mouse.get_pos()):
            currentPage = "start"
            continue

    
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            exit()
            
        for i in range(len(keybind_changers)):
            keybind_changers[i].update(event, player_keys[i])
            
        for i in range(len(player_keys)):
            player_keys[i].press_button(event, notesCall, notesGroup)
        
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                currentPage == "start"
                continue
            if event.key == pyg.K_TAB:
                scroll_speed = 0
            if event.key == pyg.K_0:
                scroll_speed = 10
                

            
            
    pyg.display.flip()
    clock.tick(framerate)