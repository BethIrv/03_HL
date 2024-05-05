import math
import random


# checks users have entered yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes or No")


def instruction():
    print('''
    
^^^ Instructions ^^^

To begin with, choose how many rounds you would like. 
To play infinite rounds, simply press <enter>

You can also change your parameters or use default. (Default is 1-100)

You must try to guess the secret number, within your guess limit. 

Enjoy!

    ''')


# checks for an integer with optional upper / lower limits and exit code for infinite mode / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an Integer"

    # if the number needs to be more than an integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = f"Please enter an Integer that is more than / equal to {low}"

    # if the number needs to between low & high
    else:
        error = f"Please enter an Integer that is between {low} and {high} (inclusive)"

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# calculate the maximum number of guesses
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine Starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

print("🎀🎀 Welcome to the Higher Lower Game 🎀🎀")

print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds? (Push <enter> for infinite mode): ",
                       low=1, exit_code="")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5


# allow user to choose the high / low number
else:
    low_num = int_check("Low Number?: ")
    high_num = int_check("High Number?: ", low=low_num + 1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n🎶🎶 Round {rounds_played + 1} (Infinite Mode) 🎶🎶"
    else:
        rounds_heading = f"\n🎶🎶 Round {rounds_played + 1} of {num_rounds} 🎶🎶"

    print(rounds_heading)

    # get the user's choice
    user_choice = input("Choose: ")

    # if the user choice is exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if the user is in infinite mode, increase the rounds
    if mode == "infinite":
        num_rounds += 1

# Game loop ends here

# Game History / Statistics area
