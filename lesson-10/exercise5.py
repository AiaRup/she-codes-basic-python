result = [i * 100 if i % 2 == 0 else i for i in range(1,10)]
print(result)

# option 2
result2 = list(map(lambda x: x * 100 if x % 2 == 0 else x, range(1,10)))
print(result2)