import pygame
import time
import random
import sys


pygame.init()

print(pygame.font.get_fonts())
# variables to change characteristics of game
display_width = 800
display_height = 600
close = False
black = (0,0,0)
white = (255,255,255)
red = (255,0,0) 
block_color = (255,115,0) # change rgb values for color
car_width = 73
# ------------------------- #

# create game display
gameDisplay = pygame.display.set_mode((display_width,display_height)) # change screen size
pygame.display.set_caption('Dodge') # change title of game
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.png') # change image here (make sure its in same folder as this file)
pygame.key.set_repeat(20, 20) # helps with key lag
#------------------------------------------#

def blocks_dodged(count):
    font = pygame.font.SysFont(None, 25) # initalize font object
    text = font.render("Dodged: "+ str(count), True, black)
    gameDisplay.blit(text,(0,0))

def blocks(blockx, blocky, blockw, blockh, color):
    # draw blocks onto display
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

def car(x,y):
    # render car image onto display
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, block_color) # create rectangular surface for fon
    return textSurface, textSurface.get_rect() # get rectangular area of surface to place font on

def message_display(text):
    # create and render message on screen
    font_object = pygame.font.Font(None,115) # create font object 
    text, text_surface = text_objects(text, font_object) # create text and surface to render on
    text_surface.center = ((display_width/2),(display_height/2)) # set text location
    gameDisplay.blit(text, text_surface) # render text on screen

    pygame.display.update()

    time.sleep(2)
    pygame.quit() # quit pygame module
    sys.exit() # exit window
    
def crash():
    message_display('Crashed')
    
def game():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    block_startx = random.randrange(0, display_width)
    block_starty = -600
    block_speed = 4 # change starting speed of block
    block_width = 100 # change size of block
    block_height = 100

    dodged = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5 # change car speed
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        
        # create and draw blocks with their position and size
        blocks(block_startx, block_starty, block_width, block_height, block_color)

        block_starty += block_speed # change block posiion using speed
        car(x,y)
        blocks_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if block_starty > display_height:
            block_starty = 0 - block_height
            block_startx = random.randrange(0,display_width)
            dodged += 1
            block_speed += 1
            block_width += (dodged * 1.2)

        if y < block_starty + block_height: # check for collisions
            if x > block_startx and x < block_startx + block_width or x+car_width > block_startx and x + car_width < block_startx+block_width:
                crash()
        
        pygame.display.update()
        clock.tick(60)

        
game()


