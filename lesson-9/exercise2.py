from random import randint

# Code Academy
# guesses_left = 3
# # Start your game!

# while guesses_left > 0:
#   guesses_left -= 1
#   guess = int(raw_input("Your guess: "))
#   if guess == random_number:
#     print "You win!"
#     break
# else:
#   print "You lose."

def get_user_guess():
  number = input('Please input a number between 1 to 100: ')
  return int(number)

def game_on_version_three():
  random_number = randint(1, 100)
  user_guess = ''
  while user_guess != random_number:
    user_guess = get_user_guess()
    if user_guess < random_number:
      message = 'Your guess is too low'
    elif user_guess > random_number:
      message = 'Your guess is too high'
    print(message)
  else:
    print('You\'ve guessed it right!')

game_on_version_three()