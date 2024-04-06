# words = []

# runs = True
# while (runs):
#     new: str = input("Give a word: ")
#     if (new not in words):
#         words.append(new)
#     else:
#         runs = False


# for word in words:
#     print("Word: ", word)

# print(len(words))


def mean(numbers: list) -> float:
    i: float = 0.0
    for num in numbers:
        i += num
    return i/len(numbers)


print(mean([1, 2, 3, 4, 5]))


def range_of_list(numbers: list):
    return max(numbers) - min(numbers)


print(range_of_list([1, 2, 5, 7, 4, 3]))


# text = input("Type a string: ")
# i, x = len(text), 0

# while i > 0:
#     print(text[x])
#     print("*")
#     x, i = x+1, i-1


# number = int(input("Give a number: "))
# for num in range(-number, number+1):
#     if num != 0:
#         print(num)


def list_of_start(numbers: list):
    for num in numbers:
        print("*"*num)


list_of_start([3, 7, 1, 1, 2])


def anagrams(text_1: str, text_2: str):
    text_1.sort()
    return True


print(anagrams("python", "java"))
