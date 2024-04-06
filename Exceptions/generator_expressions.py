# Will give the size of memory in bytes
from sys import getsizeof

# Lets say we have a data set of a billion large. We don't want to store that in our memory
# In those situations it's more efficient to use a generator object
# Generator objects are iterable, and with each iteration they generate/spit out a new object
# So unlike lists they don't store all objects in memory
# But they generate a new value in each iteration
values = (x * 2 for x in range(100000))
print(values)

# for x in values:
#     print(x)

# The size of a generator object is interresting:
print("gen: ", getsizeof(values))

# Compare it to a list of the same "size"
# values = [x * 2 for x in range(100000)]
# print("list: ", getsizeof(values))

# Since it is not stored we don't know how many items (len) the generator object is going to produce
print(len(values))
