from array import array
from sys import getsizeof
from collections import deque

dict_1 = {"x": 1, "y": 2}
dict_2 = dict(x=1, y=2)
dict_3 = {x: x*2 for x in range(5)}
print(dict_3)
print(type(dict_3))

set_1 = {1, 2, 3}
set_2 = set([1, 1, 3, 4, 5])
set_3 = {x*2 for x in range(5)}
print(set_3)
print(type(set_3))

list_1 = [1, 2, 3, 4, "h"]
list_2 = list(set_1)
list_3 = list_1 + list_2
print(list_3)

array_1 = array("i", set_2)
print(*array_1)

tuple_1 = 1, 2
tuple_2 = (1, 2, 3, 4)
tuple_3 = (x*2 for x in range(5))
print(tuple_3)
for i in tuple_3:
    print(i)
print(getsizeof(tuple_3))

queue_1 = deque([])
queue_1.append(1)
queue_1.append(2)
queue_1.append(3)
print(queue_1)
print(queue_1.popleft())

stack_1 = []
stack_1.append(1)
stack_1.append(2)
stack_1.append(3)
print(stack_1)
print(stack_1.pop())
