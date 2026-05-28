import time, turtle, random
from utils import *
# Section 1: Setup
set_background("park")
s1 = create_sprite("bench",0,-200)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y+7)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor()
    s1.goto(x, y-7)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
    
def move_left():
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x-7, y)
    
def move_right(): 
    x = s1.xcor()
    y = s1.ycor() 
    s1.goto(x+7, y)

window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")



# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

def draw ():
    s1.pendown()
window.onkeypress(draw, "c")

window.onkeypress (stop_drawing, "d")


window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")


# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()