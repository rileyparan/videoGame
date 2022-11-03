# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules needed 
import pygame as pg
from pygame.sprite import Sprite
import random
# 2 dimensional vector 
vec = pg.math.Vector2

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# define what the colors are 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# sprites...
# creates the player's certain class 
class Player(Sprite):
    # represent the instance of the class, access the attributes/methods of the class in python
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        # background to be green
        self.image.fill(GREEN)
        # rectangular area of the Surface 
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    # reference to the current instance of the class, used to access variables that belong to the class  
    def controls(self):
        # returns a list of the state of all keys 
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
            # print(self.vel)
        if keys[pg.K_d]:
            self.acc.x = 5
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        # includes friction within the game 
        self.acc.x += self.vel.x * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos
# 2D representation of something on the screen
# sprites...
class Platform(Sprite):
    # lets the class initialize the object's attributes 
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        # background green
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
# creates a clock object which can be used to keep track of time
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()

# instantiate the player class
player = Player()
plat = Platform(WIDTH/2, HEIGHT/3, 100, 35)

# adds the player to all the sprites group
all_sprites.add(player)
all_sprites.add(plat)


# Game loop
running = True
# runs until the "while" condition is satisfied 
while running:
    # it keep the loop running while using clock
    clock.tick(FPS)
# used to iterate a sequence (list, string)
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()
# quit function that closes pgame 
pg.quit()
