import random
import turtle as t


def get_turn_size():
    turn_size = input('Enter turn size( wide,square,narrow): ')
    return turn_size 

def get_line_length():
    choice = input('Enter line length (long,medium,short): ').lower()
    if choice == 'long':
        line_length = 250
    elif choice == 'medium':
        line_length = 200
    elif choice == 'short':
        line_length = 100
    return line_length

def get_line_width():
    choice = input('Enter line length (super,regular,thin): ').lower()
    if choice == 'super':
        line_width = 40
    elif choice == 'regular':
        line_width = 25
    elif choice == 'thin':
        line_width = 10
    return line_width


def inside_window():
    left = (-t.window_width() / 2) + 100
    right = (t.window_width() / 2) - 100
    top = (t.window_height() / 2) - 100
    bottom = (-t.window_height() / 2) + 100
    (x,y) = t.pos()
    inside = left < x < right and bottom < y < top
    return inside


def move_turtle(line_length,turn_size):
    # extension: could change it to rgb instead
    # t.colormode(255)
    # red = random.randint(0,255)
    # blue = random.randint(0,255)
    # green = random.randint(0,255)
    # t.pencolor(red,blue,green)
    
    # extension: add stamps to our turtle. Add folowing code under pencolor 
    # t.fillcolor(random.choice(pen_colors)) or use above example
    # t.shapesize(3,3,1)
    # t.stamp()
    
    # extention: replace code underneath inside_window() but keep t.right,t.forward, and the else clause 
    # if turn_size == 'wide':
    #      angle = random.randint(120,150)
    # elif turn_size == 'square':
    #      angle = random.randint(80,90)
    # elif turn_size == 'narrow':
    #      angle = random.randint(20,40)
    
    colors = ['red','orange','yellow','green','blue','purple']
    t.pencolor(random.choice(colors))   
    # uncomment for use on extension 2: t.fillcolor(random.choice(colors))
    if inside_window():
        angle = random.randint(0,180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)



# extention change pensize and move_turtle argument to random.randint(0,somenumber)

line_width = get_line_width()
line_length = get_line_length()
turn_size = get_turn_size()
t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('fastest')
t.pensize(line_width) # line_width 

while True:
    move_turtle(line_length,turn_size) # line_length