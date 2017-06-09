# original code : https://pythonprogramming.net/displaying-images-pygame/?completed=/pygame-python-3-part-1-intro/

# import modules we need for the game
import pygame
from pygame.locals import *
import time
import random

pygame.init()                       # initialize pygame module
clock = pygame.time.Clock()         # initalize clock for frames per second

# game variables---#
display_width = 800
display_height = 600
x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0
car_width = 73
# ----------------#

# create the display with size and title
display = pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption('Game')
# -----------------# 

# color codes
black = (0,0,0)
white = (255,255,255)

pygame.key.set_repeat(20,20)
carImg = pygame.image.load('racecar.png') # load an image from our current directory

def car(x,y):                         # function for creating the car that takes x,y coordinates
    display.blit(carImg, (x,y))       # place car onto display


def game():
    global x,y,x_change,display_width,car_width
    
    collided = False
    
    while True:
        event = pygame.event.poll()       # takes a pygame event
        if event.type == QUIT:     # if we wish to quit the game break out of loop
            break
        if event.type == KEYDOWN:         # if we press down key
            if event.key == K_LEFT:       # if we press left key
                x_change = -5             # change car speed by amount
            if event.key == K_RIGHT:      # if we press right key
                x_change = 5
        if event.type == KEYUP:           # if we let go of key, stop car speed/movement
            if event.key == K_LEFT or event.key == K_RIGHT:
                x_change = 0
                
        x += x_change                    # change x position of car by its speed
        
    
        display.fill(white)              # fill screen with background color
        car(x,y)                         # call car function to create it
        
        if x > display_width - car_width or x < 0: # car collision
            collided = True    
    
        pygame.display.update()          # update display after every iteration
        clock.tick(60)                   # frames per second

    pygame.display.quit()                # quit the game
    
game()