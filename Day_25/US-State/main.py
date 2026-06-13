import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. State")
image = 'states_img.gif'
screen.addshape(image)
t.shape(image)

data = pd.read_csv('Us_states.csv')
count_state = len(data['state'])
all_states = data['state']
correct_state = 0
guessed_states = []

while correct_state != count_state:
    answer_state = screen.textinput(
        title=f'{correct_state}/{count_state} States Correct',
        prompt="What's another state's name?"
    )

    if answer_state is None or answer_state.lower() == 'exit':
        missed_states = [state for state in allstates if state not in guessed_states]
        data_dict = {
            "states": missed_states
        }
        file = pd.DataFrame(data_dict)
        file.to_csv('missed_states.csv')
        break

    answer_state = answer_state.title()
    result = data.query(f"state == '{answer_state}'")
    if not result.empty:
        guessed_states.append(answer_state)
        turtle = t.Turtle()
        turtle.hideturtle()
        turtle.penup()
        x_value = data.loc[data['state'] == answer_state, 'x'].values[0]
        y_value = data.loc[data['state'] == answer_state, 'y'].values[0]
        turtle.goto(x_value, y_value)
        turtle.write(answer_state)
        correct_state += 1