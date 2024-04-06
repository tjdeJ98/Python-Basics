class Point:
    # Magic Methods (Begin and end with __...__)
    # Are called automatically by the Python interpeter depending on how we use our objects and classes
    # So __init__ is automatically called by the Python interpeter when we create a new Point object/instance
    # For complete list of all magic methods: A Guide to Python's Magic Methods << rafekettler.com
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.__str__())
print(str(point))
