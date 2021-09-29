import functools

# exercise 1


def isAnagram(s: str, t: str) -> bool:
  if len(s) != len(t):
    return False
  for char in s:
    if s.count(char) != t.count(char):
      return False
  else:
    return True


# exercise 2
roman_letters = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}


def roman_to_int(s: str) -> int:
  i = 0
  result = 0
  while i < len(s):
    if i + 1 < len(s) and s[i:i+2] in roman_letters:
      result += roman_letters[s[i:i+2]]
      i += 2
    else:
      result += roman_letters[s[i]]
      i += 1
  return result


print(roman_to_int('MCMXCIV'))

# exercise 3


def plus_one(digits):
  num = int(''.join(str(x) for x in digits))
  return [int(x) for x in str(num + 1)]
