import datetime

class Student:
  def __init__(self, name, surname, age, weight, devices, grades, birthdate):
    print("student")
    self.name = name
    self.surname = surname
    self.full_name = self.name + " " + self.surname # this should be str - 'Tom Smith'
    self.age = age # int - 2
    self.weight = weight # float - 70.5 KG
    self.devices = devices # list - ['PC', 'Phone', 'Laptop']
    self.grades = grades # dict - {'oop': 5, 'marketing': 4.5}
    self.birthdate = birthdate # date - 11-04-93
    self.exchange_program = False
  
  def device_list_append(self):
    new_device = input("Please enter new device: ")
    self.devices.append(new_device)

  def device_list_ellement_remove(self):
    print(self.devices)
    device_remove = input("Please enter device to remove: ")
    if device_remove in self.devices:
      self.devices.remove(device_remove)
      print(device_remove + " had been removed from " + self.full_name + "'s device list successfully!")
    else:
      print("Error! The item wasnt at the list in first place!")

  def greetings(self):
    print("Hello, my name is", self.name + "!")

  def greetings_fullname(self):
    print("Hello, my full name is", self.full_name + "!")

  def getting_older(self):
    self.age = self.age + 1

  def exchange_program_check(self):
    if self.exchange_program == True:
      print( "Student", self.full_name, "is from exchange program")
    else:
      print( "Student", self.full_name, "isn't from exchange program")

  def true_age(self):
    day,month,year = map(int, self.birthdate.split("-"))
    today = datetime.date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    print(self.full_name, "is", age ,"years.")

def give_subject_and_grade(self):
  pass

def fix_subject(self):
  pass

def fix_grade(self):
  pass

class Pony(Student):
  def __init__(self, name, surname, age, weight, devices, grades, birthdate):
    super().__init__(name, surname, age, weight, devices, grades, birthdate)
    self.exchange_program = True # boolean


mike_smit = Student(
  name = "Mike",
  surname = "Smit",
  age = 24,
  weight = 78.0,
  devices = ['Tablet'],
  grades = {'math': 5, 'cooking': 4.5, 'p.e.':4},
  birthdate = "23-12-1999")

twiglight_sparkle = Pony("Twiglight Sparkle", "Esacha", 28,  73.2, ['PC', 'Phone', 'Laptop'], {'math': 5, 'english': 4.5, 'p.e.': 4 }, "1998-04-23")
applejack = Pony("Apple Jack", "Bagcabax", 26, 85.3, ['Phone', 'Laptop'], {'math': 5, 'english': 4.5, 'gardening':4}, "1998-04-23")

mike_smit.greetings_fullname()
applejack.greetings()
print(applejack.age)
applejack.getting_older()
print(applejack.age)
applejack.exchange_program_check()
mike_smit.exchange_program_check()
mike_smit.true_age()
print(mike_smit.age)
mike_smit.getting_older()
print(mike_smit.age)
mike_smit.true_age()
