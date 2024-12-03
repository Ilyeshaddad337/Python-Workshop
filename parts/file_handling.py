attempt = 0
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = None

print(f"Current High Score: {high_score if high_score else 'No high score yet!'}")

# After the game
if (high_score is None) or (attempt < high_score):
    print("New High Score!")
    with open("highscore.txt", "w") as file:
        file.write(str(attempt))