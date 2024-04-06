values = []

# item = x
# items = range(5)
# expression = x*2
for x in range(5):
    values.append(x*2)

print(values)

# [expression = x*2 for item = x in items = range(5)]
values_com_list = [x*2 for x in range(5)]

print(values)

# We can do the same for sets
values_com_set = {x*2 for x in range(5)}
print(values_com_set)

# We can also make dictionarys
values_com_dict = {x: x*2 for x in range(5)}
print(values_com_dict)

# When ever this pattern appears in code:
values = {}  # or []
for x in range(5):
    values[x] = x*2
# We should use dict comprehension


# What about tuples?
values_com_tuple = (x*2 for x in range(5))
print(values_com_tuple)  # We get a <generated object>?
