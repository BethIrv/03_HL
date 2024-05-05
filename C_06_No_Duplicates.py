already_guessed = []

secret = 7
guesses_used = 0
guesses_allowed = 5

guess = ""
while guess != secret:
    guess = int(input("Guess: "))

    # checks the guess isn't a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}. You've used "
              f"{guesses_used} / {guesses_allowed} guesses.")
        continue

    # if the guess isn't a duplicate, add it to the list
    else:
        already_guessed.append(guess)

    guesses_used += 1
