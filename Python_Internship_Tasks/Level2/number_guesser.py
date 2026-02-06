import random

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

number = random.randint(start, end)

while True:
    guess = int(input("Enter your guess: "))
    
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct Guess!")
        break
