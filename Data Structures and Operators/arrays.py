# Take little memory, and are a little faster if you work with for example 10.000 items.
# Use a list when you have less items. Don't solve something that is not a problem.

from array import array

# first parameter of array is a "Typecode" -> a string that determince the type of objects in your array
# https://docs.python.org/3/library/array.html
numbers = array("i", [1, 2, 3])

# To append to end
numbers.append(4)

# add to specific index
numbers.insert(4)

# Remove last item
numbers.pop()

# Remove item
numbers.remove()

# access items by index
# Note that every object in the array is typed (typecode). So for "i" every object should be an integer
# So we can't put anything but an integer.
numbers[0]
