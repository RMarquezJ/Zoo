class Animal:

  def __init__(self, name, age, health, mood):

    self.name = name
    self.age = age
    self.health = health
    self.mood = mood
  
  def display_info(self):

    if self.mood < 30:
      self.mood = 'Angry'
    
    elif self.mood > 80:
      self.mood = 'Happy'
    
    else:
      self.mood = 'Relaxed'
    
    if self.health < 70:
      self.health = 'Unhealthy'
    
    elif self.health < 40:
      self.health = 'Sick'
    
    else:
      self.health = 'Healthy'

    print(f'{self.name}, {self.age} years old. Looks {self.health} and {self.mood}')
  
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
    
    print(f'{zoo1.animals[which_one - 1]} was given a banana')
  
  def __repr__(self):
    return self.name



class Bird(Animal):
  def __init__(self, name, age=1, health=80, mood=70, doesFly=True):
    super().__init__(name, age, health, mood)

  def feed(self):

    self.health += 15
    self.mood += 5

    print(f'{zoo1.animals[which_one - 1]} was given a cricket')
  
  def __repr__(self):
    return self.name


class Feline(Animal):
  def __init__(self, name, age=2, health=70, mood=50, furPattern='Plain'):
    super().__init__(name, age, health, mood)

  def feed(self):

    self.health += 10
    self.mood += 10

    print(f'{zoo1.animals[which_one - 1]} was given a mouse')
  
  def __repr__(self):
    return self.name

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
    print('-'*(62+len(self.name)))
    return self
  
  def __repr__(self):
    return self.name


zoo1 = Zoo('Buin Zoo')

zoo1.add_ape('Gorilla').add_ape('Chimpancee')
zoo1.add_feline('Tiger').add_feline('Lion')
zoo1.add_bird('Owl').add_bird('Penguin')

def main():

  while True:


    print(f'\nWellcome to {zoo1}!\n')

    response = input('Select an action: \n1: Add Animal \n2: Feed Animal \n3: Donate Animal \n4: Zoo Info \n0: Back \n')

    if response == '0':

      break
    
    if response == '1':

      specie = input('\nWich animal would you like to add? \n1: Ape \n2: Feline \n3: Bird \n0: Exit \n')

      if specie == '1':

        apeName = input('\nApe name: ')
        zoo1.add_ape(apeName)
        print(f'\nCongratulations, {apeName} is now part of our zoo!\n')

      elif specie == '2':

        felineName = input('\nFeline name: ')
        zoo1.add_feline(felineName)
        print(f'\nCongratulations, {felineName} is now part of our zoo!\n')

      elif specie == '3':

        birdName = input('\nBird name: ')
        zoo1.add_bird(birdName)
        print(f'\nCongratulations, {birdName} is now part of our zoo!\n')

      elif specie =='0':

        continue

    elif response == '2':
      for i in range(len(zoo1.animals)):
        print(f'{i+1}: {zoo1.animals[i].name}')
      which_one = int(input('¿which animal do you want to feed? \n'))

      if which_one > len(zoo1.animals):
        print('Does not exist')
        continue
      # import pdb; pdb.set_trace()
      zoo1.animals[which_one - 1].feed()
    
    elif response == '3':
      for i in range(len(zoo1.animals)):
        print(f'{i+1}: {zoo1.animals[i].name}')
      rel = int(input('¿which animal do you want to donate? \n'))

      if rel > len(zoo1.animals):
        print('Does not exist')
        continue
      print(f'\n{zoo1.animals[rel - 1]} was donated to a wildlife reserve')
      zoo1.animals.pop(rel - 1)
      

    elif response =='4':
      zoo1.print_all_info()
    
    else:
      continue

main()