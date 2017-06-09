# Introduction tutorial for paint game for scicamps 2017
# uses pygame module to create a visual simulation of the paint program
# some extensions are found in paint.py

# all the things we need to code this game
import pygame 
import time
import random
from pygame.locals import * 
# -------------------------------- #
    
# game setup ------------- #
pygame.init()                                  # initalizes the pygame module
title = 'Paint'
size = (700,600)                               # size of window
display = pygame.display.set_mode(size,0,0)    # creates window
pygame.display.set_caption(title)              # creates title of game
# game setup --------------#


# game variables ---------------#
drawing = False                 # should the brush be drawing on the screen?
erased = False                  # has the screen been erased?
brush_radius = 10               # radius of the brush 
brush_center = (0,0)            # where the brush is on the screen
color = (255,0,0)               # color of the brush
# ------------------------------#

while True:                     # game loop that goes on forever until user clicks close button
    event = pygame.event.poll() # get a single pygame event
    if event.type == QUIT:      # if user clicks the close button
        break                   # get out of game loop
    
    elif event.type == MOUSEBUTTONDOWN:
        brush_center = event.pos                                    # place brush's center where the mouse pointer is
        pygame.draw.circle(display,color,brush_center,brush_radius) # draw circle on screen
        drawing = True                                              # keep on drawing
        
    elif event.type == MOUSEBUTTONUP:
        drawing = False                                             # stop drawing
    
    elif event.type == KEYDOWN:                         # if we hold a key down
        if event.key == K_BACKSPACE :                   # if we press the backspace key 
            erased = True                               # let program know we want to erase screen
            if erased:                                  # if we wish to erase screen
                display.fill(pygame.Color('black'))     # fill display with the background color
                erased = False                          # we do not wish to erase screen anymore
    
    
    pygame.display.update()     # update the game every iteration
    
pygame.display.quit()           # quit game

