# Class names in Python always CamelCase. Always start with capital letter, no numbers or reading signs.
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, int))
