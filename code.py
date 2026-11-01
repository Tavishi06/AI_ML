import random

def lucky_num():
    lucky_Num = random.randint(1, 100)

    print("Guess the lucky number between 1 and 100!")

    while True:

        guess = input("Enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Your guess is out of range. Please guess between 1 and 100.")
            continue

        if guess < lucky_Num:
            print("Too low! Try again.")

        elif guess > lucky_Num:
            print("Too high! Try again.")

        else:
            print(f"Congratulations! You've guessed the lucky number {lucky_Num}!")
            break

lucky_num()