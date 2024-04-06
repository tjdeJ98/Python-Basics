# A collection with no duplicates -> unordered so we can't access them with an index
numbers = [1, 1, 2, 3, 4]

first = set(numbers)
second = {1, 5}
# second.add(5)
# second.remove()
# len(second)

# A union |
# This will return a new set that will include all the items that are either in the -
# first or the second set
print(first | second)

# get the intersection of both sets
print(first & second)

# Remove all in second from first.
print(first - second)

# sematric difference (either in first or second set but not both)
print(first ^ second)

# How to check if something in the set, because we can't use an index
if 1 in first:
    print("yes")
