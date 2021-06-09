import turtle
import pandas


screen = turtle.Screen()
screen.title(" US STATES GAME")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_coordinates = data["x"].to_list()
y_coordinates = data["y"].to_list()
guessed_states=[]


while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Whats another state's name?").title()
    if answer == "Exit":
        missed_states = {
            "Missed": []
        }
        for s in states:
            if s not in guessed_states:
                missed_states["Missed"].append(s)

        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)



