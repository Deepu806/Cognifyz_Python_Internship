import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number (1-100): "))
    
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct! You guessed it.")
        break
