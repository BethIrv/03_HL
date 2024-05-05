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


# Guessing Loop

# random number
secret = 7

# existing parameters
low_num = 0
high_num = 10
guesses_allowed = 5

# set guesses at each round
guesses_used = 0

guess = ""
while guess != secret and guesses_used < guesses_allowed:

    # asks the user to guess the number
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # checks user doesn't want to quit
    if guess == "xxx":
        # set end_game to use so that outer loop can be broken
        end_game = "yes"
        break

    # add one to guesses used
    guesses_used += 1

    # if there's one guess left,
    if guess < secret and guesses_used < guesses_allowed:
        feedback = (f"Too low, Please try a higher number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")
    elif guess > secret and guesses_used < guesses_allowed:
        feedback = (f"Too high, Please try a lower number. "
                    f"You've used {guesses_used} / {guesses_allowed} guesses")

    # when the secret number has been guessed
    elif guess == secret:
        if guesses_used == 1:
            feedback = "🎉🎉 Lucky! You got it on the first try. 🎉🎉"
        elif guesses_used == guesses_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done! You guessed the secret number in {guesses_used} guesses."

    # if there are no guesses left!
    else:
        feedback = "🤦‍♀️🤦‍♀️ Sorry - You ran out of guesses. You lose this round 🤦‍♀️🤦‍♀️"
        guesses_used = guesses_allowed + 1

    # print feedback to user
    print(feedback)

    # Additional Feedback (warn user that they are running out of guesses)
    if guesses_used == guesses_allowed - 1:
        print("\n💣💣 Careful - You have one guess left! 💣💣\n")

print()
print("End of Round")
