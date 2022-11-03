

# imported the necessary libraries 
from random import randint
import pygame as pg
from pygame.sprite import Sprite 
from ast import Break
import random
from turtle import width
from platform import platform

vec = pg.math.Vector2 

# the settings for the game 
WIDTH = 1200
HEIGHT = 600
FPS = 25
# the settings for the player 
PLAYER_GRAV = 0.6
PLAYER_FRIC = 0.5
SCORE = 0
# Colors
WHITE = (300,300,300)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
ORANGE = (300, 95,0)
YELLOW = (275, 100, 0)
PURPLE = (150, 200, 0)

# determines the images/words within the game 
def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('timesnewroman')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

def colorbyte(x,y):
   return random.randint (0,255)

class Player(Sprite): 
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface ((50,50))
        self.b = 265
        self.image.fill((self.b))
        self.rect = self.image.get_rect()
        self.pos = vec(675,675)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 15

    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
    
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, platform, False)
        self.rect.x += -1
        if hits:
            self.jumps = 2
        if self.jumps > 0:
            self.vel.y = -self.jumppower
            self.jumps -=1
            print(self.jumps)

    def inbounds(self):
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH

    def inbounds(self):
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > HEIGHT:
            self.pos.x = HEIGHT
            
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # sets the friction
        self.acc.x += self.vel.x * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.inbounds()
        self.rect.midbottom = self.pos

        all_sprites.add()
        Bullet.add()

    def draw(self): 
        pass 

class Platform(Sprite): 
    def __init__(self, x, y, w, h, typeof):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Bullet(Sprite): 
    def __init__(self, x, y, w, h): 
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect.x = x
        self.rect.y = y 
        self.speed = 6
        self.rect = self.image.get_rect()
    def update(self): 
        self.rect.y -= self.speed
        if (self.rect.y <0): 
            self.kill()
            print (Bullet)


class GANG(Sprite): 
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH or self.rect.x < 0: 
            self.speed *= -1 


pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("the game")
clock = pg.time.Clock()

Player = Player()

plat = Platform(150, 370, 98, 25)
plat2 = Platform(250, 375, 100, 25)
plat3 = Platform(500, 250, 88, 45)
plat4 = Platform(75, 255, 130, 45)
plat5 = Platform(85, 475, 120, 85)
plat6 = Platform(80, 500, 115, 90)
ground = Platform(0, HEIGHT-40, WIDTH, 40)
print(Player.rect.x)
print(Player.rect.y)


all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
GANG = pg.sprite.Group()
Bullet = pg.sprite.Group()


for i in range(30):
    m = GANG(randint(0,WIDTH), randint(0,600), 27, 27, (colorbyte(),colorbyte(),colorbyte()))
all_sprites.add(m)
GANG.add(m)
print(m)
print(GANG)

all_sprites.add(Player, plat, plat2, plat3, plat4, plat5, plat6)
all.sprites.add(Player, plat, plat2, plat3, plat4, plat5, plat6) 

# game loop
clock.tick (FPS)

running = True
while running: 

    hits = pg.sprite.spritecollide(Player, all_plats, False)
    if hits:
        Player.pos.y = hits[0].rect.top
        Player.vel.y = 0
    Bullethits = pg.sprite.groupcollide(Bullet, GANG, True, True)
    GANGplat = pg.sprite.groupcollide(Bullet, all_plats, True, False)
        
    mobhits = pg.sprite.spritecollide(Player, GANG, True)
if mobhits:
        Player.health -= 1
        if Player.r < 255:
            Player.r += 15 
for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            p = Bullet(Player.rect.midtop[0], Player.rect.midtop[1], 9, 9)
            all_sprites.add()
            Bullet.add()
            mpos = pg.mouse.get_pos()
            print(mpos)
        if event.type == pg.KEYDOWN: 
            if event.key == pg.K_SPACE: 
                Player.jump()
all_sprites.update()

screen.fill(BLACK)
draw_text("HEALTH: " + str(Player.health), 25, WHITE, WIDTH / 3, HEIGHT / 11)

all_sprites.draw(screen)
pg.display.flip() 
if Player.health == (0): 
    print("GAME OVER")
Break
pg.quit() 
