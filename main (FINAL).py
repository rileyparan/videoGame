# Sources Cited
# https://dev.to/ilya_romanov/the-snake-game-in-python-1enf - notes to help with the "Snake Game"
# https://www.edureka.co/blog/snake-game-with-pygame/ - Snake Game 

# imported the libraries necessary for the game to run 
import pygame
import time
import random
#  initializes all of the imported pygame modules 
pygame.init()
 
#  sets the colors within the game 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#  sets the frame work for the game 
dis_width = 600
dis_height = 400

#  displays the name of the game / sets the mode 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('The Snake Game - Riley Paran')

#  helps track time 
clock = pygame.time.Clock()

#  the settings for the "snakes" size/speed
snake_block = 10
snake_speed = 15

#  sets the font for the game when finished 
font_style = pygame.font.SysFont("TIMESNEWROMAN", 25)
score_font = pygame.font.SysFont("TIMESNEWROMAN", 35)

#  sets the settings for the "snake"
def our_snake(snake_block, snake_list):
    # gives the list for "snakes" characteristics 
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

#  sets the color and font style within the game 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#  game loop 
def gameLoop():
    game_over = False
    game_close = False

#  hold the updating values of the x and y coordinates 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
#  calls the list for the "snake"
    snake_List = []
    Length_of_snake = 1
#  random module - generate random numbers from a specified range 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

#  used to iterate over a block of code as long as the condition is true 
    while not game_over:
 
        while game_close == True:
            # background color for when the game is over 
            dis.fill(blue)
            # message for when the MC either wins or loses 
            message("You Lost! Press C to Play Again / Q to Quit", red)
#  updates pygame specifically the image 
            pygame.display.update()
#  keydown class of pygame
            for event in pygame.event.get():
                # key down command settings 
                # an event that leads to an action within the game which I have assigned 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # an event that leads to an action within the game which I have assigned 
            # calls for K(LEFT, RIGHT, UP, DOWN)... 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
#  makes sure the x and y coordinates are smaller than the screen size 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
# background color 
        dis.fill(blue)
# sets the settings for the "food" block 
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
# calls upon the "snake"
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
# settings for the "snakes" size
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
#  display the size of the snake - 1 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
#  updates/refreshes the disaply of the screen when the "snake" eats the "food" 
        pygame.display.update()
#  correlates towards the displayment size of the snake (-1)
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
#  time tracking 
        clock.tick(snake_speed)
#  used to uninitialize everything 
    pygame.quit()
    quit()
 
#  the loop that keeps the game running 
gameLoop