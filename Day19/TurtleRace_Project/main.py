import turtle
from turtle import Turtle,Screen
import random

my_screen=Screen()
turtle_list=[]
my_screen.setup(width=500,height=400)
turtle_colors=["red","blue","green","yellow","violet","orange"]
turtle_pos=[-75,-45,-15,15,45,75]
user_bet=my_screen.textinput(title="Turtle Race",prompt="Which colour do you want to bet on?")
for i in range(len(turtle_colors)):
    my_turtle=Turtle("turtle")
    my_turtle.color(turtle_colors[i])
    my_turtle.penup()
    my_turtle.goto(-230,turtle_pos[i])
    turtle_list.append(my_turtle)

if user_bet:
    game_on=True
winner=""
while game_on:
    for my_turtle in turtle_list:
        my_turtle.forward(random.randint(1,10))
        if(my_turtle.position()[0]>230):
            winner=my_turtle.color()[0]
            if(winner==user_bet):
                print(f"Congrats,You won!The winner is {winner} turtle.")
            else:
                print(f"Sorry,You lost!The winner is {winner} turtle.")
            game_on=False
            #my_screen.bye()
            break
my_screen.exitonclick()