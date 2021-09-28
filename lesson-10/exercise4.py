result = [i * 100 for i in range(1,10) if i % 2 == 0]
print(result)

# option 2
result2 = list(map(lambda x: x * 100, list(filter(lambda i: i % 2 == 0, range(1,10)))))
print(result2)