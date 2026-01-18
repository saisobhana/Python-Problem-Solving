import random
number_to_guess = random.randint(1,50)
while True:
    try:
        guess_number = int(input("Enter any number between 1 and 50:-"))
        if guess_number < number_to_guess:
            print("Too Low!")
        elif guess_number > number_to_guess:
            print("Too High!")
        else:
            print("you guessed it right!")
            break
    except ValueError:
        print("Please enter a valid number")
