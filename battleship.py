import random

def create_board():
    return [['O' for _ in range(10)] for _ in range(10)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ships(board):
    for ship_size in range(5, 1, -1):  # Place ships of sizes 5, 4, 3, 2
        while True:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, 9)
                col = random.randint(0, 10 - ship_size)
                if all(board[row][col + i] == 'O' for i in range(ship_size)):
                    for i in range(ship_size):
                        board[row][col + i] = str(ship_size)
                    break
            else:  # direction == 'vertical'
                row = random.randint(0, 10 - ship_size)
                col = random.randint(0, 9)
                if all(board[row + i][col] == 'O' for i in range(ship_size)):
                    for i in range(ship_size):
                        board[row + i][col] = str(ship_size)
                    break

def get_user_guess():
    while True:
        guess = input("Enter your guess (row column): ")
        try:
            row, col = map(int, guess.split())
            if 0 <= row < 10 and 0 <= col < 10:
                return row, col
            else:
                print("Invalid guess. Row and column must be between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def battleship():
    print("Welcome to Battleship!")
    player_board = create_board()
    computer_board = create_board()

    place_ships(player_board)
    place_ships(computer_board)

    while True:
        print("Your board:")
        print_board(player_board)
        print("Computer's board:")
        print_board(computer_board)

        print("Your turn:")
        player_row, player_col = get_user_guess()
        if computer_board[player_row][player_col] != 'O':
            print("Hit!")
            ship_size = int(computer_board[player_row][player_col])
            computer_board[player_row][player_col] = 'X'
            if all(cell == 'X' for row in computer_board for cell in row if cell == str(ship_size)):
                print("You sank a ship!")
        else:
            print("Miss!")

        if all(cell == 'X' for row in computer_board for cell in row if cell in '2345'):
            print("Congratulations! You sank all of the computer's ships. You win!")
            break

        print("Computer's turn:")
        computer_row = random.randint(0, 9)
        computer_col = random.randint(0, 9)
        if player_board[computer_row][computer_col] != 'O':
            print("The computer hit your ship!")
            ship_size = int(player_board[computer_row][computer_col])
            player_board[computer_row][computer_col] = 'X'
            if all(cell == 'X' for row in player_board for cell in row if cell == str(ship_size)):
                print("One of your ships sank!")
        else:
            print("The computer missed!")

        if all(cell == 'X' for row in player_board for cell in row if cell in '2345'):
            print("Game over! The computer sank all of your ships. You lose!")
            break

if __name__ == "__main__":
    battleship()