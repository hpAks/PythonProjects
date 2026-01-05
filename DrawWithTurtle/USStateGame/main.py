import turtle

import pandas

guessed_state = []

screen = turtle.Screen()
screen.title("U.S. States Game")

data_dict = pandas.read_csv("50_states.csv")
state_col = data_dict["state"].to_list()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
go_on = True
while go_on:
    answer_input = screen.textinput(title=f"{len(guessed_state)}/50 states correct:",prompt="Whats another state name?").title()

    if answer_input in state_col:
        state_info = data_dict[data_dict.state == answer_input.title()]
        guessed_state.append(answer_input)
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(float(state_info.x.item()), float(state_info.y.item()))
        state_turtle.write(state_info.state.item())
        if len(guessed_state) == 50:
            go_on = False
            turtle.write("You Won!!",False, "center",("Arial",25,"bold"))
    elif answer_input == "Exit" :
        result_state = [ state for state in state_col if state not in guessed_state]

        data_frame = pandas.DataFrame(result_state)
        data_frame.to_csv("result.csv")
        go_on = False


