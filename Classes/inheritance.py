# Problem: We have a duplicate eat method DRY Don't Repeat Yourself
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Inheritance:
# Animal: Parent, Base Class
# Mammal: Child, Sub Class
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


nemo = Fish()
nemo.eat()
print(nemo.age)
