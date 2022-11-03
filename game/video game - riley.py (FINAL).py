# imported the necessary libraries needed for game to run 
from pygame.sprite import Sprite
import random
from random import randint
from ast import Break
from turtle import width
import pygame as pg

vec = pg.math.Vector2

# colors within the game 
GREEN = (0, 255, 0)
WHITE = (250, 250, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255,255,0)
PURPLE = (255,250,0)
RED = (255, 0, 0)

# the framework for the game   
HEIGHT = 825
WIDTH = 1200
FPS = 30
mpos = (0,0)

# the settings for the game 
PLAYER_FRIC = 1
PLAYER_GRAV = 0.5
SCORE = 0

def colorbyte():
    return random.randint(0,255)

# sprites...
# the code for the Player 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.r = 0
        self.g = 0
        self.b = 255
        self.image.set_colorkey(WHITE)
        self.image.fill((self.r,self.g,self.b))
        self.rect = self.image.get_rect()
        self.pos = vec(660,660)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 100
# keeps the player within bounds or within coordinates of the game 
    def inbounds(self):
        if self.pos.x < 1:
            self.pos.x = 1
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
# allows player to move horizontally 
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -1
        if keys[pg.K_d]:
            self.acc.x = 1
# allows vel. and grav. 
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        self.acc.x += self.vel.x * -0.6
        self.vel += self.acc
        self.pos += self.vel + 0.6 * self.acc
        self.inbounds()
        self.rect.midbottom = self.pos

    def draw(self):
        pass
# class...
# code for the bullets coming out of Player
class Pewpew(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.speed = 1

    def update(self):
        self.rect.y -= self.speed
        if (self.rect.y < 0):
            self.kill()
            print(pewpews)

# code for the enemies that the bullets hit  
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.speed *= -1
        
# platform
# code for the barriers that the bullets being absorbed 
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# creates a window for the game 
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("the game")
clock = pg.time.Clock()

# create the groups needed for the game 
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()
pewpews = pg.sprite.Group()

# instantiate the classes 
player = Player()
plat = Platform(180, 100, 200, 45)
plat2 = Platform(400, 110, 200, 45)
plat3 = Platform(616,200,150,50)
plat4 = Platform(600, 210, 300, 50)
plat5 = Platform(500,300, 120,50)
plat6 = Platform(126,310, 120,50)
plat7 = Platform(400,400, 223,23)
plat8 = Platform(668,410, 223,23)
plat9 = Platform(150, 500, 198, 85)
plat10 = Platform(270, 700, 198, 85)
plat11 = Platform(665,600,50,40)
plat12 = Platform(774,610,100,50)
plat13 = Platform(800,700,100,50)
ground = Platform(0, HEIGHT-40, WIDTH, 40)

# instantiate the mobs within a for loop
# add them to the certain groups 
for i in range(45):
    m = Mob(randint(0,WIDTH), randint(0,550), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
    all_sprites.add(m)
    mobs.add(m)
    print(m)
print(mobs)

# adding the plat(1,2,3...) to the groups 
all_sprites.add(player, plat, plat2, plat3, plat4, plat5,plat6, plat7, plat8,plat9, plat10, plat11, plat12, plat13, ground)
all_plats.add(plat, plat2, plat3, plat4, plat5, plat6, plat7, plat8,plat9, plat10, plat11, plat12, plat13, ground)

# GAME LOOP
# keeps game running
clock.tick(FPS)
# game loop 
running = True
while running:
# what happens when bullets his barriers(plat)
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
# what happens when bullets hit either mob or plat
    pewpewhits = pg.sprite.groupcollide(pewpews, mobs, True, True)
    pewpewhplat = pg.sprite.groupcollide(pewpews, all_plats, True, False)
# happens when bullets his mob or mob attacks player
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    if mobhits:
        player.health -= 1
        if player.r < 255:
            player.r += 15 

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            p = Pewpew(player.rect.midtop[0], player.rect.midtop[1], 10, 10)
            all_sprites.add(p)
            pewpews.add(p)
            mpos = pg.mouse.get_pos()
            print(mpos)
        
# updates all sprites included 
    all_sprites.update()


    #   fills the background screen black  
    screen.fill(BLACK)

   
    # displays the player's colors 
    player.image.fill((player.r,player.g,player.b))

    # displays the specified sprites 
    all_sprites.draw(screen)

   
    pg.display.flip()
    
    
# quit game
pg.quit()

