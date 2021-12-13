# Some of these exercises can be solved using some built-in functions of python.
# The scope is not to use them, to use and exercise `for` and `if`.

# homework with lists and for
# ex 1
def say_hello_to_all(list_of_names):
    for names in list_of_names:
        print(names)


names = ["Bob", "Jane", "Bill", "George", "Ryan"]
say_hello_to_all(names)


# ex 2
def print_only_odd_numbers(list_of_numbers):
    for numbers in list_of_numbers: # print only the odd numbers from the list (numerele impare)
        if numbers % 2 != 0:
            print(numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_only_odd_numbers(numbers)


# ex 3
def return_even_numbers(list_of_numbers):
    for numbers in list_of_numbers:
        if numbers % 2 == 0:
            print(numbers, end=" ")

    # return a new list with only the even numbers
    # example of code to add element to the end of a list
    #   lista.append(4)

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.append(8)
even_numbers = return_even_numbers(numbers)
print(even_numbers)


# ex 4 - difficult

def return_an_ordered_list(list_of_numbers):
    return sorted(list_of_numbers)# write code that returns a list of ordered numbers (0, 1, 2, 3, ...)


numbers = [0, -4, 56, 7.0, 89, 203.45, 0.45, -0.3, 5, 8]
ordered_numbers = return_an_ordered_list(numbers)
# print(ordered_numbers)
if ordered_numbers == [-4, -0.3, 0, 0.45, 5, 7.0, 8, 56, 89, 203.45]:
    print("function is good")
else:
    print("function is not good")
# a little hint, you need to keep track of the index on which you are on

#without built in func



#
# # ex 5
# #create a function which returns the number of elements in a list
my_list = [1, 5.6, 2, 69, "word", 666, "stuff"]
number_of_elements = len(my_list)
print("The list contain", number_of_elements, "elements")

#
# # ex 6
# # create a function which multiplies all the numbers in the list

list_to_try = ["hello", 2, 1, -4, "alt string", True]

el = 1
for num in list_to_try:
    try:
        el *= int(num)
    except :
        pass
print("The result is " + str(el))



# # ex 7 - difficult
# # create a function which removes duplicate items from a list
list_with_duplicates = [1, 1, 2, 3, 3, 2, 5, 6, 7, "a", 5, 2]
list_without = [1, 2, 3, 5, 6, 7, "a"]
# method 1
list_with_duplicates = list(dict.fromkeys(list_with_duplicates))
print(list_with_duplicates)

# method 2
for i in list_with_duplicates:
    if list_with_duplicates.count(i) > 1:
        list_with_duplicates.remove(i)

print(list_with_duplicates)

# method 3

list_without_duplicates = []

for i in list_with_duplicates:
    # Add to the new list
    # only if not present
    if i not in list_without_duplicates:
        list_without_duplicates.append(i)

print(list_without_duplicates)


# # ex 8
# # create a function which creates a text with all the strings from the list
lista8 = ["hey", 1, False, "there", "do", 0, "you", -0.9, "know", "the", "clock", 77, 88.9]

def str_only(list):
    s = ""
    for ele in list:
        if(type(ele) == str):
            s += ele
    return s

print(str_only(lista8))

# ex 9 - intermediary difficulty
# create a function which returns the maximum and minimum number from a list

def max_min(list):
    print("Maximum number is ", max(list), " and minimum is ", min(list))

listuta = [1, 2, 3, 4, 5, 6, 7, 8]
print(max_min(listuta))