movie = ['The Notebook', 'Maleficent', 'Batman v Superman', 'Black Swan', 'Gone Girl', 'War of the Worlds', 'Just Married']
actor = ['Rachel McAdams', 'Angelina Jolie', 'Gal Gadot', 'Natalie Portman', 'Rosamund Pike', 'Dekota Fanning', 'Brittany Murphy']

movies = dict(zip(movie, actor))
movies2 = { k:v for k,v in zip(movie, actor) }
print(movies)
print(movies2)