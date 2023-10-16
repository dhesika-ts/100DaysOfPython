# import colorgram
#
# color_list=colorgram.extract('image.jpg',20)
# color_rgb=[]
#
# for i in range(len(color_list)):
#     cl = []
#     print(i)
#     for j in range(3):
#         cl.append(color_list[i].rgb[j])
#     color_rgb.append(tuple(cl))
import random
import turtle
from turtle import Turtle,Screen
color_list=[(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 232, 237), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94), (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79), (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35)]
turtle.colormode(255)
my_turtle=Turtle()
my_turtle.speed("fastest")
my_turtle.hideturtle()
my_turtle.penup()
my_turtle.setheading(225)
my_turtle.forward(300)
my_turtle.setheading(0)

for row in range(10):
    for column in range(10):
        my_turtle.pendown()
        my_turtle.dot(20,random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)

    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.setheading(0)

my_screen=Screen()
my_screen.exitonclick()