import random
def main():
    number = random.randint(1,10)
    guess = None
    print("Welcome to the Random Number's Game!")
    print("The program has chose a number between 1 and 10. Can you guess it?")

    while guess != number: # keep asking the user for guesses until they guess correctly
        try:
            guess = int(input("Make a guess between 1 and 15: "))
        except ValueError:
            print("That's not a number. Try again.")
            continue


        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("You guessed it!")
            break

# Python convention for running the program
if __name__ == "__main__":
    main()