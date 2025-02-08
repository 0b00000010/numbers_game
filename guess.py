import random
def main():
    
    guess = None
    Attempts = 0
    print("Welcome to the Random Number's Game!")
    min = int(input("Choose your minimum number "))
    max = int(input("Choose your maximum number "))
    number = random.randint(min,max)
    print("The program has chosen a number between " + str(min) + " and " + str(max) + " Can you guess it?")
    
    while guess != number: # keep asking the user for guesses until they guess correctly
        try:
            guess = int(input("Make a guess between "+ str(min) + " and " + str(max) +": "))
        except ValueError:
            print("That's not a number. Try again.")
            continue
        Attempts = Attempts+1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("You guessed it!")
            print("You guessed in "+ str(Attempts))
            break

# Python convention for running the program
if __name__ == "__main__":
    main()