class Beach:
  parts = ['water', 'sand']  # if it changes better to put as instance attribute

  def __init__(self, name, water_color, temperature, location):
    self.name = name
    self.water_color = water_color
    self.temperature = temperature
    self.heat_rating = 'hot' if temperature > 25 else 'cool'
    self.location = location

  def add_part(self, part):
    self.parts.append(part)


nitzanim = Beach('nitzanim', 'blue', 30, 'Israel')

print(type(nitzanim))
print(id(nitzanim))
