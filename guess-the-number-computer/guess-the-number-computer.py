import random


def guess(number_to_guess):
    random_number = random.randint(1, number_to_guess)
    guess = 0
    while guess != random_number:
        guess = int(input(
            f"Try to figure what number is from 1 - {number_to_guess}: "))
        print(guess)
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")

    print(f"Yay, congrats. You've guessed the number {random_number}!")


guess(10)
