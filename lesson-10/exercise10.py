languages = ['HTML', 'JavaScript', 'Python', 'Ruby']

result = list(filter(lambda x: x == 'Python', languages))
print(result)

# option 2
result2 = [i for i in languages if i == 'Python']
print(result2)