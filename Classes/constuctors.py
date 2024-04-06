class Point:
    # Magic method
    # This is constructor and exicuted when we make a new Point Object
    # What is "self"? Self is a reference to the current Point Object -> point = Point(1, 2) is an object of Point
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # No need to pass the self parameter where we call the method. Python does this automatically
    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# x would be an attribute of the Point Object
print(point.x)
point.draw()
