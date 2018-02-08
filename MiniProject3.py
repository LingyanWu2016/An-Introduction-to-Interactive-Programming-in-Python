# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
total_stop = 0
good_stop = 0
isRunning = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t<600:   #less than 1 min
        A = 0
        BC = t/10
        D = t%10
    elif t<10:    #less than 1 sec
        A = 0
        BC = 0
        D = t
    else:
        A = t/600
        BC = t%600/10
        D = t%600%10
    return str(A)+":"+BC_format(BC)+"."+str(D)

def BC_format(bc):
    if bc<10:
        return "0"+str(bc)
    else:
        return str(bc)

def stops():
    return str(good_stop)+"/"+str(total_stop)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global isRunning
    isRunning = True
    timer.start()
    
def stop_button():
    global isRunning
    global good_stop
    global total_stop
    global time
    
    isRunning = False
    total_stop += 1
    timer.stop()
    
    if time%10 == 0:
        good_stop += 1
    
def reset_button():
    global time
    global isRunning
    global good_stop
    global total_stop
    
    time = 0
    isRunning = False
    good_stop = 0
    total_stop = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    if time>6000:
        timer.stop()

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),(150,200),20,'red')
    canvas.draw_text(stops(),(220,200),20,'white')
# create frame

#frame = simplegui.create_frame("Stop Watch",400,400)
frame = simplegui.create_frame("Stop Watch", 400, 400)
timer = simplegui.create_timer(100,timer_handler)
                     
# register event handlers
frame.set_draw_handler(draw)
                     
frame.add_button("Start",start_button)                    
frame.add_button("Stop",stop_button)
frame.add_button("Reset",reset_button)

# start frame
frame.start()
