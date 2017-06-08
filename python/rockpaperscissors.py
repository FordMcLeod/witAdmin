# Rock Paper scissors demo for python introduction. SciCamps 2017
# Extentions: Add options for lives, an option to ask the player to play again.
# 2 player mode. Add another option besides rock/paper/scissors. etc.

import random
import time

computer = random.randint(0,2)                                          # Let 0 = rock, 1 = paper, 2 = scissors
print("Let's play rock paper scissors!")
time.sleep(1.5)                                                         # Pause in between statements
while True:                                                             # Validate input to make sure user can only type 'y' or 'n'
    instruct = input("Wish to listen to instructions?(y/n) ").lower()   # keep input in lowercase letters
    if instruct == 'y' or instruct == 'n':                              # if we get what we want, break out of while loop
        break
    
if instruct == 'y':
    # These triple quotes let use write more stuff for the print statement in several lines
    print('''In this game you choose rock paper or scissors and hope to beat your opponent's  move.
    Scissors beats paper, paper beats rock, and rock beats scissors. The computer chooses its move 
    based on a random number. You win if your move is successful.''') 
    time.sleep(3)
    
while True:
    player = input("Choose rock,paper, or scissors. (r/p/s)").lower()
    if player == 'r' or player == 'p' or player == 's':
        break
    
if computer == 0:              # if computer choose rock
    if player == 'r':
        print('It is a tie! Computer chose rock')
    elif player == 'p':
        print('You win! Computer chose rock')
    else:
        print('You lose! Computer chose rock')
elif computer == 1:            # if computer chooses paper
    if player == 'r':
        print('You lose! Computer chose paper')
    elif player == 'p':
        print('It is a tie! Computer chose paper')
    else:
        print('You Win! Computer chose paper')
else:                          # if computer chooses scissors
    if player == 'r':
        print('You Win! Computer chose scissors')
    elif player == 'p':
        print('You lose! Computer chose scissors')
    else:
        print('It is a tie! Computer chose scissors')    