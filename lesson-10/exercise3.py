movie = ['The Notebook', 'Maleficent', 'Batman v Superman', 'Black Swan', 'Gone Girl', 'War of the Worlds', 'Just Married']
actor = ['Rachel McAdams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman', 'Rosamund Pike', 'Dekota Fanning', 'Brittany Murphy']

dict(zip(movie, actor)).items()

result = [f'{m} is played by {a}' for m,a in dict(zip(movie, actor)).items()]
print(result)