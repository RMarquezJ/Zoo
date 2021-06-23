class Animal:

  def __init__(self, name, age, health, mood):

    self.name = name
    self.age = age
    self.health = health
    self.mood = mood
  
  def display_info(self):

    print(f'\n{self.name}, Health: {self.health}, Mood: {self.mood}')
    return self
  
  def feed(self):

    self.health += 10
    self.mood += 10

    return self


class Ape(Animal):
  def __init__(self, name, age=3, health=90, mood=50, hasTail=True):
    super().__init__(name, age, health, mood)
  
  def feed(self):

    self.health += 5
    self.mood += 15
      
      # elif food == 'banana' or 'peanut':
      #   self.health +=10
      #   self.mood += 30

    return self


class Bird(Animal):
  def __init__(self, name, age=1, health=80, mood=70, doesFly=True):
    super().__init__(name, age, health, mood)

  def feed(self):

    self.health += 15
    self.mood += 5


class Feline(Animal):
  def __init__(self, name, age=2, health=70, mood=50, furPattern='Plain'):
    super().__init__(name, age, health, mood)

class Zoo:

  def __init__(self, zoo_name):
    self.animals = []
    self.name = zoo_name

  def add_ape(self,name):
    self.animals.append(Ape(name))
    return self

  def add_feline(self,name):
    self.animals.append(Feline(name))
    return self
  
  def add_bird(self,name):
    self.animals.append(Bird(name))
    return self

  def print_all_info(self):
    print('-'*30, self.name, '-'*30)
    for animal in self.animals:
      animal.display_info()
    return self
  
  def __repr__(self):
    return self.name


zoo1 = Zoo('Buin Zoo')

zoo1.add_ape('gorilla').add_ape('chimp')
zoo1.add_feline('tiger').add_feline('lion')
zoo1.add_bird('owl').add_bird('penguin')

while True:


  print(f'\nWellcome to {zoo1}\n')

  response = input('1: Add Ape \n2: Add Feline \n3: Add Bird \n4: Feed Animal \n5: Zoo Info \n0: Exit \n')

  if response == '0':

    break

  elif response == '1':

    apeName = input('\nApe name: ')
    zoo1.add_ape(apeName)
    print(f'\n{apeName} is now part of our zoo!\n')

  elif response == '2':

    felineName = input('\nFeline name: ')
    zoo1.add_feline(felineName)
    print(f'\n{felineName} is now part of our zoo!\n')

  elif response == '3':

    birdName = input('\nBird name: ')
    zoo1.add_bird(birdName)
    print(f'\n{birdName} is now part of our zoo!\n')

  elif response == '4':
    for i in range(len(zoo1.animals)):
      print(f'{i+1}: {zoo1.animals[i].name}')
    which_one = int(input('¿which animal do you want to feed? \n'))

    if which_one > len(zoo1.animals):
      print('Does not exist')
      continue
    # import pdb; pdb.set_trace()
    zoo1.animals[which_one - 1].feed()

  elif response =='5':
    zoo1.print_all_info()
  
  else:
    continue