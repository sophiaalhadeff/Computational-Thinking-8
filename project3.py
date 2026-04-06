from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -250
y1 = 200
x2 =-200
y2 = 70
x3 = -250
y3 = -60
x4 = -250
y4 = -230


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("bahamas")
t1 = create_sprite("puppy",x1,y1)
t2 = create_sprite("cardinal",x2,y2)
t3 = create_sprite("puppy",x3,y3)
t4 = create_sprite("cardinal",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
# # Sprite 3 could win because it's speed is 15, but sprite 4 could also win because it's speed is anywhere from 10-30.
for i in range(20):
    x1 += 5
    x2 += 10
    x3 += 15
    x4 += random.randint ( 10,30)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)    
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
s5 = create_sprite("fox",-200,-200)
if x3 >= x2 and x3 >= x1 and x3 >= x4:
    s5.write("Player 3 wins!")
elif x4 >= x2 and x4 >= x1 and x4 >= x3:
    s5.write("Player 4 wins!")


turtle.exitonclick() 