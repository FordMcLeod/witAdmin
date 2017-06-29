# references: http://inventwithpython.com/pygame/chapter2.html


# all the things we need to code this
import pygame 
import time
import random
from pygame.locals import * 
# -------------------------------- #
    
# game setup ------------- #
pygame.init()      # initalizes the pygame module
pygame.font.init() # initalizes the pygame font module
title = 'Pygame Tutorial'
size = (700,600)                               # size of window
display = pygame.display.set_mode(size,0,0)    # creates window
pygame.display.set_caption(title)              # creates title of game
# game setup --------------#

clock = pygame.time.Clock()


# draws 4 different rectangles with different colors and locations
pygame.draw.rect(display,(0, 128, 255), pygame.Rect(30,30,60,60))
pygame.draw.rect(display,(0, 0, 255), pygame.Rect(130,30,60,60))
pygame.draw.rect(display,(0, 128, 0), pygame.Rect(230,30,60,60))
pygame.draw.rect(display,(255, 255, 255), pygame.Rect(330,30,60,60))

font = pygame.font.SysFont("comicsans",50)              # use a font from the pygame system with size (if not found print(pygame.font.get_fonts()) and choose a different one
text = font.render("WOOOO THIS WORKS!!!",1,(255,255,0)) # draw text on a seperate font surface with text,color features
display.blit(text,(100, 100))                           # place text onto display at a location

cat = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'



while True:                     # game loop that goes on forever until user clicks close button
    event = pygame.event.poll() # get a single pygame event that allows us to check if we pressed a certain key etc.
    if event.type == QUIT:      # if user clicks the close button
        break                   # get out of game loop
    
    display.fill(pygame.Color('white')) # fill display with background color
    
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'    

    display.blit(cat,(catx,caty))     # place image on display with location
    clock.tick(30)                    # control speed of game using frames per second
    pygame.display.update()

pygame.display.quit()