import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
IMAGE = "blank_states_img.gif"
screen.setup(width=734, height=862)
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("all_states.csv")
all_states = data.state.to_list()

guessed_states = []
missed_states = []

while len(guessed_states) < 33:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States/UT Correct",
                                    prompt="What's another state's/UT's name?").title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missed_states).to_csv("States_missed.csv")
        break

