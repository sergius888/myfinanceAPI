# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.


# ex1 write code that creates a list with the input params of the function
# pass # this line can be removed after the code is written


def create_list(x, y, z, w, t):
    print(x, y, z, w, t)


list = [3, 1, 2, 5, 4]
create_list(*list)


# ex2
def is_smaller_than_1_and_is_positive(a):
    if a < 1 and a > 0:  # the function should return a bool
        return True  # it should check the condition from the functions name
    else:
        return False


print(is_smaller_than_1_and_is_positive(0.2))

#ex3
def compute_password_strength(password):
    strengths = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
    if len(password) > strengths["weak"] and len(password) < strengths["decent"]:
        print("Your password is weak")
    elif len(password) >= strengths["decent"] and len(password) < strengths["good"]:
        print("Your password is decent")
    elif len(password) >= strengths["good"] and len(password) < strengths["strong"]:
        print("Your password is good")
    elif len(password) >= strengths["strong"]:
        print("Your password is strong")
    else:
        print("try again")

password = "ihavenoideawhatijustdid"
compute_password_strength(password)


# def compute_password_strength(password):
#     strengths = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
#     weak = list(strengths.values())[0]
#
#     if len(password) > 0 and len(password) < 8:
#         return strengths[0]
#     elif len(password) >= 8 and len(password) < 16:
#         return strengths[8]
#     elif len(password) >= 16 and len(password) < 32:
#         return strengths[16]
#     elif len(password) >= 32:
#         return strengths[32]
#     else:
#         print("try again")
#
# password = "ihavenoideawhatijustdid"
# print(compute_password_strength(password))


# ex4
# create a sentence on this line using the 3 names from the tuple

example_of_tuple = ("Horea", "Closca", "Crisan")
text = (example_of_tuple[0], ' and', example_of_tuple[1], ' were trolled by ', example_of_tuple[2])
print(text)



#ex5  #receives a variable 'email' which is a string, checks if there is only one char '@' and after it only 1 '.'
def is_email(email):
    a = "@"
    dot = "."
    total_a = email.count(a)
    total_dot = email.count(dot)
    if total_a == 1:
        domain = email.split(a, 1)
        if total_dot in domain == 1:
            return

if is_email("roberto.judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto@judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto.judet@itschool"):
    print("Daca se printeaza asta, functia a evaluat corect")

# #ex6
# def check_int_bigger_than_10_float_smaller_than_0_point_5(m, n):
#     # receives 2 params 'm' & 'n'
#     # one is a float, the other int, we do not know which one
#     # check the following 2 condtions: the int is bigger than 10, the float has after the point a value smaller than 0.5
#     # if one condtion is True, return True from the function
#     pass

def check_func(m, n):
    if int > 10 or float