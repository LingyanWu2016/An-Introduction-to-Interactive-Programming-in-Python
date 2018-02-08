# implementation of card game - Memory

import simplegui
import random
lst1 = range(8)
lst2 = range(8)
lst = lst1+lst2
turns = 0
random.shuffle(lst)
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
# helper function to initialize globals
def new_game():
    global lst,state,first,second,exposed,turns    
    exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(lst)
    state = 0
    first = -1
    second = -1
    turns = 0
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global exposed,lst,turns
    global first
    global second
    
    if state == 0:
        if exposed[pos[0]//50] == False:
            exposed[pos[0]//50] = True
            state = 1
            first = pos[0]//50
    elif state == 1:
        if exposed[pos[0]//50] == False:
            exposed[pos[0]//50] = True
            state = 2
            second = pos[0]//50
    else:
        turns += 1
        label.set_text("Turns = "+str(turns))
        if exposed[pos[0]//50] == False:
            exposed[pos[0]//50] = True
            state = 1
            if lst[first] != lst[second]:
                exposed[first] = False
                exposed[second] = False
            first = pos[0]//50

    
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if exposed[i] == True:
            pos = [50*i+17,60]
            canvas.draw_text(str(lst[i]),pos,40,'White')
        else:
            canvas.draw_polygon([[i*50,0],[(i+1)*50,0],[(i+1)*50,100],[i*50,100]],1,'Red','Green')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

