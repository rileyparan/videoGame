# import the certain libraries and modules needed 
import pygame as pg
from pygame.sprite import Sprite
import random

import os

# sets up the image onto the game file 
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# defines what the colors are 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# creates the player's certain clas 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # imports the Bell image onto the game for it to be displayed 
        self.image = pg.image.load(os.path.join(img_folder, 'power.jpg')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        print(self.rect.center)
        # allows the character's to move around 
    def update(self):
        self.rect.x += 5
        self.rect.y += 5
        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.y > HEIGHT:
            self.rect.y = 0

# as it goes into py game, it initializes all imported pygame modules and for it to be showed  
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

# container class to hold/manage multiple Sprite objects  
all_sprites = pg.sprite.Group()

# calls the player class using the parenthesis
player = Player()

# adds the particular player to all the sprites group
all_sprites.add(player)


# this would be the game loop
running = True
while running:
    # this keeps the loop running using the clock
    # will compute how many milliseconds have passed since the last call
    clock.tick(FPS)

    # enables a class to notify other classes 
    for event in pg.event.get():
        # check for closed window
        # if the event obect is a quit event, it runs the code that deactivates the pg library
        if event.type == pg.QUIT:
            running = False
    
    # update all sprites
    all_sprites.update()

    # changes the background screen color
    screen.fill(GREEN)
    # draw all sprites, calling the screen 
    all_sprites.draw(screen)

# allows only a portion of the screen to be updated instead of the entire area
    pg.display.flip()

pg.quit()
# run the code that deactivates the Pygame library 
