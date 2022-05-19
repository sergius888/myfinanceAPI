# Some of these exercises can be solved using some built-in functions of python.
# The scope is not to use them, to use and exercise `for` and `if`.

# homework with lists and for
# ex 1
def say_hello_to_all(list_of_names):
    for name in list_of_names:
        print(name)


names = ["Bob", "Jane", "Bill", "George", "Ryan"]
say_hello_to_all(names)


# ex 2
def print_only_odd_numbers(list_of_numbers):
    for nr in list_of_numbers:
        if nr % 2 != 0:
            print(nr)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_only_odd_numbers(numbers)


# ex 3
def return_even_numbers(list_of_numbers):
    list_of_even_numbers = []# create a new empty list
    for nr in list_of_numbers:
        if nr % 2 == 0: # check nr is divisible by 2, rest equals 0
            list_of_even_numbers.append(nr)
    return list_of_even_numbers


# ex 4 - difficult
def return_an_ordered_list(numbers):
    index1 = 0
    index2 = 0
    for el1 in numbers:
        for el2 in numbers:
            if index1 < index2 and numbers[index1] > numbers[index2]:
                aux = numbers[index2] # we save one of the numbers in a variable
                numbers[index2] = numbers[index1]
                numbers[index1] = aux # aux is the initial value of numbers[index2]
            index2 = index2 + 1
        index1 = index1 + 1
        index2 = 0
    return numbers

numbers = [0, -4, 56, 7.0, 89, 203.45, 0.45, -0.3, 5, 8]
ordered_numbers = return_an_ordered_list(numbers)
if ordered_numbers == [-4, -0.3, 0, 0.45, 5, 7.0, 8, 56, 89, 203.45]:
    print("function is good")
else:
    print("function is not good")
# a little hint, you need to keep track of the index on which you are on


# ex 5
def count_list(lista):
    length = 0
    for element in lista:
        length = length + 1
    print(length)

my_list = [22, 89, 12, 0, 28, 15]


# print("Number of elements in the list: ", get_number_of_elements(my_list))

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count_list(x)

# ex 6
# create a function which multiplies all the numbers in the list
list_to_try = ["hello", 2, 1, -4, "alt string", True]
def multiply(lista):
    result = 1
    for el in lista:
        if type(el) == int or type(el) == float:
            result = result * el
    return result

print(multiply(list_to_try))


# ex 7 - difficult
# create a function which removes duplicate items from a list
list_with_duplicates = [1, 1, 2, 3, 3, 2, 5, 6, 7, "a", 5, 2]
list_without = [1, 2, 3, 5, 6, 7, "a"]
def is_in_list(element, lista):
    for el in lista:
        if el == element:
            return True # when we find the first element, we exit and return True
    return False # means we did not find the element

def remove_duplicates(lista):
    new_list = []
    for el in lista:
        if el in new_list:
            pass
        else:
            new_list.append(el)
    return new_list

if remove_duplicates(list_with_duplicates) == list_without:
    print("we removed the duplicates")
else:
    print("we did NOT remove")

# ex 8
# create a function which creates a text with all the strings from the list


def create_sentence(lista):
    sentence = ""
    for el in lista:
        if type(el) == str:
            sentence = sentence + el + " "
    print(sentence)


lista8 = ["hey", 1, False, "there", "do", 0, "you", -0.9, "know", "the", "clock", 77, 88.9]
create_sentence(lista8)

# ex 9 - intermediary difficulty
# create a function which returns the maximum and minimum number from a list
def min_and_max(lista):
    min = lista[0]
    max = lista[0]
    for el in lista:
        if min > el:
            min = el
        if max < el:
            max = el
    return (min, max)

print(min_and_max(numbers))





