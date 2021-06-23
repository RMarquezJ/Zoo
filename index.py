class Animal:

  def __init__(self, name, age, health, mood):

    self.name = name
    self.age = age
    self.health = health
    self.mood = mood
  
  def display_info(self):

    print(f'{self.name}, Health: {self.health}, Mood: {self.mood}')
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
    self.mood += 5
      
      # elif food == 'banana' or 'peanut':
      #   self.health +=10
      #   self.mood += 30

    return self


class Bird(Animal):
  def __init__(self, name, age=1, health=80, mood=70, doesFly=True):
    super().__init__(name, age, health, mood)


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


  print(f'Wellcome to {zoo1}')

  response = input('1: Add Ape \n2: Add Feline \n3: Add Bird \n4: Feed Animal \n5: Show Zoo Info \n0: Exit \n')

  if response == '0':

    break

  elif response == '1':

    zoo1.add_ape(input('Ape name:'))

  elif response == '2':

    print('Feline name:')
    zoo1.add_feline(input())

  elif response == '3':

    print('Bird name:')
    zoo1.add_bird(input())

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