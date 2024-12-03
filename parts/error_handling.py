try:
    guess = int(input("Enter your guess: "))
except ValueError:
    print("Invalid input! Please enter a number.")