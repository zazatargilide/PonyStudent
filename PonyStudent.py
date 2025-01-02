import datetime

class Student:
  def __init__(self, name, surname, age, weight, devices, grades, birthdate):
    self.name = name
    self.surname = surname
    self.full_name = self.name+" "+ self.surname # this should be str - 'Tom Smith'
    self.age = age # int - 2
    self.weight = weight # float - 70.5 KG
    self.devices = devices # list - ['PC', 'Phone', 'Laptop']
    self.grades = grades # dict - {'oop': 5, 'marketing': 4.5}
    self.birthdate = birthdate # date - 11-04-93
    self.exchange_program = False #boolean

  def device_list_append(self):
    new_device = input("Please enter new device: ")
    self.devices.append(new_device)

  def device_list_element_remove(self):
    print(self.devices)
    device_remove = input("Please enter device to remove: ")
    if device_remove in self.devices:
      self.devices.remove(device_remove)
      print(device_remove + " had been removed from " + self.full_name + "'s device list successfully!")
    else:
      print("Error! The item wasn't at the list in first place!")

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
    print(self.grades)
    name_subject = input("Please enter new subject's name: ")

    if name_subject not in self.grades:
        mark = input("Please enter mark for new subject: ")
        print(name_subject + "was added to the grades dictionary with", mark, "mark now.")
        self.grades[name_subject] = mark
        print(self.grades)
    elif name_subject in self.grades:
      print("The subject already exits!")
    else:
      print("Error!")

  def fix_subject(self):
    print(self.grades)
    name_subject = input("Please enter subjects name that you want to change: ")

    if name_subject in self.grades:
        new_name_subject = input("Please enter new subject name: ")
        print(name_subject, "subjects name was changed to", new_name_subject, "now.")
        self.grades[new_name_subject] = self.grades.pop(name_subject)
        print(self.grades)
    else:
      print("Error! The subject was not found!")

  def fix_grade(self):
    print(self.grades)
    name_subject = input("Please enter subject's name that the grade of you want to change: ")

    if name_subject in self.grades:
        mark = input("Please enter mark that you want to change: ")
        print(name_subject + "s' subjects grade was changed to", mark, "now.")
        self.grades[name_subject] = mark
        print(self.grades)
    else:
      print("Error! The subject was not found!")

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

twiglight_sparkle = Pony("Twiglight Sparkle", "Moon", 28,  73.2, ['PC', 'Phone', 'Laptop'], {'math': 5, 'english': 4.5, 'p.e.': 4 }, "23-11-2005")
applejack = Pony("Apple Jack", "Bagcabax", 26, 85.3, ['Phone', 'Laptop'], {'math': 5, 'english': 4.5, 'gardening':4}, "23-04-1998")
twiglight_sparkle.true_age()