import datetime

class Student:
    def __init__(self, name, surname, age, grades, birthdate, devices, type = "human"):
        self.name = name
        self.surname = surname
        self.full_name = name +" "+  surname
        self.age = age
        self.grades = grades
        self.birthdate = birthdate # day-month-year(4 digits)
        self.devices = devices # list - ['PC', 'Phone', 'Laptop']
        self.type = type
        self.exchange_program = False

    def zapoznanie(self):
        your_name = input("Jak masz na imie? \n")
        your_answer = input(f"Masz piekne imie, {your_name}!\n")

        if any(phrase in your_answer.lower() for phrase in ["a ty", "a, ty"]):
            print(f"Nazywam sie {self.name} {self.surname}. Milo mi :)")

    def starzeje_sie(self):
        self.age = self.age + 1
        if self.age == 1:
            print("Student", self.name, "ma tylko jeden rok")
        elif self.age % 10 in [2, 3, 4] and self.age not in [12, 13, 14]:
            print("Student", self.name, "teraz ma", self.age,"lata")
        elif self.age % 10 in [1, 5, 6, 7, 8, 9] or self.age % 10 == 0 or self.age in [12, 13, 14] and self.age != 1:
            print("Student", self.name, "teraz ma", self.age,"lat")

    def zmenic_imie_i_nazwisko(self):
        choose_function = input("Chcesz zmienić imię lub nazwisko obiektu?\n")
        if any(phrase in choose_function.lower() for phrase in ["imie", "imię"]):
            self.name = input("Jakie będzie nowe imię obiektu?\n").title()
            print(f"{self.name} to nowe imię obiektu")

        elif choose_function.lower() == "nazwisko":
            self.surname = input("Jakie będzie nowe nazwisko obiektu?\n").title()
            print(f"{self.surname} to nowe nazwisko obiektu")

    def zmienic_oceny(self):

        def dac_przedmiot_i_ocene():
            print(self.grades)
            name_subject = input("Proszę wpisać nazwę nowa zajęć:")

            if name_subject.lower() not in self.grades:
                mark = input("Proszę wpisać znak dla nowa zajęć:")
                print(name_subject + "dodano zajęcia szkolne z oceną", mark)
                self.grades[name_subject] = mark
                print(self.grades)
            elif name_subject.lower() in self.grades:
                print("Lekcja o tej nazwie już istnieje!")
            else:
                print("Błąd!")

        def popraw_przedmiot():
            print(self.grades)
            name_subject = input("Wpisz nazwę zajęć, które chcesz zmienić:").lower()

            if name_subject.lower() in self.grades:
                new_name_subject = input("Proszę wpisać nową nazwę zajęć:").lower()
                if new_name_subject == name_subject:
                    print("Błąd! To samo imię!")
                else:
                    print(name_subject, "nazwa przedmiotu szkolnego została teraz zmieniona na", new_name_subject)
                    self.grades[new_name_subject] = self.grades.pop(name_subject)
                    print(self.grades)
            else:
                print("Błąd! Nie znaleziono zajęć!")

        def popraw_ocene():
            print(self.grades)
            name_subject = input("Proszę wpisać nazwę przedmiotu, z którego chcesz zmienić ocenę:").lower()
            if name_subject in self.grades:
                old_mark = self.grades[name_subject]
                try:
                    mark = int(input("Proszę wpisać nową ocenę z przedmiotu::"))
                    if mark == old_mark:
                        print("Błąd! Nowy znak jest taki sam jak stary znak.")
                    else:
                        self.grades[name_subject] = mark
                        print(f"{name_subject.capitalize()}, ocena z tego przedmiotu została zmieniona na: {mark}.")
                        print(self.grades)
                except ValueError:
                    print("Nieprawidłowe dane wejściowe! Wprowadź wartość liczbową oceny.")
            else:
                print("Błąd! Nie znaleziono zajęć!")

        choose_method = input("Which method you want to choose?\n(Add new subject / Fix subject's grade / Fix name of subject)\n")
        if choose_method.lower() == "add new subject":
            dac_przedmiot_i_ocene()
        elif choose_method.lower() == "fix subject's grade":
            popraw_ocene()
        elif choose_method.lower() == "fix name of subject":
            popraw_przedmiot()
        else:
            print("Error!")

    def sprawdzenie_programu_wymiany(self):
        if self.exchange_program == True:
            print( "Student", self.full_name, "is from exchange program")
        else:
            print( "Student", self.full_name, "isn't from exchange program")

    def prawdziwy_wiek(self):
        day,month,year = map(int, self.birthdate.split("-" or "/"))
        today = datetime.date.today()
        age = today.year - year - ((today.month, today.day) < (month, day))
        if self.age == 1:
            print("Student", self.full_name, "ma tylko jeden rok")
        elif self.age % 10 in [2, 3, 4] and self.age not in [12, 13, 14]:
            print("Student", self.full_name, "ma", self.age,"lata")
        elif self.age % 10 in [1, 5, 6, 7, 8, 9] or self.age % 10 == 0 or self.age in [12, 13, 14] and self.age != 1:
            print("Student", self.full_name, "ma", self.age,"lat")

    def zmien_liste_urzadzen(self):

        def device_list_append():
            new_device = input("Please enter new device: ")
            self.devices.append(new_device)
            print(self.devices)

        def device_list_element_remove():
            device_remove = input("Please enter device to remove: ")
            if device_remove in self.devices:
                self.devices.remove(device_remove)
                print(device_remove + " had been removed from " + self.full_name + "'s device list successfully!")
            else:
                print("Error! The item wasn't at the list in first place!")

        choose_method = input("Which method you want to choose?\n(Add new device / Remove device)\n")
        if choose_method.lower() == "add new device":
            device_list_append()
        elif choose_method.lower() == "remove device":
            device_list_element_remove()
        else:
            print("Error!")


class Pony(Student):
    def __init__(self, name, surname, age, color, grades, birthdate, devices):
        super().__init__(name, surname, age, grades, birthdate, devices)
        self.color = color
        self.type = "pony"
        self.exchange_program = True

mami_takada = Student("Mami", "Takada", 19, {"polski jezyk": 5, "japonski jezyk": 5, "matematyka": 4}, "23-12-1999", ['PC', 'Phone', 'Laptop'])
applejack = Pony("Applejack", "Bloom", 21, "yellow", {"polski jezyk": 3, "informatyka": 5, "matematyka": 5}, "12-02-1989", ['Phone', 'Laptop'])
applejack.prawdziwy_wiek()