from turtle import Turtle, Screen
import pandas as pd

# Set up the screen
screen = Screen()
screen.title("U.S States Game")

# Add the U.S. map as a background image
image = "blank_states_img.gif"
screen.bgpic(image)  # Set the background image

# Create turtle for writing state names
t = Turtle()
t.penup()
t.hideturtle()

# Read the CSV file
data = pd.read_csv("50_states.csv")

# Get a list of states from the data
states = data['state'].to_list()

# Track guessed states to prevent duplicates
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess a state's name (or type 'Exit' to quit):"
    )

    if not answer:  # Handle if the user cancels the input
        break

    answer = answer.title()  # Capitalize input

    if answer == "Exit":
        break

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)

        # Get state's x, y coordinates from the CSV
        state_data = data[data['state'] == answer]
        x, y = int(state_data.x.item()), int(state_data.y.item())

        # Display state name at correct coordinates
        t.goto(x, y)
        t.write(answer, align="center", font=("Arial", 8, "bold"))
    else:
        print("Incorrect guess or already guessed.")

# Close the screen when the game ends
screen.mainloop()