def line(x, y):
    print(x*y)


line("y", 5)


def square(width, height, char):
    for x in range(height):
        print(char*width)


def triangle(num, char):
    for x in range(1, num+1):
        print(char*x)


def shape(num_x, char_x, num_y, char_y):
    triangle(num_x, char_x)
    square(num_x, num_y, char_y)


shape(5, "X", 3, "*")
shape(2, "o", 4, "+")
shape(3, ".", 0, ",")

#  *
# ***
# *****
#  *


def spruce(num):
    print("A spruce!")
    for x in range(1, num+1):
        amount = num-x
        print(" "*amount, "*"*(x*2-1))

    print(" "*(num-1), "*")


spruce(7)


def greatest_number(*args):
    return max(args)


print(greatest_number(1, 2, 3, 4))


def same_chars(item, index_1, index_2):
    return item[index_1] == item[index_2]


print(same_chars("programmer", 6, 7))
print(same_chars("programmer", 0, 4))


def first_word(sentence: str):
    return sentence.split()[0]


def middle_word(sentence: str):
    sentence_list = sentence.split()
    middle = int(len(sentence_list)/2)
    return sentence_list[middle]


def last_word(sentence: str):
    return sentence.split()[-1]


sentence = "It was a dark and stormy python"
print(first_word(sentence))
print(middle_word(sentence))
print(last_word(sentence))

sentence = "It was"
print(first_word(sentence))
print(middle_word(sentence))
print(last_word(sentence))
