# updated extentions for random number guessing game

import random

def checkanswer():
    while True:
        guess = input("Please guess the correct number from 0 to 100: ")
        try:
            guess = int(guess)
            if (guess in range(0,101)):
                return guess
        except:
            print("guess again")
            
lives = 5
computer_guess = random.randint(0,100)
print("Welcome to Owen, Kynan, and Monica's random number guessing game")
while True:
    print("Your lives " + str(lives))
    our_guess = checkanswer()
    if (lives == 0 and (our_guess != computer_guess)):
        print("You lose the number was " + str(computer_guess))
        break
    if (our_guess == computer_guess):
        print("You are correct YESSSS")
        break    
    elif (our_guess < computer_guess):
        print("too low")
        lives -= 1  
    elif (our_guess > computer_guess):
        print("too high")
        lives -= 1
               
   