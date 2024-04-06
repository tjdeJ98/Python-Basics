from pprint import pprint
"""
Find the most repeated character in this text
"""
sentence = "This is a common interview questions"

# First solution
unique_chars = set([char.lower() for char in sentence if char.strip()])

x = 0
result = ""
for char in unique_chars:
    i = 0

    for char_sen in sentence:
        if char == char_sen.lower():
            i += 1

    if i > x:
        x = i
        result = char

print(result, x)

# second solution
i, result = 0, ""
unique_chars = set([char.lower() for char in sentence if char.strip()])

for char in unique_chars:
    sen_count = sentence.lower().count(char)
    if i < sen_count:
        i, result = sen_count, char

print(result, i)


# Course solution
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char_frequency = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)

pprint(sorted_char_frequency[0])
