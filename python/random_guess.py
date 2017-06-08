import random                                               # this allows us to access functions from this library

computer_answer = random.randint(0,10)                      # let computer pick its number from randomly from 0 to 10 (inclusive). A
print('Welcome to the random number guessing game')         # print statement to start the game
print('Player please choose wisely!!!')
answer = input('Choose a number between 0 and 10? ')        # Let user input their number choice

if str(computer_answer) == answer:                          # If the computer's guess is the same as the user's
    print("You chose the right number")
else:                                                       # If not,
    print('Oh no the number was ' + str(computer_answer))   # Also print off the actual answer by concatenating 2 strings