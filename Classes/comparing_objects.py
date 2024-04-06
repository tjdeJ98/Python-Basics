class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y == other.y


point = Point(10, 20)
other = Point(1, 2)
# Will now use the __eq__ from the instance
print(point == point)

# Note how when we have the __gt__ implemented python will automatically do the __lt__ < for you
print(point > point)
print(point < point)
