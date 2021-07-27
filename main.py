import csv
import pandas
import turtle
import time
import sys

screen = turtle.Screen()
screen.title("Guess the U.S States Game.")
image = ("blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state1 = data.state.to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50", prompt="Whats another state name:- ").title()

    if answer_state == "Exit":
        missing_states = []
        man = [missing_states.append(states) for states in state1 if states not in guessed_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn")
        sys.exit()

    if answer_state in guessed_state:
        tin = turtle.Turtle()
        tin.penup()
        tin.hideturtle()
        tin.write(f"You entered the answer again! You thought you can cheat MUGGLE!", align="center",
                  font=("Courier", 8, "normal"))
        time.sleep(5)
        tin.clear()

    elif answer_state in state1:
        guessed_state.append(answer_state)
        tin = turtle.Turtle()
        tin.penup()
        tin.hideturtle()
        state_data = data[answer_state == data.state]
        tin.goto(int(state_data.x), int(state_data.y))
        tin.write(f"{answer_state}", align="center", font=("Courier", 8, "normal"))

    elif answer_state != state1:
        tin = turtle.Turtle()
        tin.penup()
        tin.hideturtle()
        tin.write(f"That's not the state in U.S", align="center", font=("Courier", 8, "normal"))
        time.sleep(2)
        tin.clear()


turtle.mainloop()
