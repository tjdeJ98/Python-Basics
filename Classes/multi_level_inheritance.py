class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Sparrow(Bird):
    def get_color(self):
        print("black")

# Chickens can't fly: so this is "Inheritence abuse"


class Chicken(Bird):
    pass


# Employee is a Person is a LivingCreature is a Thing
# Just because this is the case in real life, it doesn't mean it should be in software
# The Methods of your class are there so solve a business problem. That's the focus of your software!
# Just because an animal can eat in de real world, it doesn't mean your animal class should have an eat method.
# LIMIT inheritance to 1 or 2 levels. Beyond that you shoot yourself in the foot!
