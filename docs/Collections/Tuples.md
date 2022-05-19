Tuples are a group of multiple items stored in a single variable.

```
t1 = (1, 2)

t2 = ('x', 2, 'y')
```

Tuples cannot be changed as we change lists and dictionaries.

They are useful if we want to send multiple variables from a function.

```
def send_three_items():
    return (1, 2, 3)
```

Also when we go through a dictionary, we receive a tuple (key, value)

```
dict = {'key1': 1, 'key2': 2}

# dict.items() returns a list of tuples and we access 2 params at once
for key, value in dict.items():
    print(key)
    print(value)
```

More examples: https://www.programiz.com/python-programming/tuple