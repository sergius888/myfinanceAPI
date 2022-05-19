#ex1
def create_list(x, y, z, w, t):
    lista = [x, y, z, w, t]
    return lista


a = create_list(1, 2, 0, 0, 0)
print(a)

#ex2
def is_smaller_than_1_and_is_positive(a):
    return a < 1 and a >= 0





#ex3
def compute_password_strength(password):
    s = {"weak": 0, "decent": 8, "good": 16, "strong": 32}
    length = len(password)
    if length < s["decent"]:
        return "weak"
    if length < s["good"]:
        return "decent"
    if length < s["strong"]:
        return "good"
    return "strong"

print(compute_password_strength(""))

#ex4
example_of_tuple = ("Horea", "Closca", "Crisan")
text = example_of_tuple[0] + "," + example_of_tuple[1] + "&" + example_of_tuple[2]

#ex5
def is_email(email):
    arond_index = email.find("@")
    # if we do not find any @, we exit with false
    if not arond_index > 0:
        return False
    # if we find an @, we check that there is a point after it and no @
    # we do +1 so we ommit the first @
    point_index = email[arond_index+1:].find(".")
    arond_index2 = email[arond_index+1:].find("@")
    return point_index > 0 and arond_index2 == -1



print(is_email("roberto@itschool"))
print(is_email("roberto@itschool.ro"))



if is_email("roberto.judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto@judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")
else:
    print("evaluare gresita")

if not is_email("roberto.judet@itschool"):
    print("Daca se printeaza asta, functia a evaluat corect")

#ex6
def check_int_bigger_than_10_float_smaller_than_0_point_5(m, n):
    # first we check if one of them is int and bigger than 10
    if bigger_than_10(m) or bigger_than_10(n):
        return True
    # second we check if one is float and smaller than 0.5
    elif type(m) == float and m <= 0.5 and m > 0 or type(n) == float and n <= 0.5 and n > 0:
        return True
    else:
        return False

def bigger_than_10(a):
    return type(a) == int and a > 10
