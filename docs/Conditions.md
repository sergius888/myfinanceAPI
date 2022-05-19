We can check if a condition is true or false in Python. Many times we will need to different actions depending on a condition.

We use `if` keyword for this -> if <condition>:
```
if today == "Monday":
    print("we have course at ITSchool")
```
All lines which are indented will be executed if the condition is True.


What if we also want to execute code if the condition is False
```
if today == "Monday":
    print("we have course at ITSchool")
else:
    print("we don't have course")
    print("lines in else will execute if the condition in if is False")
```

We can have more ifs chained. We put them in `elif` (else + if)
```
if today == "Monday":
    print("we have course at ITSchool")
elif today == "Wensday":
    print("we also have course")
else:
    print("we don't have course")
```

How to create more complex conditions?

We can have more conditions which must be True. We use `and` keyword for this.
```
if today == "Monday" and hour == "18":
    print("we have course now")
```

We can have more conditions and only one has to be True. We use 'or' keyword
```
if today == "Monday" or today is "Wensday":
    print("we have course today")
```

What if we want to do something only if a condition is False and nothing if it is True? We can write our code in `else`, but our if would be empty. A better solution is to use the `not` keyword.

```
if not False:
    print("we execute some code")
```

To compare 2 things we use `==` or `is`. To negate the comparison we do it like this `!=` or `is not`.
```
if today != "Monday" and today is not "Wensday":
    print("we do not have a course today")
```

Additional resources:

https://docs.python.org/3/tutorial/controlflow.html

https://www.simplilearn.com/tutorials/python-tutorial/python-if-else-statement

https://www.w3schools.com/python/python_conditions.asp

https://www.tutorialspoint.com/python/python_if_else.htm

https://www.programiz.com/python-programming/if-elif-else
