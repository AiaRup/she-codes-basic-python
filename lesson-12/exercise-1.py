with open("./lesson-12/text.txt", "r") as text_file:
  with open("./lesson-12/reverse.txt", "w") as reverse_file:
    lines = text_file.readlines()
    for line in lines:
      reverse_file.write(line[::-1])
    for line in lines:
      reverse_file.write(line)
