from turtle import Turtle, Screen
import random

is_race_on= False
screen = Screen()
screen.setup(width=500, height=400)
user_bet=screen.textinput(title= "Make your bet", prompt='Which turtle will win the race? Enter a color: ["red", "yellow", "green", "orange", "blue", "purple"]')
color=["red", "yellow", "green", "orange", "blue", "purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0, 6):
    _turtle = Turtle(shape="turtle")
    _turtle.penup()
    _turtle.color(color[turtle_index])
    _turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(_turtle)
if user_bet:
    is_race_on=True   

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on= False
            winner= turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
                
        rand_dist= random.randint(0, 10)
        turtle.forward(rand_dist)
    
screen.exitonclick()
