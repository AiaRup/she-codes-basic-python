import datetime


# Exercise 2


class Person:
  def __init__(self, name, surname, birthdate, address, telephone, email):
    self.name = name
    self.surname = surname
    self.birthdate = birthdate
    self.address = address
    self.telephone = telephone
    self.email = email
    self._age = None
    self._age_last_recalculated = None
    self._recalculate_age()

  def _recalculate_age(self):
    today = datetime.date.today()
    age = today.year - self.birthdate.year
    if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
      age -= 1

    self._age = age
    self._age_last_recalculated = today

  def age(self):
    if (datetime.date.today() > self._age_last_recalculated):
      self._recalculate_age()

    return self._age

# Exercise 1- OOP


class Song:
  def __init__(self, title, artist, album, track_number):
    self.title = title
    self.artist = artist
    self.album = album
    self.track_number = track_number
    artist.add_song(self)


class Album:
  def __init__(self, title, artist, year):
    self.title = title
    self.artist = artist
    self.year = year
    self.tracks = []
    artist.add_album(self)

  def add_track(self, title, artist=None):
    if artist is None:
      artist = self.artist

    track_number = len(self.tracks)
    song = Song(title, artist, self, track_number)
    self.tracks.append(song)


class Artist:
  def __init__(self, name):
    self.name = name
    self.albums = []
    self.songs = []

  def add_album(self, album):
    self.albums.append(album)

  def add_song(self, song):
    self.songs.append(song)


class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)


band = Artist("Bob's Awesome Band")
album = Album("Bob's First Single", band, 2013)
album.add_track("A Ballad about Cheese")
album.add_track("A Ballad about Cheese (dance remix)")
album.add_track("A Third Song to Use Up the Rest of the Space")
playlist = Playlist("My Favourite Songs")

for song in album.tracks:
  playlist.add_song(song)

"""Exercise 4"""
"""Exercise 5"""
