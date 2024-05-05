# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        print()
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter Yes / No")


def instruction():
    print('''

^^^ Instructions ^^^

To begin with, choose how many rounds you would like. 
To play infinite rounds, simply press <enter>

You can also change your parameters or use default. (Default is 1-100)

You must try to guess the secret number, within your guess limit. 

Enjoy!

    ''')


# Main routine
print()
print("🎀🎀 Welcome to the Higher Lower Game 🎀🎀")

# loop for testing purposes

print()
want_instructions = yes_no("Would you like to read the instructions?: ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("Program continues")
