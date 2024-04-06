# If we have classes that only contain data you might want to use a named typle instead.
from collections import namedtuple

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
# namedtuple we can't change the values after creating them
# p1.x = 10
# So we have to create a new namedtuple object
p1 = Point(x=10, y=2)

p2 = Point(x=1, y=2)
# Python compares objects based on where they are
# stored in memory. (Before we changed the __eq__ magic method)
print(p1 == p2)
print(id(p1), id(p2))
