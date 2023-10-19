import turtle
import pandas

count = 0

sc = turtle.Screen()
sc.title("U.S. States Game")
image = "blank_states_img.gif"
sc.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{count}/50 Guess the state",
                                    prompt="Whats the state name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_state]
        t.goto(int(states_data.x.iloc[0]), int(states_data.y.iloc[0]))
        t.write(states_data.state.item())
        count += 1
