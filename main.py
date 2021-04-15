from turtle import Turtle,Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Please Make Your Bet", prompt="Which Turtle Will win the Race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -70, -40, -10, 30, 60]
all_turtle = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user_input:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_input == winning_color:
                print(f"You Have Won! The Winning Color is {winning_color}")
            else:
                print(f"You Loose! The Winning Color is {winning_color}")

        turtle.forward(random.randint(0, 10))




screen.exitonclick()