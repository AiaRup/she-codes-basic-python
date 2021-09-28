from datetime import date

def calculate_age(year_of_birth):
    today = date.today()
    return today.year - int(year_of_birth)

def get_initials(name, last_name):
    return '{first}{second}'.format(first=name[0].upper(), second=last_name[0].upper())

def get_user_details():
  name = input('Please enter your name: ')
  last_name = input('Please enter your last name: ')
  year_of_birth = input('Please enter your year of birth: ')

  age = calculate_age(year_of_birth)
  initials = get_initials(name, last_name)
  result = f'your initials are {initials} and your age is {age} years old'
  print(result)

get_user_details()