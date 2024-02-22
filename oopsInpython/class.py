"""class Student:
    name = "karan"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)"""



"""class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()

print(car1.color)
print(car1.brand)"""


"""class Student:
    name = "karan"
    def __init__(self):
        print("Adding new student in database")

s1 = Student()"""


"""class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in database")

s1 = Student("karan", 99)
print(s1.name, s1.marks)  #karan 99

s2 = Student("arjun", 88)
print(s2.name, s2.marks)  #arjun 88"""

class Student:
    colloge_name = "Techno NJR"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("welcome,", self.name)

    def get_marks(self):
        return self.marks    
        
s1 = Student("karan", 99)
s1.welcome()
print(s1.get_marks())