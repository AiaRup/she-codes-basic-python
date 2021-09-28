
def participant_info(*args, **kwargs):
  print(args)
  print(kwargs)

participant_info('Python', 'Web', 'Java', age=7, first_name = 'she', last_name = 'codes')

if 3 == " 3":
   print("Coffee")
elif "six" > "five" and "ball" > "glass":
   print("Dinner")
else:
   print("Sweet")

   height = 89
message = "High enough" if height >= 60 else "Not high enough"
print(message)

def dbl_by_five(x):
   return 5 * x

print(dbl_by_five (3))
print(dbl_by_five (5))
print(dbl_by_five (9))