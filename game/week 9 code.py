# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
# from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

vec = pg.math.Vector2

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# player settings
PLAYER_FRIC = -0.2
PLAYER_GRAV = 1
POINTS = 0

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# sprites...
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_w]:
            self.acc.y = -5
        if keys[pg.K_s]:
            self.acc.y = 5
    def jump(self):
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        if hits:
            print("i've collided...")
            self.vel.y = -20
    def update(self):
        self.acc = vec(0,0)
        self.controls()
        
        # friction
        self.acc += self.vel * PLAYER_FRIC
        # self.acc.x += self.vel.x * PLAYER_FRIC
        # self.acc.y += self.vel.y * PLAYER_FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos

class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x+=1

        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
mobs = pg.sprite.Group()

# instantiate classes
# the settings for the blocks in the "game"
player = Player()
plat = Platform(WIDTH/2, HEIGHT/3, 100, 35)
plat2 = Platform(WIDTH/5, HEIGHT/6, 200, 25)
plat1 = Platform(75, 300, 100, 35)
# mob = Mob(25, 57, 25, 25)

# add instances to groups
all_sprites.add(player)
all_sprites.add(plat)
all_sprites.add(plat1)
# all_sprites.add(mob)
all_platforms.add(plat)
all_platforms.add(plat1)

for i in range(150):
    # instantiate mob class repeatedly
    m = Mob(randint(0, WIDTH), randint(0,HEIGHT), 25, 25, (randint(0,255), randint(0,255) , randint(0,255)))
    all_sprites.add(m)
    mobs.add(m)
print(mobs)
# Game loop
running = True
while running:
    # keep the loop running using clock
    dt = clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    hits = pg.sprite.spritecollide(player, all_platforms, False)
    if hits:
        print("i've collided...with a platform")
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    if mobhits:
        POINTS += 1
        print(POINTS)
        print("i've collided...with an enemy")
        print(mobhits[0].color)
    all_sprites.update()
    
    ############ Draw ################
    # draw the background screen

    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)
    draw_text("POINTS: " + str(POINTS), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw_text("FPS: " + str(dt), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw_text("asdfasdfasdfasdfasdf: " + str(dt), 22, WHITE, WIDTH / 2, HEIGHT / 24)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()