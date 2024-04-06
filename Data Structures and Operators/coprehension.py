items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

# lambda parameter: expression

prices = list(map(lambda item: item[1], items))
# Comprehension
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
print(filtered)
