class Point:
    # Class attributes that are shared along all Point Class instances/Objects
    default_color = "red"

    def __init__(self, x, y):
        # Instance Attributes for our point Objects in the constructor of out Point class
        # attribute that belong to point instances or point objects
        # So every point object can have different values
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# here we can change the Class Attribute by calling the class attribute.
# Note: This is across all classes
Point.default_color = "yellow"
point = Point(1, 2)
# Attributes are dynamic in python, so we don't have to define them in the constructor
# we can define them later, when ever we need them
# point.z = 10
print(point.default_color)
print(Point.default_color)
# Note how the already created objects also change with the changing of the Class Attribute change
Point.default_color = "blue"
print("After Blue: ", point.default_color)
point.draw()

another = Point(3, 4)
another.draw()
