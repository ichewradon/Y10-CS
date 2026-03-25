import random

number = random.randint(1,101)
guess = 0

while guess != number:
    guess = int(input("Guess a number and I'll say higher or lower."))
    if guess < number:
        print("The number is higher")
    elif guess > number:
        print("The number is lower")
    else:
        print(f"The number is {guess}!")
