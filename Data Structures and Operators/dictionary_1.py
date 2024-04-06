# Data struction. A collection of key value pairs.
# name -> contact : key -> value pair

point = {"x": 1, "y": 2}  # We can only use immutable items for keys
# list()
# tuple()
# set()
# dict()

# keyword arguments x=1
# This is same as mentioned above but a bit cleaner and easier because no ""
point = dict(x=1, y=2)

# Index is name of a key
point["x"] = 10
point["y"] = 20

# invalid key nog in dict
# print(point["a"])

# Solution
if "a" in point:
    print(point["a"])

# Searches for items with key "a", if not found then returns 0 by default
print(point.get("a", 0))

# To delete an item
del point["x"]

# print(point["x"])

# Loop over dict
for key in point:
    print(key, point[key])

# loop over dict get tuples
for key, value in point.items():
    print(key, value)
