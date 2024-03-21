import random
def generate_random_number():
    return random.randint(1, 100)
def compare_numbers(guess, target):
    return guess - target
def is_valid_input(user_input):
    return user_input.isdigit()
def main():
    target_number = generate_random_number()
    max_guesses = 5
    num_guesses = 0

    print("Welcome to the guessing game! I've chosen a number between 1 and 100. Can you guess it?")
    while num_guesses < max_guesses:
        user_guess = input("Enter your guess: ")
        if not is_valid_input(user_guess):
            print("Please enter a valid number.")
            continue
        user_guess = int(user_guess)
        difference = compare_numbers(user_guess, target_number)
        if difference == 0:
            print("Congratulations! You guessed the number correctly!")
            break
        else:
            num_guesses += 1
            if difference > 0:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
            print(f"You have {max_guesses - num_guesses} guesses left.")
    if num_guesses == max_guesses:
        print(f"Sorry, you've run out of guesses. The correct number was {target_number}.")

    main()