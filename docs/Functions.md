-> we can group multiple lines of code into a function so we can call that code from multiple places

```
>>> def function():
...     print('hello')
... 
>>> function()
hello
```

-> functions can receive multiple params

```
>>> def hello(first_name, last_name):
...     print(f"Hello {first_name} {last_name}")
... 
>>> hello('R', 'J')
Hello R J
```

-> functions can return values

```
>>> a = hello('R', 'J')
>>> print(a)
None
>>> def ret():
...     return 2
... 
>>> x = ret()
>>> print(x)
2
```

**More info about functions**

https://www.geeksforgeeks.org/functions-in-python/

https://www.programiz.com/python-programming/function

https://www.tutorialspoint.com/python/python_functions.htm

https://www.guru99.com/functions-in-python.html

https://docs.python.org/3/library/functions.html