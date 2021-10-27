def print_words(file_name):
  with open(file_name, "r") as text_file:
    data = text_file. read()
    result = count_word(data)
    sorted_result = sorted(result.keys())
    for i in sorted_result:
      print(i, result[i])
  return sorted_result


def count_word(full_text):
  result = {}
  for word in full_text.split():
    if word.lower() not in result:
      wordCount = 0
      wordCount += full_text.count(word.lower())
      wordCount += full_text.count(word.upper())
      wordCount += full_text.count(word.capitalize())
      result.update({word.lower(): 1 if wordCount == 0 else wordCount})
  return result


print_words("./lesson-12/alice.txt")
