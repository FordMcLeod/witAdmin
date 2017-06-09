# original code : https://pythonprogramming.net/displaying-images-pygame/?completed=/pygame-python-3-part-1-intro/

# import modules we need for the game
import pygame
from pygame.locals import *
import time
import random

pygame.init()                       # initialize pygame module
clock = pygame.time.Clock()         # initalize clock for frames per second
pygame.font.init()

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
green = (0,255,0)

pygame.key.set_repeat(20,20)
carImg = pygame.image.load('racecar.png') # load an image from our current directory


def obstacles(x, y, w, h, color):
    pygame.draw.rect(display, color, pygame.Rect(x, y, w, h))

def car(x,y):                         # function for creating the car that takes x,y coordinates
    display.blit(carImg, (x,y))       # place car onto display

def crash():
    global display_width,display_height,black
    font = pygame.font.SysFont('comicsans',115)                 # grab selected font with its size
    message = 'You Crashed!'
    text = font.render(message,True,black)                      # render the font with the message and color to create the text
    text_surface = text.get_rect()                              # get the text's surface to be placed on
    text_surface.center = ((display_width/2),(display_height/2))# position text on center of screen
    display.blit(text, text_surface)                            # put text onto display
    pygame.display.update()
    time.sleep(3)                                               # pause for 3 seconds before game quits
    return None                                                 # return None to help with quitting game
    

def game():
    global x,y,x_change,display_width,car_width
    
    # obstacle variables
    startx = random.randrange(0, display_width)   # start position is random based on screen width size
    starty = -600                                 
    o_speed = 7
    o_width = 100
    o_height = 100
    dodged = 0
    # ---------
    
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
        
        obstacles(startx, starty, o_width, o_height, green) # create obstacles
        starty += o_speed                                   # move obstacles by their speed
        
        if x > display_width - car_width or x < 0: # car collision
            result = crash()                       # call function to start crash sequence
            if result == None:                     # have this just so we can quit game afterwards
                break
            
            
        
        if starty > display_height:
            starty = 0 - o_height
            startx = random.randrange(0,display_width)
            dodged += 1
            o_speed += 1
            o_width += (dodged * 1.2)
            
        if y < starty + o_height:
            if x > startx and x < startx + o_width or x + car_width > startx and x + car_width < startx + o_width:
                result = crash()
                if result == None:
                    break 
                
    
    
        pygame.display.update()          # update display after every iteration
        clock.tick(60)                   # frames per second

    pygame.display.quit()                # quit the game
    
game()