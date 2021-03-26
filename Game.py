import random
print("NUMBER GUESSING GAME")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9):")
while chances < 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You Won !!!")
    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)
    else:
        print("Your guess was too high: Guess a number lower than", guess)
    chances=chances+1
if chances < 5:
    print("You Lose !!! The number is", number)