
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
import math
# helper function to start and restart the game
choose_range=100
used = 0
limit = int(math.ceil(math.log(choose_range,2)))
def new_game():
    # initialize global variables used in your code here
    global secret_number   
    global limit    
    limit = int(math.ceil(math.log(choose_range,2)))
    secret_number = random.randrange(0,choose_range)
      
    print " "
    print "New game,range(0,"+str(choose_range)+")"
    print "I'm ready.Now you guess my secret number."
    print "You have "+str(limit)+" guesses left."

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    global choose_range
    choose_range=100  
    print ""
    print "you have chosen range:0-100.Game will now restart."
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    global choose_range
    choose_range = 1000
    print ""
    print "you have chosen range:0-1000.Game will now restart."
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global limit
    global used
    guess_number = int(guess)
   
    print "Guess was "+str(guess_number)
    
    limit -= 1
    used += 1
    
    if guess_number == secret_number:
        print "Correct!You got me in "+str(used)+" guesses."
        new_game()
    else:
        if guess_number > secret_number:
            print "Lower"
            print "Your remaining guesses is "+str(limit)
        else:
            print "Higher"
            print "Your remainging guesses is "+str(limit)
        if limit==0:
            print "You failed to guess my secret number.The answer should be "+str(secret_number)
            new_game()

    
# create frame
frame = simplegui.create_frame("Guess Number",200,200)
frame.add_button("range100",range100)
frame.add_button("range1000",range1000)
frame.add_input("enter a number",input_guess,200)

# register event handlers for control elements and start frame
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric