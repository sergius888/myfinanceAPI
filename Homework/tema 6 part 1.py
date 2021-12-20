def is_divisible(number, divisor):
    if number % divisor == 0:
        return True  # check that the variable `number` is divisible by `divisor`
    else:
        return False

print(is_divisible(20, 2))

# create a function which receives a number
# if the number is odd (impar) multiply by 3, if not divide it by 2


def function_number(number):
    if number % 2 == 0:
        return number / 2
    else:
        return number * 3

print(function_number(0))

#
#
# What values should x,y have so the following if statements are True? What about False?

x = 7 # True
a = x > 6 and x < 12
print(a)


x = 6 # False
a = x > 6 and x < 12
print(a)


x = 12
y = 7
b = x > 10 or y > 10
print(b)

x = 12
y = 13
b = x > 10 or y > 10
print(b)

x = False
c = x < 9 or True
print(c)

y = 98
d = y > 99 and False
print(d)

x = 10
e = x > 10 and x < 10 # this will be false for any value
print(e)

x = 0 # it could also be true
f = not x
print(f)

x = 13
y = 90
h = x > 12 and x < 18 or y > 4 and not y < 89
print(h)
