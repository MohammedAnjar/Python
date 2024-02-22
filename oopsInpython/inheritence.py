class Car:
    color = "black"

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stoped...")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("fortuner")
car2 = Toyota("prius")

print(car1.start())
print(car1.color)