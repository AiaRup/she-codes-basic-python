result = ['Boom' if i % 7 == 0 else i for i in range(1,100)]
print(result)

# option 2
result2 = list(map(lambda x: 'Boom' if x % 7 == 0 else x, range(1,100)))
print(result2)