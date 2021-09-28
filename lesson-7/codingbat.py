def string_match(a, b):
  count = 0
  for index, item in enumerate(a):
    if index >= len(a) -1 or index >= len(b):
      break
    if a[index:index+2] == b[index:index+2]:
      count += 1
  return count

print(string_match('xxcaazz', 'xxbaaz'))

# solution
def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0

  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count


### EXERCISE 1
def equal_strings(list):
  result = []
  for item in list:
    if item[0] == item[len(item)-1]:
      result.append(item)

  return result

print(equal_strings(['bb', 'aba', 'abc']))

# solution:

def print_first_and_last_chars_equal_strings(given_strings):
    result = []
    for i in range(len(given_strings)):
        if len(given_strings[i]) >= 2:
            current_string = given_strings[i]
            if current_string[0] == current_string[-1]:
                result.append(given_strings[i])
    print(result)


print_first_and_last_chars_equal_strings(['aba', 'xyz', 'aa', 'x', 'bbb'])
print_first_and_last_chars_equal_strings(['', 'x', 'xy', 'xyx', 'xx'])