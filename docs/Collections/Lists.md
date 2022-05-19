<h2>List</h2>

A list is a collection of data. It can contain all the fundamental data types (bool, int, float & str) and also objects or data types made by us.

```
>>> a = ['foo', 'bar', 'baz', 'qux']

>>> print(a)
['foo', 'bar', 'baz', 'qux']
>>> a
['foo', 'bar', 'baz', 'qux']
>>> empty_list = []

>>> print(empty_list)
[]
```

A list can have elements of different types.

```
>>> a = ['foo', 1, True, Task()]

```

It is recommended that in most cases lists contain only 1 type of element. Thus it is easier to interact with its elements. Lists which contain only 1 type of element are called `cohesive lists`.


Lists are ordered using an index. The index starts from 0 and has no limit, maybe your computer's memory.
```
>>> a = ['foo', 'bar', 'baz', 'qux']
>>> print(a[0])
'foo'
>>> print(a[2])
'baz'

>>> [1, 2, 3, 4] == [4, 1, 3, 2]
False
```

List elements do not need to be unique. You can have the same value multiple times.
```
>>> a = ['c', 'c', 'd']
```


**Slicing**

```
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a[2:5]
['baz', 'qux', 'quux']
>>> a[1:]
['bar', 'baz', 'qux', 'quux', 'corge']
>>> a[:3]
['foo', 'bar', 'baz']
>>>
```

We can also use negative index. For example if we want the list without its last 2 elements
```
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a[:-2]
['foo', 'bar', 'baz', 'qux']
```

**Checking an element is in a list**

```
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> 'qux' in a
True
>>> 23 in a
False
>>> 23 not in a 
True
>>> 'foo' not in a
False
```

**Concatenation & replication**

-> use + for concatenation

-> use *`*`* for replication

```
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a + ['grault', 'garply']
['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'grault', 'garply']
>>> a * 2
['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'foo', 'bar', 'baz',
'qux', 'quux', 'corge']
```

**Adding an element**

-> call function *append* on a list

```
>>> a
['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a.append('z')
>>> a
['foo', 'bar', 'baz', 'qux', 'quux', 'corge', 'z']


```

**Cycling**

-> to go through all the elements in a list, we can use **for**

```
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

for element in a:
    print(element) # will print the element at the current index

```



**More in depth knowledge about lists:**

https://realpython.com/python-lists-tuples/#python-lists

https://docs.python.org/3/tutorial/datastructures.html

https://www.w3schools.com/python/python_lists.asp

