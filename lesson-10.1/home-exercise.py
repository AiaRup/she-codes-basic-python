from random import randint
import string


def cows_and_bulls(real, guess):
  bools = 0
  hits = 0
  for i, x in enumerate(real):
    if x in guess:
      if i == guess.find(x):
        bools += 1
      else:
        hits += 1
  return {'bools': bools, 'hits': hits}


# print(cows_and_bulls('abcde', 'acdzr'))
# print(cows_and_bulls('abcde', 'abdzr'))


def game_on():
  letters = string.ascii_lowercase
  random_word = ''
  guess = ''
  result = {'bools': 0, 'hits': 0}
  for i in range(5):
    random_word = random_word + letters[randint(0, len(letters) - 1)]
  print(random_word)
  while result['bools'] < 5:
    while len(guess) < 5 or guess == '' or not guess.isalpha():
      guess = input('Please enter a 5 letter word:')
    result = cows_and_bulls(random_word, guess)
    print(f'Your guess results are {result}')
    guess = ''
    if (result['bools'] == 5):
      print('Yow win')
      break


game_on()
