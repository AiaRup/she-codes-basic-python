###### Convert 2 lists into dic
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

sampleDict = dict(zip(keys, values))
print(sampleDict)

###### Merge 2 dic
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

###### New dic from another dic
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

####### Check value inside dic
sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(200 in sampleDict.values())

