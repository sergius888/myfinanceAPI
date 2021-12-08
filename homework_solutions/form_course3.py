a = 3
b = 5

# we only defined the function, we did not call it
def suma(a, b):
    print(a + b)

if True and False: # every condtion with `and` & `False` goes to False
    print("yes")
else:
    print("no")

if True or False: # every condition with `or` & `True` goes to True
    print("True or False => True")
else:
    print("True or False => False")

if not False: # not False = True, not True = False
    print("not False = True")
else:
    print("not False = False")

if 2 == "2":
    print("2 yes")
else:
    print("2 no")

suma(3, 4)

# if False or True
if type(2) == type(2.0) or type(2) == type(-56):
    print("True condition")
else:
    print("False condtion")

# not (type(2) == type(2.0) ) => not False => True
# if True and True
if not type(2) == type(2.0) and type(2) == type(0):
    pass


def compute_sum(a, b):
    # a = 1, b = 1
    if type(a) == type(b):
        sum2 = a + b
        return sum2

x = compute_sum(1, 1)

x22 = ["a", "b", "c"]
x22[0] = "d" # "a" => "d"
print(x22)

d = {"x": 2, "y": 4, "z": 7}
s = d["a"] + d["c"] # d["a"] = 2, d["c"] = 7
print(s)

t = (1, 4, 8)
