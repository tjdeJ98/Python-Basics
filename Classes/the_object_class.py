# Base class of all classes in Python is "object"
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, Animal))
print(isinstance(m, object))
# See how this o has all the magic methods. And how these are inheritate by the mammal class.
o = object()
# o.

print(issubclass(Mammal, object))
