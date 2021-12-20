#ex1
def create_list(x, y, z, w, t):
    lista = [x, y, z, w, t]
    return lista

a = create_list(1, 2, 3, 4, 5)
print(a)

ex2
def is_smaller_than_1_and_is_positive(a):
    return a < 1 and a >= 0


I deleted by mistake above and don't know how to undo

#ex5
def is_mail(email):
    arond_index = email.find("@")
    #if we do not find any @ we exit or false
    if not arond_index > 0:
        return False
    #if we find and @, we check that there is a point after it and no @
    # we do +1 so we omit the first @
    point_index = email[arond_index+1:].find(".")
    arond_index2 = email[arond_index+1:].find("@")


print(is_email("asd@gmail.com"))

if is_email("roberto.judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto@judet@itschool.ro"):
    print("Daca se printeaza asta, functia a evaluat corect")

if not is_email("roberto.judet@itschool"):
    print("Daca se printeaza asta, functia a evaluat corect")

#ex6
def check_int_bigger_than_10_float_smaller_than_0_point_5(m, n):
    #$ check if one of them is int and bigger than 10
    if bigger_than_10(m) or bigger_than_10(n):
        return True
    # check if one is float and smaller than 0.5
    if type(m) == float and m <= 0.5 and m > 0 or type(n) == float and n <= 0.5 n > 0:
        return True
    else:
        return False

def bigger_than_10(a):
    return type(a) == ind and a > 10