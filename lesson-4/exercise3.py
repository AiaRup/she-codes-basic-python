from random import randint

def get_user_guess():
  number = input('Please input a number between 1 to 100: ')
  return int(number)

def game_on():
  random_number = randint(1, 100)
  user_guess = get_user_guess()
  message = 'You Won' if user_guess == random_number else 'Oh No! You Lost'
  print(message)

# game_on()

def game_on_version_two():
  random_number = randint(1, 100)
  user_guess = get_user_guess()
  if user_guess < random_number:
    message = 'Your guess is too low'
  elif user_guess > random_number:
    message = 'Your guess is too high'
  else:
    message = 'You\'ve guessed it right!'
  print(message)

game_on_version_two()