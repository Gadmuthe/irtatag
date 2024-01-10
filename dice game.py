import random 
def roll_dice():
    return random.randint(1,6)

def play_game():
    player_score = 0
    computer_score = 0

    for _ in range(3):
        input("Press Enter to roll the dice...")
        player_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"You rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")

        if player_roll > computer_roll:
            print("You win this round!")
            player_score += 1
        elif player_roll < computer_roll:
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

    print("\nFinal Scores:")
    print(f"You: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You win!")
    elif player_score < computer_score:
        print("Computer wins. Better luck next time!")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    print("Let's play a dice game!")
    play_game()