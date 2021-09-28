def char_freq(char_list):
  freq = {}
  for char in char_list:
    if not char in freq.values():
      freq.update({char: char_list.count(char)})

  return freq

print(char_freq(['a', 'b', 'z', 'z', 'b', 'b']))