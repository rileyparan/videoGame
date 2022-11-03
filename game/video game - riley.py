# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
# from platform import platform
from tokenize import group
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint

vec = pg.math.Vector2

# game settings 
WIDTH = 1200
HEIGHT = 800
FPS = 60

# player settings
PLAYER_GRAV = 0.8
PLAYER_FRIC = 0.1
SCORE = 0

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('timesnewroman')
        font = pg.font.Font(font_name, size) 
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

def colorbyte():
    return random.randint(0,255)

# sprites...
class Player(Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((50, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 40
        self.speedx = 0

    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5

    def update(self):
        self.speedx = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.speedx = -8
        if keystate[pg.K_d]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def inbounds(self):
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH

    def inbounds (self): 
        if self.pos.x < 0: 
            self.pos.x = 0
        if self.pos.x > HEIGHT: 
            self.pos.x = HEIGHT

    def shoot(self):
        Bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(Bullet)
        Bullet.add(Bullet)
        

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.speed *= -1
        
class Bullet(Sprite): 
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
bullets = pg.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
     m = Mob(randint(0,WIDTH), randint(0,550), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
all_sprites.add(m)
mobs.add(m)
print(m)
print(mobs)


# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
ground = Platform(0, HEIGHT-40, WIDTH, 40)

all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()
ground = Platform(0, HEIGHT-40, WIDTH, 40)
bullets = pg.sprite.Group()

# instantiate classes
player = Player()
plat = Platform(180, 380, 100, 35)
plat2 = Platform(289, 180, 100, 35)
plat3 = Platform (500, 200, 100, 35)
plat4 = Platform (800, 400, 100, 35)


for i in range(100):
    m = Mob(randint(0,WIDTH), randint(0,HEIGHT), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
    all_sprites.add(m)
    mobs.add(m)
    print(m)

# add player to all sprites group
all_sprites.add(player)
all_plats.add(plat, plat2)

# add platform to all sprites group
all_sprites.add(plat)
all_sprites.add(plat2)

# add things to their respective groups
all_sprites.add(player, plat, plat2, ground)
all_sprites.add(player, plat, plat2, ground)
all_sprites.add(player, plat, plat3, ground)
all_sprites.add(player, plat, plat4, ground)


# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pg.sprite.spritecollide(player, all_plats, True)
    if hits:
        print("ive struck a plat")
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
    mobhits = pg.sprite.spritecollide(player, mobs, False)
    if mobhits:
        print("ive struck a mob")
        SCORE += 1
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
        
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw text
    draw_text("POINTS: " + str(SCORE), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()

