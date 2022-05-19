# there will be some exercises here

def is_divisible(number, divisor):
    return number % divisor == 0

print(is_divisible(7, 3))
print(is_divisible(100, 10))

# create a function which receives a number
# if the number is odd (impar) multiply by 3, if not divide it by 2
def ex2(nr):
    if nr % 2 == 0:
        return nr // 2
    else:
        return nr * 3

def number(x):
    if x % 2: # if 0 -> False, if 1 -> True
        print(x * 3)
    else:
        print(x // 2)

number(4)
number(5)

# What values should x,y have so the following if statements are True? What about False?
x = 11
a = x > 6 and x < 12
print(a)

x = 11
a = x > 6 and x < 12
print(a)

x = 12
y = 12
b = x > 10 or y > 10
print(b)

x = False
c = x < 9 or True
print(c)

y = 99
d = y > 99 and False # this will always be False
print(d)

# x = None
# e = x > 10 and x < 10, this will be False for any value
# print(e)

x = 0 # it could also be False
f = not x
print(f)

x = 13
y = 90
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)
