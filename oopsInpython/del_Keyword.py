# del --> del keyword use to delete attribute or object

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("sharddha")
#del s1
print(s1)
del s1.name
print(s1.name) 