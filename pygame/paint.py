# finished paint code with some extensions built into it

import pygame
import time
import random
from pygame.locals import *
    
drawing = False
erased = False
brush_radius = 10
brush_center = (0,0)


pygame.init() # initalizes the pygame module
title = 'Paint'
size = (1000,1000)
display = pygame.display.set_mode(size,0,0) # creates window
pygame.display.set_caption(title) # creates title of game
pygame.key.set_repeat(20,20) # allows for holding down keys

while True:
    event = pygame.event.poll()
    if event.type == QUIT:
        break
    elif event.type == MOUSEBUTTONDOWN:
        brush_center = event.pos 
        color = (random.randrange(256),random.randrange(256),random.randrange(256))
        pygame.draw.circle(display,color,brush_center,brush_radius)
        drawing = True
    elif event.type == MOUSEBUTTONUP:
        drawing = False
    elif event.type == MOUSEMOTION:
        if drawing:
            pygame.draw.circle(display,color,event.pos,brush_radius)
            
    elif event.type == KEYDOWN:
        if event.key == K_BACKSPACE :
            erased = True
            if erased:
                display.fill(pygame.Color('black'))
                erased = False
        if event.key == K_KP_PLUS:
            brush_radius += 3
        if event.key == K_KP_MINUS:
            if brush_radius > 0:
                brush_radius -= 3
            else:
                brush_radius = 3
           
    pygame.display.update()
    
pygame.display.quit()