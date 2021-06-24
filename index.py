class Animal:

  def __init__(self, name, age, health, mood):

    self.name = name
    self.age = age
    self.health = health
    self.mood = mood
  
  def display_info(self):
    
    moodval = ''
    healthval= ''

    if self.mood < 30:
      moodval = 'Angry'
    
    elif self.mood <50:
      moodval = 'Stressed'
    
    elif self.mood > 75:
      moodval = 'Happy'
    
    else:
      moodval = 'Relaxed'
    
    if self.health < 75:
      healthval = 'Unhealthy'
    
    elif self.health < 40:
      healthval = 'Sick'
    
    else:
      healthval = 'Healthy'

    print(f'{self.name}:    \t {self.age} years old. Looks {healthval} and {moodval}')
  
  def feed(self):

    self.health += 10
    self.mood += 10

    return self


class Ape(Animal):
  def __init__(self, name, age=3, health=90, mood=80, hasTail=True):
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

class Reptile(Animal):
  def __init__(self, name, age=1, health=80, mood=50, hasLegs=True):
    super().__init__(name, age, health, mood)

  def feed(self):

    self.health += 20
    self.mood += 5

    print(f'{zoo1.animals[which_one - 1]} was given a fly')
  
  def __repr__(self):
    return self.name


class Feline(Animal):
  def __init__(self, name, age=2, health=70, mood=40, furPattern='Plain'):
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

  def add_reptile(self,name):
    self.animals.append(Reptile(name))
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

zoo1.add_ape('Gorilla').add_feline('Tiger').add_bird('Penguin').add_reptile('Iguana')

def main():

  while True:


    print(f'\nWellcome to {zoo1}!\n')

    response = input('Select an action: \n1: Add Animal \n2: Feed Animal \n3: Donate Animal \n4: Zoo Info \n0: Back \n')

    if response == '0':

      break
    
    if response == '1':

      specie = input('\nWich animal would you like to add? \n1: Ape \n2: Feline \n3: Bird \n4: Reptile \n0: Exit \n')

      if specie == '1':

        apeName = input('\nApe name: ')
        apeAge = int(input ('\nAge: '))

        if apeAge<0 or apeAge>50:
          print('Value must be between 1 and 100')
          continue

        apeHealth = int(input ('\nHealth (1~100): '))
        if apeHealth<0 or apeHealth>101:
          print('Value must be between 1 and 100')
          continue

        apeMood = int(input ('\nMood level (1~100): '))
        if apeMood<0 or apeMood>101:
          print('Value must be between 1 and 100')
          continue

        zoo1.add_ape(apeName)
        zoo1.animals[len(zoo1.animals)-1].age = apeAge
        zoo1.animals[len(zoo1.animals)-1].health = apeHealth
        zoo1.animals[len(zoo1.animals)-1].mood = apeMood

        print(f'\nCongratulations, {apeName} is now part of our zoo!\n')

      elif specie == '2':

        felineName = input('\nfeline name: ')
        felineAge = int(input ('\nAge: '))

        if felineAge<0 or felineAge>50:
          print('Value must be between 1 and 100')
          continue

        felineHealth = int(input ('\nHealth (1~100): '))
        if felineHealth<0 or felineHealth>101:
          print('Value must be between 1 and 100')
          continue

        felineMood = int(input ('\nMood level (1~100): '))
        if felineMood<0 or felineMood>101:
          print('Value must be between 1 and 100')
          continue

        zoo1.add_feline(felineName)
        zoo1.animals[len(zoo1.animals)-1].age = felineAge
        zoo1.animals[len(zoo1.animals)-1].health = felineHealth
        zoo1.animals[len(zoo1.animals)-1].mood = felineMood

      elif specie == '3':

        birdName = input('\nbird name: ')
        birdAge = int(input ('\nAge: '))

        if birdAge<0 or birdAge>50:
          print('Value must be between 1 and 100')
          continue

        birdHealth = int(input ('\nHealth (1~100): '))
        if birdHealth<0 or birdHealth>101:
          print('Value must be between 1 and 100')
          continue

        birdMood = int(input ('\nMood level (1~100): '))
        if birdMood<0 or birdMood>101:
          print('Value must be between 1 and 100')
          continue

        zoo1.add_bird(birdName)
        zoo1.animals[len(zoo1.animals)-1].age = birdAge
        zoo1.animals[len(zoo1.animals)-1].health = birdHealth
        zoo1.animals[len(zoo1.animals)-1].mood = birdMood

      elif specie == '4':

        reptileName = input('\nreptile name: ')
        reptileAge = int(input ('\nAge: '))

        if reptileAge<0 or reptileAge>50:
          print('Value must be between 1 and 100')
          continue

        reptileHealth = int(input ('\nHealth (1~100): '))
        if reptileHealth<0 or reptileHealth>101:
          print('Value must be between 1 and 100')
          continue

        reptileMood = int(input ('\nMood level (1~100): '))
        if reptileMood<0 or reptileMood>101:
          print('Value must be between 1 and 100')
          continue

        zoo1.add_reptile(reptileName)
        zoo1.animals[len(zoo1.animals)-1].age = reptileAge
        zoo1.animals[len(zoo1.animals)-1].health = reptileHealth
        zoo1.animals[len(zoo1.animals)-1].mood = reptileMood

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