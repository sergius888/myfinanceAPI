a = 3
b = 5


def suma(a, b):
    print (a + b)

if True and False: # every condition with "and" & "False" goes to False
    print("yes")
else:
    print("no")

if True or False: # every addition with "or" & "True" goes True
    print("True or False => True")
else:
    print("True or False => False")

if not False:
    print("not False = True")
else:
    print("not Flase = False")


if not True:
    print("not True = Flase")
else:
    print("not True = True")


if 2 == "2":
    print("2 yes")
else:
    print("2 no")

if type(2) == type(2.0) or type(2) == type(-22):
    print("second condition is true which means the condition its the True ")
else:
    print("false condition")


# not type(2) == type(2.0)  => not False => True
if not type(2) == type(2.1) and type(2) == type(0):
    pass

l = ["a", "b", "c"]
l[0] = "d"
print(l)

d = {"a":2, "b":4, "c": 7}
s = d["a"] + d["c"]
print(s)


t = (1, 3, 8)
print(t[2])
