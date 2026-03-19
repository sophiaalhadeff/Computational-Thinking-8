fall_points = 0
summer_points = 0
winter_points = 0

print("Hi! Welcome to the season quiz! Answer each question with an A, B, or C.")
input()
print("Let's get started!")
input()

answer1 = input("What is your favorite drink  A pumpkin spice latte, B lemonade, or C hot chocolate?   ") 
if answer1 == "A" or answer1 == "a":
     fall_points += 1
elif answer1 == "B" or answer1 == "b":
    summer_points += 1
elif answer1 == "C" or answer1 == "c":
    winter_points += 1

answer2 = input("What is your favorite weather A crisp and cool, B sunny and bright, or C snowing?     ")
if answer2 == "A" or answer2 == "a":
    fall_points += 1
elif answer2 == "B" or answer2 == "b":
    summer_points += 1
elif answer2 == "C" or answer2 == "c":
    winter_points += 1

answer3 = input("What is your favorite activity A leaf art, B hanging out on the beach, or C skiing/snowboarding?   ")
if answer3 == "A" or answer3 == "a":
    fall_points += 2
elif answer3 == "B" or answer3 == "b":
    summer_points  += 2
elif answer3 == "A" or answer3 == "c":
    winter_points += 2

answer4 = input("What is your favorite animal A squirrel, B dragonflies, or C polar bears?    ")
if answer4 == "A" or answer4 == "a":
    fall_points += 1
elif answer4 == "B" or answer4 == "b":
    summer_points += 1
elif answer4 == "C" or answer4 == "c":
    winter_points += 1
    
answer5 = input("What is your favorite type of shoe, A sneaker, B sandal, or C boot?")
if answer5 == "A" or "a":
    fall_points += 1
elif answer5 == "B" or "b":
    summer_points += 1
elif answer5 == "C" or "c":
    winter_points += 1

print(f"Your score is {fall_points} fall, {summer_points} summer, and {winter_points} winter!")

if fall_points > winter_points and fall_points > summer_points:
    print ("Based on this survey you are a fall person!")
if winter_points > summer_points and winter_points > fall_points:
    print ("Based on this survey you are a winter person!")
if summer_points > fall_points and summer_points > winter_points:
    print ("Based on this survey you are a summer person!")
