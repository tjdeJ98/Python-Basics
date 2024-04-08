import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=2))
chars = string.ascii_letters + string.digits
print("".join(random.choices(chars, k=4)))

nums = [1, 2, 3, 4]
random.shuffle(nums)
print(nums)
