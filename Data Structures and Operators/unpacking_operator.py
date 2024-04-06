numbers = [1, 2, 3]
print(numbers)
# But we want
print(1, 2, 3)

# For this we use the unpacking operator: *
# We unpack the container, take out the individual elements and pass them as
# arbitraty arguments.
print(*numbers)

# Also useful for creating lists
values = list(range(5))
print(values)

# Now with the unpacking operator: *
# We can unpack any iterable with this operator
# 1. we unpack the itterabel: !!Meaning: We take individual variables!!
values = [*range(5), *"Hello"]
print(values)

# Use it to combine lists
first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]
print(values)

# With dictionaries
first = dict(x=1)
second = dict(x=10, y=2)
# Unpack both dicts and add an extra element
# Note that if you have 2 dicts with the same key, the last parameters value will be used: second
combined = {**first, **second, "z": 1}
print(combined)
