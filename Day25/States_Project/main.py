import turtle
import pandas

screen=turtle.Screen()
screen.setup(800,700)
screen.title("India States Game")
image="india_map.gif"
screen.addshape(image)
turtle.Turtle(image)

game_on=True

data=pandas.read_csv("states.csv")
states=data["state"].tolist()
x=data["x"].tolist()
y=data["y"].tolist()
correct_guesses=[]

while game_on:
    answer = screen.textinput(title=f"{len(correct_guesses)}/{len(states)} correct states",
                              prompt="What's the state name?").title()
    for i in range(0,len(states)):
        if states[i]==answer and answer not in correct_guesses:
            turtle_obj = turtle.Turtle()
            turtle_obj.hideturtle()
            turtle_obj.penup()
            turtle_obj.goto(x[i], y[i])
            turtle_obj.write(f"{answer}", align="left", font=('Times New Roman', 10, 'normal'))
            correct_guesses.append(answer)

    if len(correct_guesses)==len(states) :
        game_on=False

    if answer=="Exit":
        not_guessed = []
        for state in states:
            if state not in correct_guesses:
                not_guessed.append(state)
        df = pandas.DataFrame(not_guessed)
        df.to_csv("states_missed.csv")
        screen.bye()

screen.exitonclick()