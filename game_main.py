# TODO 1: Convert the guess to Title case - DONE
# TODO 2: Check if the guess is among the 50 states - DONE
# TODO 3: Write correct guesses onto the map - DONE
# TODO 4: Use a loop to allow the user to keep guessing - DONE
# TODO 5: Record the correct guesses in a list - DONE
# TODO 6: Keep track of the score

import turtle
import pandas
from game_objects import Map
from game_score import TheScore

# Load the data from the CSV file
data = pandas.read_csv("50_states.csv")
states = data.state

# Create an instance of TheScore
displayed_score = TheScore()
# Create an instance of Map
game_map = Map()

# Create the screen object first
screen = turtle.Screen()
screen.title("Merica States Game")
# Set the screen size
screen.setup(width=800, height=600)
# Set the screen color
turtle.Screen().bgcolor("PowderBlue")
# Load and set the shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # To find x and y values for csv file.
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


list = data["state"].to_list()
def user_guess():
    state_list = []
    score = 0

    while score < 50:
        #global user_input

        user_input = screen.textinput(title="Guess the state", prompt="Name a state").title()

        # Confirm if guess was already entered
        if user_input in state_list:
            print("You already guessed this state")
            continue

        # User guesses a state correctly
        elif user_input in list and user_input not in state_list:

            print("yes")
            score += 1

            # Score board
            displayed_score.increase_score()
            # Call the score method
            displayed_score.update_score()


            state_list.append(user_input)
            print(state_list)
            print(f"Your score is: {score}")

            # Retrieve x and y values from entered state
            x_value = data.loc[data['state'] == user_input, 'x'].values[0]
            y_value = data.loc[data['state'] == user_input, 'y'].values[0]

            # Pass user_input to guess_to_map
            map_instance = Map()
            map_instance.guess_to_map(user_input,x_value,y_value)

        else:
            print("That is not a state")
            print(f"Your score is: {score}")

user_guess()


# Call the win method
game_map.win()



# Keep the window open
screen.exitonclick()
