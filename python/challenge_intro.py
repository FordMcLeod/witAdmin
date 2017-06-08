# CS Challengers Python Challenge

import time # optional import if you wish to have pauses in between dialogue

def main():
    print('Welcome young hero to YEG! We need to defeat the dark forces of evil at all costs')   
    time.sleep(2)                               # allow for pauses in between lines
    print('Please choose your superpower.')
    time.sleep(1)
    
    while True:                                 # validaing input, keep asking user for input until we get what we want
        power = input('ice or fire? ')          # assign our input to variable so we can access it later   
        if power == 'ice' or power == 'fire':   # break out of while loop if we get correct input
            break
    print('Let your adventure begin\n')
    
    dungeon() 
        
def dungeon(): 
    print("Where am I? This forest is so largely dense in trees but at least it's quiet and peaceful in here")
    time.sleep(2)
    print("Ahh I see a zombie looking person over there")
    time.sleep(2)
    
    while True:
        action = input('Should I use my powers or flee? (type in powers or flee)')
        if action == 'powers':
            print('Time to attack with my superpowers')          
            print('Uh oh this zombie is too strong!!!')
            print('The hero is now gone')
            break                                                # end of game for this path
        elif action == 'flee':
            print('Yess I can run way faster than this zombie')
            print('The hero sucessfully escapes')
            # here we would call another function but for this part of the tutorial its just going to loop back again
            
            
main()  # call main function here 






