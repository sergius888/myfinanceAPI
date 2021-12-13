#ex1
def create_list(x, y, z, w, t):
    # write code that creates a list with the input params of the function
    pass # this line can be removed after the code is written

#ex2
def is_smaller_than_1_and_is_positive(a):
    #the function should return a bool
    # it should check the condition from the functions name
    pass

#ex3
def compute_password_strength(password):
    strengths = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
    # a password can be considered decent if it has at least 8 characters, so goes for the rest
    #write code that will return the strenght of the variable 'password'
    pass

#ex4
example_of_tuple = ("Horea", "Closca", "Crisan")
text  = "" # create a sentence on this line using the 3 names from the tuple

#ex5
def is_email(email):
    #receives a variable 'email' which is a string, checks if there is only one char '@' and after it only 1 '.'
    #returns bool
    pass

if is_email("roberto.judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto@judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto.judet@itschool"):
    print("Daca se printeaza asta, functia a evaluat corect")

#ex6
def check_int_bigger_than_10_float_smaller_than_0_point_5(m, n):
    # receives 2 params 'm' & 'n'
    # one is a float, the other int, we do not know which one
    # check the following 2 condtions: the int is bigger than 10, the float has after the point a value smaller than 0.5
    # if one condtion is True, return True from the function
    pass