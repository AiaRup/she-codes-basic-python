from random import randint
import urllib.request

def download_image():
  random_number = randint(1, 1000)
  file_location = '{name}.png'.format(name=random_number)
  url = 'https://images.unsplash.com/photo-1591154669695-5f2a8d20c089?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=934&q=80'
  urllib.request.urlretrieve(url, file_location)


download_image()