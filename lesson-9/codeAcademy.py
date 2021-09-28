
# enumerate
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
  print(index+1, item)

# zip

# It’s also common to need to iterate over two lists at once. This is where the built-in zip function comes in handy.

# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

# zip can handle three or more lists as well!

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  # Add your code here!
  if a > b:
    print(a)
  else:
    print(b)

# Practice
def is_even(x):
  return x % 2 == 0

########################

def is_int(x):
  if int(x) == x:
    return True
  else:
    return int(abs(x)) - abs(x) > 0

########################

def digit_sum(n):
  sum = 0
  for number in str(n):
    sum += int(number)
  return sum

def factorial(x):
  result = 1
  for i in range(1, x+1):
    result *= i
  return result

########################

def is_prime(x):
  if x == 0 or x == 1 or x < 0:
    return False
  for n in range(2, x - 1):
    if x % n == 0:
      return False
  else:
    return True

########################

def reverse(text):
  result = []
  for char in text:
    result.insert(0, char)
  return ''.join(result)

########################

def anti_vowel(text):
  vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
  result = ''
  for char in text:
    if char not in vowel:
      result = result + char
  return result

########################

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
  result = 0
  for char in word:
    result += score[char.lower()]
  return result

########################

def censor(text, word):
  return text.replace(word, '*'*len(word))

########################

def count(sequence, item):
  result = 0
  for i in sequence:
    if item == i:
      result += 1
  return result

########################

def purify(list):
  result = []
  for item in list:
    if item % 2 == 0:
      result.append(item)
  return result

########################

def product(list):
  result = 1
  for num in list:
    result = result * num
  return result

########################

def remove_duplicates(list):
  result = []
  for item in list:
    if item not in result:
      result.append(item)
  return result

########################

def median(list):
  sorted_list = sorted(list)
  middle = int(len(list) / 2)
  if len(list) % 2 != 0:
    return sorted_list[int(round(middle))]
  else:
    return (sorted_list[middle] + sorted_list[middle-1])/2.0