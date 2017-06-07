# Code references: http://www.pygame.org/project-Very+simple+Pong+game-816-.html


# Import things we need for our pong game
import pygame
import random
from pygame.locals import *

pygame.init()                                          # Initalize pygame module
pygame.font.init()                                     # Initialize font features for text

screen = pygame.display.set_mode((640,480),0,0)        # set screen size
pygame.display.set_caption("Pong!!!!!")                # create title for game

# Create background
back = pygame.Surface((640,480))                       # create surface for background
background = back.convert()                            # convert surface for easier rendering
background.fill(pygame.Color('black'))                 # fill background with desired color

# create the padddles/bars 
bar = pygame.Surface((10,50))                          # create surface for bar
bar1 = bar.convert()                                  
bar_color = pygame.Color('white')                      
bar1.fill(bar_color)                                   # colour player 1's bar with desired colour
bar2 = bar.convert()
bar2.fill(bar_color)                                   # colour player 2's bar with desired colour

# create the ball
circ_surface = pygame.Surface((15,15))   
ball_color = pygame.Color('orange')
circ = pygame.draw.circle(circ_surface,ball_color,(15//2,15//2),15//2)
ball = circ_surface.convert()
ball.set_colorkey((0,0,0))
score_color = pygame.Color('white')

# set speed and location of both player's paddles and the ball
bar1_location = [10,215]                      # location of player1's bar with x,y coordinates
bar2_location = [620,21]                      # location of player2's bar with x,y coordinates
score = [0,0]                                 # the score of both players
movement = [0,0]                              # movement of bar with x,y coordinates
ball_location = [307.5,232.5]                 # location of the ball with x,y coordinates
ball_speed = [250, 250, 250]                  # speed of the ball with x,y coordinates and the last option being AI's

#clock and font objects
clock = pygame.time.Clock()                   # need clock for frame movement (frames per second)
font = pygame.font.SysFont("calibri",40)      # pick font for scores

# aesthetic features of game
frame_rectobject = Rect((5,5),(630,470))


while True:
    event = pygame.event.poll()
    if event.type == QUIT:
        break
    if event.type == KEYDOWN:
        if event.key == K_UP:
            movement[1] = -ai_speed
        elif event.key == K_DOWN:
            movement[1] = ai_speed
    elif event.type == KEYUP:
        if event.key == K_UP:
            movement[1] = 0
        elif event.key == K_DOWN:
            movement[1] = 0
    
    score1 = font.render(str(score[0]),True,score_color)
    score2 = font.render(str(score[1]),True,score_color)

    screen.blit(background,(0,0))
    frame = pygame.draw.rect(screen,pygame.Color('white'),frame_rectobject,2)
    middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
    screen.blit(bar1,bar1_location)
    screen.blit(bar2,bar2_location)
    screen.blit(ball,ball_location)
    screen.blit(score1,(250,210))
    screen.blit(score2,(380,210))

    bar1_location[1] += movement[1]
    
# movement of ball
    time_passed = clock.tick(60)
    time_sec = time_passed / 1000.0
    
    ball_location[0] += ball_speed[0] * time_sec
    ball_location[1] += ball_speed[1] * time_sec
    ai_speed = ball_speed[2] * time_sec
    
    
#AI of the computer.
    if ball_location[0] >= 305.:
        if not bar2_location[1] == ball_location[1] + 7.5:
            if bar2_location[1] < ball_location[1] + 7.5:
                bar2_location[1] += ai_speed
            if  bar2_location[1] > ball_location[1] - 42.5:
                bar2_location[1] -= ai_speed
        else:
            bar2_location[1] == ball_location[1] + 7.5
    
    if bar1_location[1] >= 420: 
        bar1_location[1] = 420
    elif bar1_location[1] <= 10: 
        bar1_location[1] = 10
    if bar2_location[1] >= 420:
        bar2_location[1] = 420
    elif bar2_location[1] <= 10: 
        bar2_location[1] = 10.
    
    
    
# collisions based on the size of the display
    if ball_location[0] <= bar1_location[0] + 10.:
        if ball_location[1] >= bar1_location[1] - 7.5 and ball_location[1] <= bar1_location[1] + 42.5:
            ball_location[0] = 20
            ball_speed[0] = -ball_speed[0]
    if ball_location[0] >= bar2_location[0] - 15:
        if ball_location[1] >= bar2_location[1] - 7.5 and ball_location[1] <= bar2_location[1] + 42.5:
            ball_location[0] = 605.
            ball_speed[0] = -ball_speed[0]
    if ball_location[0] < 5:
        score[1] += 1
        ball_location = [320,232.5]
        bar1_location[1] = 215
        bar2_location[1] = 215
    elif ball_location[0] > 620:
        score[0] += 1
        ball_location =[320,232.5]
        bar1_location[1] = 215
        bar2_location[1] = 215        
    if ball_location[1] <= 10:
        ball_speed[1] = -ball_speed[1]
        ball_location[1] = 10.
    elif ball_location[1] >= 457.5:
        ball_speed[1] = -ball_speed[1]
        ball_location[1] = 457.5

    pygame.display.update()                 

pygame.display.quit()