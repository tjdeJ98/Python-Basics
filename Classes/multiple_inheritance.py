class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# In Python a Class can have multiple base classes
# Called: Multiple Inheritance
class Manager(Employee, Person):
    pass


manager = Manager()
# It will look at it's first base class: So in this case Employee
# Problem: If someone now switches the order of the Employee and Person, the behaviour of our
# object manager changes and it shouldn't
manager.greet()


# So only use multiple inheritence when the classes look nothing like eachother
# and are small
# For example:


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
