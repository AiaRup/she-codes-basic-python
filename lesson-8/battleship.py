from random import randint

board = []
board_size = 5
number_of_guesses = 4


def create_board(board, size):
  for x in range(size):
    board.append(["O"] * size)


def print_board(board):
  for row in board:
    print(" ".join(row))


def random_row(board):
  return randint(0, len(board) - 1)


def random_col(board):
  return randint(0, len(board[0]) - 1)


# create the board for the game
create_board(board, board_size)

# get random location of battleship
ship_row = random_row(board)
ship_col = random_col(board)


def game_on():
  for turn in range(number_of_guesses):
    print_board(board)
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      print("Congratulations! You sunk my battleship!")
      break
    else:
      if (guess_row < 0 or guess_row > board_size) or (guess_col < 0 or guess_col > board_size):
        print("Oops, that's not even in the ocean.")
      elif(board[guess_row][guess_col] == "X"):
        print("You guessed that one already.")
      else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
      turn += 1

      if turn == number_of_guesses:
        print("Game Over")
        print_board(board)


game_on()
