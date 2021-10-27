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


def print_top(file_name):
  with open(file_name, "r") as text_file:
    data = text_file. read()
    result = count_word(data)
    sorted_result = [{k: v} for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)]
    for i in range(20):
      for item in sorted_result[i]:
        print(f'{item} {sorted_result[i][item]}')


# print_words("./lesson-12/alice.txt")
print_top("./lesson-12/alice.txt")
