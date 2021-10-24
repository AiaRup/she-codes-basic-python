# exercise 2
"""1."""
person = {}

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

for property, p_type in properties:
  valid_value = None

  while valid_value is None:
    try:
      value = input("Please enter your %s: " % property)
      valid_value = p_type(value)
    except ValueError:
      print("Could not convert %s '%s' to type %s. Please try again." % (property, value, p_type.__name__))

  person[property] = valid_value

"""2."""


def print_list_element(thelist, index):
  try:
    print(thelist[index])
  except IndexError:
    print("The list has no element at index %d." % index)


"""3."""


def add_to_list_in_dict(thedict, listname, element):
  try:
    l = thedict[listname]
  except KeyError:
    thedict[listname] = []
    print("Created %s." % listname)
  else:
    print("%s already has %d elements." % (listname, len(l)))
  finally:
    thedict[listname].append(element)
    print("Added %s to %s." % (element, listname))


# exercise 3
"""1."""
person = {}

properties = [
    ("name", str),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

for property, p_type in properties:
  valid_value = None

  while valid_value is None:
    try:
      value = input("Please enter your %s: " % property)
      valid_value = p_type(value)
    except ValueError as e:
      print(e)

  person[property] = valid_value

"""2."""


def print_list_element(thelist, index):
  try:
    print(thelist[index])
  except IndexError as ie:
    print("The list has no element at index %d." % index)
    raise ie
