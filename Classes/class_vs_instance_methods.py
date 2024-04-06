class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # cls is a reference to the class and not the object/instance like "self".
    @classmethod  # <- decorator
    def zero(cls):
        # Same ass calling Point(0, 0) but makes it so we have 1 spot where we do it and not every where were we need it.
        return cls(0, 0)

    # These are instance methods
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# So we call them with an instance of the Class
point.draw()  # So instance method

# Zero would be a method defined a class level
point2 = Point.zero()  # <- factory method: creates a new object with 0 values
point2.draw()
