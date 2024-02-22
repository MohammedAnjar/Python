class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetalis(self):
        print("role,", self.role)
        print("dept,", self.dept)
        print("salary,", self.salary)

"""e1 = Employee("developer","software",100000)
e1.showDetalis()"""

class Engineer(Employee):
    def __init__(self, name, age):
        super().__init__("engineer", "IT", 75000)


engg1 = Engineer("Elon musk", 40)
engg1.showDetalis()
        
