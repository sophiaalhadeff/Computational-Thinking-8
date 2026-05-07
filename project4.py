from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("saas")

# The goal of this game is to get as many cardinals and turtles on the screen as possible.

# TODO - create at least two variables and set their starting value. ex: cookies = 0
turtle = 0
cardinals = 5

# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()

m2 = create_sprite("alien", -200,-200)
m2.hideturtle()

# Section 2 - controls
# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control

def get_cardinal():
    # Get cardinal basically puts a cardinal on the screen every time someone presses the s key.
    global cardinals
    cardinals +=1
    if cardinals >= 100:
        m1.write (f"Congratulations! You have reached 100 cardinals!")
    x = random.randint (-300,200)
    y = random.randint (-300,200)
    create_sprite("cardinal3" ,x,y)

window.onkeypress(get_cardinal, "s")

def get_turtle():
    # Get turtle basically puts a turtle on the screen every time someone presses the a key.
    global turtle
    turtle +=5
    if turtle >= 200:
        m2.write (f"Congratulations! You have reached 200 turtles!")
    x = random.randint (-300,200)
    y = random.randint (-300,200)
    create_sprite("turtle3" ,x,y)

window.onkeypress(get_turtle, "a")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    time.sleep(0.01)
    window.update()