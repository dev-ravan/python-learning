import random

secretNum = random.randint(1, 5)
guessCount = 0

while True:
        guessNum = int(input("Guess the secret number (1-100): "))
        guessCount += 1
        
        if secretNum == guessNum:
            print(f"You win! You guessed it in {guessCount} tries.")
            break
        elif guessNum < secretNum:
            print("Too low. Try again!")
        else:
            print("Too high. Try again!")
