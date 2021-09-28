alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dic = {}

def create_Rot_13():
  max_length = len(alphabet)
  for index, letter in enumerate(alphabet):
    if index < max_length/2:
      dic.update({letter: alphabet[index+13], letter.lower(): alphabet[index+13].lower(), alphabet[index+13].lower(): letter.lower(), alphabet[index+13]: letter})
  return dic

def encode_letter(letter):
  return letter if dic.get(letter) is None else dic[letter]

def decode_letter(letter):
  return letter if dic.get(letter) == None else dic[letter]

def decode(word):
  result = ''
  for char in word:
    result = f'{result}{decode_letter(char)}'
  return result

def encode(word):
  result = ''
  for char in word:
    result = f'{result}{encode_letter(char)}'
  return result

print(create_Rot_13())
print(decode('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))
print(encode('I AM LEARNING PYTHON WITH SHE CODES ACADEMY!'))