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


x = 30
y = 30 
clock = pygame.time.Clock()
pygame.key.set_repeat(20, 20)


# draws 4 different rectangles with different colors and locations
pygame.draw.rect(display,(0, 128, 255), pygame.Rect(30,30,60,60))
pygame.draw.rect(display,(0, 0, 255), pygame.Rect(130,30,60,60))
pygame.draw.rect(display,(0, 128, 0), pygame.Rect(230,30,60,60))
pygame.draw.rect(display,(255, 255, 255), pygame.Rect(330,30,60,60))

font = pygame.font.SysFont("comicsans",50)              # use a font from the pygame system with size (if not found print(pygame.font.get_fonts()) and choose a different one
text = font.render("WOOOO THIS WORKS!!!",1,(255,255,0)) # draw text on a seperate font surface with text,color features
display.blit(text,(100, 100))                           # place text onto display at a location



while True:                     # game loop that goes on forever until user clicks close button
    event = pygame.event.poll() # get a single pygame event that allows us to check if we pressed a certain key etc.
    if event.type == QUIT:      # if user clicks the close button
        break                   # get out of game loop
    
    
    # ***** can comment out lines 44-57 to demo the text and rectangle drawing before the while loop
    
    elif event.type == KEYDOWN:             # if user holds down key
        if event.key == K_LEFT:             # if user hits left key
            x -= 3                          # move rectangle to the left             
        elif event.key == K_RIGHT:          # if user hits right key
            x += 3                          # move rectangle to the right
        elif event.key == K_UP:             # if user hits up key
            y -= 3                          # move rectangle up (remmeber that in pygame (0,0) starts at top left
        elif event.key == K_DOWN:           # if user hits up key
            y += 3                          # move rectangle down

    
    display.fill(pygame.Color('black'))                                 # fill display with background color
    pygame.draw.rect(display,(255, 0, 255), pygame.Rect(x,y,60,60))     # draw rectangle depending on x,y location
    clock.tick(60)                                                      # pause for 1 seconds in between drawing frames (like frames per second)


    pygame.display.update()

pygame.display.quit()