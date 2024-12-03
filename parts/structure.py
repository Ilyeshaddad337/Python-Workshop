print("Welcome to the Guess the Number Challenge!")
print("I'm thinking of a number between 1 and 100.")
secret_number = 56
while True:
    for attempt in range(1, 8):  # Max 7 attempts
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempt} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Game Over! The number was {secret_number}.")
        
    ex = input("Do you want to play again ? (y/n)")
    if ex == "" or ex == "y":
        continue
    else:
        break
