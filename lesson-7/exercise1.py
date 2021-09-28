## Exercise 1
def print_stars(num):
  print(num*'*')


def print_upside_down_piramide(num):
  while num != 0:
    print_stars(num)
    num -= 1

def print_range_stars(start, end):
  while start <= end:
     print_stars(start)
     start += 1

def print_rhombus():
  num = 1
  while num < 3:
    print_stars(num)
    num += 1
  while num != 0:
    print_stars(num)
    num -= 1

# print_upside_down_piramide(3)

# print_range_stars(1, 5)
# print_range_stars(5, 8)
print_rhombus()

# solutions

