import random

def get_highest_score():
    try:
        with open("highscore.txt", "r") as file:
            high_score = int(file.read())
    except FileNotFoundError:
        high_score = None
    return high_score

def save_highest_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))


print("Welcome to the Guess the Number Challenge!")
print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100)

while True:
    high_score = get_highest_score()
    print(f"Current High Score: {high_score if high_score else 'No high Score yet!'}")

    for attempt in range(1, 8):  # Max 7 attempts
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")

        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempt} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"Game Over! The number was {secret_number}.")
        
        
    if (high_score is None) or (attempt < high_score):
        print("New High Score!")
        save_highest_score(attempt)
    
    
    ex = input("Do you want to play again ? (y/n)")    
    if ex == "" or ex == "y":
        continue
    else:
        break
