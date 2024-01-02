import random

def roll_dice():
    print("Rolling the dice...")
    result = random.randint(1, 6)
    print(f"The dice shows: {result}")

roll_dice()