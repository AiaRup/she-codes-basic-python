joules = [5000, 8000, 10000, 6000, 12000]

result = [(i,i/4184) for i in joules]
print(result)

# option 2
result = list(map(lambda i: (i,i/4184),joules))
print(result)

# option 3
result = [(j, cal) for (j, cal) in zip(joules, [j/4184 for j in joules])]
print(result)
