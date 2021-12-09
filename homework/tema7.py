# Some of these exercises can be solved using some built-in functions of python.
# The scope is not to use them, to use and exercise `for` and `if`.

# homework with lists and for
# ex 1
def say_hello_to_all(list_of_names):
    # write a for to say(print) hello to all names
    pass


names = ["Bob", "Jane", "Bill", "George", "Ryan"]
say_hello_to_all(names)


# ex 2
def print_only_odd_numbers(list_of_numbers):
    # print only the odd numbers from the list (numerele impare)
    pass


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_only_odd_numbers(numbers)


# ex 3
def return_even_numbers(list_of_numbers):
    # return a new list with only the even numbers
    # example of code to add element to the end of a list
    #   lista.append(4)
    pass


even_numbers = return_even_numbers(numbers)
print(even_numbers)



# ex 4 - difficult

def return_an_ordered_list(list_of_numbers):
    # write code that returns a list of ordered numbers (0, 1, 2, 3, ...)
    pass

numbers = [0, -4, 56, 7.0, 89, 203.45, 0.45, -0.3, 5, 8]
ordered_numbers = return_an_ordered_list(numbers)
if ordered_numbers == [-4, -0.3, 0, 0.45, 5, 7.0, 8, 56, 89, 203.45]:
    print("function is good")
else:
    print("function is not good")
# a little hint, you need to keep track of the index on which you are on


# ex 5
#create a function which returns the number of elements in a list

# ex 6
# create a function which multiplies all the numbers in the list
list_to_try = ["hello", 2, 1, -4, "alt string", True]

# ex 7 - difficult
# create a function which removes duplicate items from a list
list_with_duplicates = [1, 1, 2, 3, 3, 2, 5, 6, 7, "a", 5, 2]
list_without = [1, 2, 3, 5, 6, 7, "a"]

# ex 8
# create a function which creates a text with all the strings from the list
lista8 = ["hey", 1, False, "there", "do", 0, "you", -0.9, "know", "the", "clock", 77, 88.9]

# ex 9 - intermediary difficulty
# create a function which returns the maximum and minimum number from a list

