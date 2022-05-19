**Operators precedence**:
```
() -> Parentheses (grouping)

_f_(args...) -> Function call

_x_[index:index] -> Slicing

_x_[index] -> Subscription

_x.attribute_ -> Attribute reference

** -> Exponentiation

~_x_ -> Bitwise not

+_x_, -_x_ -> Positive, negative

*, /, % -> Multiplication, division, remainder

+, - -> Addition, subtraction

<<, >> -> Bitwise shifts

& -> Bitwise AND

^ -> Bitwise XOR

| -> Bitwise OR

in, not in, is, is not, <, <=,  >,  >=,  <>, !=, == -> Comparisons, membership, identity

not _x_ -> Boolean NOT

and -> Boolean AND

or -> Boolean OR

lambda -> Lambda expression
```

http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html

**Mathematical functions**:

```
import math

math.sqrt(4) # 2, square root (radical)
math.pi # the pi number
math.ceil(6.2) # 7, ceiling returns the bigger integer number (aproximare in sus)
math.floor(6.7) # 6, returns the lower integer number (aproximare in jos)
math.fabs(-5) # 5, returns the absolute value

```

https://docs.python.org/3/library/math.html
https://stackabuse.com/the-python-math-library/

**Random library**:

We can generate (pseudo)random numbers with python. 

```
import random

random.randrang(1, 100, step=1) # returns a random number between 1 and 100
```

More random functions can be found here: https://docs.python.org/3/library/random.html
https://pythonalgos.com/a-comprehensive-guide-to-the-python-random-library/

**Lambda functions** (anonymous short functions):
```
def plusone(x):
    return x + 1

pluseonelambda = lambda x: x + 1

plusone(5) # returns 6
plusonelambda(6) # returns 7
```

More info: https://realpython.com/python-lambda/

**Bitewise**: https://realpython.com/python-bitwise-operators/

