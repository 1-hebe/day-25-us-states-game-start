import turtle
import pandas
from write_map import Write_answer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
print(data.state)

more_states = True
state_count = 0
correct_answers = []

while more_states:
    answer_state = screen.textinput(title=f"{state_count}/ 50 States", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in data.values and answer_state not in correct_answers:
        correct_answers.append(answer_state)
        state_count += 1

        answer = (data[data.state == answer_state])

        x = int(answer.x.values[0])
        y = int(answer.y.values[0])
        write_answer = Write_answer()
        write_answer.write(x,y,answer_state)

    elif answer_state in correct_answers:
        print(f"You already answered {answer_state}")
    else:
        print(f"{answer_state} Not a state")
    if state_count == 50:
        print("You got all the states!")
        more_states = False

missed_states = []
for state in all_states:
    if state not in correct_answers:
        missed_states.append(state)
        answer = (data[data.state == state])
        x = int(answer.x.values[0])
        y = int(answer.y.values[0])
        write_missed = Write_answer()
        write_missed.write(x, y, state)

missed_data = pandas.DataFrame(missed_states)
missed_data.to_csv("missed_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

screen.exitonclick()