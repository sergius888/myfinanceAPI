<h2>Dictionaries</h2>

A dictionary is a collection of data. It can contain all the fundamental data types (bool, int, float & str) and also objects or data types made by us.

What separates *dicts* from *lists*? Lists' elements are accesed by numeric index (0, 1, 2 ...) while dicts' elements are accesed by keys given by the user.

```
>>> a = {'foo': 'bar', 'baz': 'qux'}
>>> print(a)
{'foo': 'bar', 'baz': 'qux'}
>>> a['foo']
'bar'
>>> a['baz']
'qux'
>>> empty_dict = {}
>>> print(empty_dict)
{}
```

A dict can have elements of different types.

```
>>> a = {'el1': 1, 'boolean_type': True, 'object': Task()}

```

Also the keys can be any type you want. Fundamental types, functions and even classes. Though it is mostly recommended to use only strings.

```
>>> b = {True: 'value', 1: 'numeric index', 2.6: 'even float'}
>>> print(b)
{True: 'numeric index', 2.6: 'even float'}
```

A dictionary can also be constructed with the built-in function `dict()`.

**Adding an element**

-> simply assign a new key to the dictionary

```
>>> print(a)
{'foo': 'bar', 'baz': 'qux'}
>>> a['new_key'] = 'new-value'
>>> print(a)
{'foo': 'bar', 'baz': 'qux', 'new_key': 'new-value'}
```

If the key already exists, it will replace the current value.

**Deleting an element**

-> use `del` statement

```
>>> print(a)
{'foo': 'bar', 'baz': 'qux', 'new_key': 'new-value'}
>>> del a['foo']
>>> print(a)
{'baz': 'qux', 'new_key': 'new-value'}
```

**Checking an element is in a list**

```
>>> print(a)
{'baz': 'qux', 'new_key': 'new-value'}
>>> print('baz' in a) # checking a key is in dict
True
>>> print('qux' in a.values()) # checking a value is in dict
True
```

**Cycling**

-> to go through all the elements in a list, we can use **for** and call `.items()` on dict

```
>>> for key,value in a.items():
...     print(key)
...     print(value)
... 
baz
qux
new_key
new-value
```

dict.keys() -> will return all the keys as a list

dict.values() -> will return all the values as a list

**More in depth knowledge about dicts:**

https://realpython.com/python-dicts/

https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python

https://docs.python.org/3/tutorial/datastructures.html#dictionaries

