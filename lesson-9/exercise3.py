
# 1
def game_on():
  number = 1
  while number < 51:
    message = 'boom' if number % 7 == 0 else number
    print(message)
    number += 1

# game_on()

#2
def game_on_version_one():
  print('The current number is 1.')
  number = 1
  while number < 20:
    number += 1
    answer = input('Next Number should be: ')
    correct_answer = 'boom' if number % 7 == 0 else str(number)

    if answer != correct_answer:
      print('Sorry! You are wrong!')
      break
  else:
    print('Good job!')


# game_on_version_one()

def game_on_version_two():
  number = 0
  while number < 20:
    is_computer_turn = number % 2 != 0
    number += 1
    correct_answer = 'boom' if number % 7 == 0 else str(number)

    if (is_computer_turn):
      print('Computer- Next Number should be: ' + correct_answer)
    else:
      answer = input('Human- Next Number should be: ')
      if answer != correct_answer:
        print('Sorry! You are wrong!')
        break



  else:
    print('Good job!')

# game_on_version_two()

def bonus():
  number = 0
  while number < 20:
    is_computer_turn = number % 2 != 0
    number += 1
    correct_answer = 'boom' if number % 7 == 0 else str(number)

    if (is_computer_turn):
      print('Computer- Next Number should be: ' + correct_answer)
    else:
      answer = input('Human- Next Number should be: ')
      if answer != correct_answer:
        print('Sorry! You are wrong!')
        break

  else:
    print('Good job!')

bonus()