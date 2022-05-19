Object oriented programming revolves around classes and objects. Classes provide a way of binding data and functionality toghether. We can bind variables and functions together.

Creating a new class creates a new data type. When we instantiate a class we create an object.

**How to define a class and instantiate an object**

```
# define a class
class ClassName:
    # set the constructor, a function to initialize the data
	# this method is optional
    def __init__(self, x: int, y: str):
        self.x = x
        self.y = y
	
	# define a function which can be called on an object of this class
    def get_y(self) -> str:
        return self.y
	
	# define a function with a param
    def set_x(self, new_value: int):
        self.x = new_value
		
	# define a static method, a method which is called on the class
	# can be called on an object, but also directly on the class
    
    @staticmethod
    def static_method():
        print('hello')
 
 
#define a class without a constructor
class ClassWithoutInit:
    pass
 
 
object = ClassName(1, 'string')
print(object.get_y()) # will print the value of object's y, string'
object.set_x(6)
print(object.x) # will print the value of object's x, 6
 
ClassName.static_method() # will print 'hello'
 
another_object = ClassWithoutInit() # instantiate a class without constructor
```


**Getters and setters**
Usually the data from a class is tagged as private. To read it we create a `get` method and to modify it we use `set`.

```
class Example:
    def __init__(self, x, y):
        self.__x = x # we use two underscores __ to mark the data as private
        self.__y = y # if private it should not be called from outside the class

    def get_x(self): # this is the classic method get, we can modify or do checks
        return self.__x

    def set_x(self, new_value): # the classis set, we can do checks before we update
        self.__x = new_value

    @property
    def y(self): # the more modern python way for getter
        return self.__y 

    @y.setter
    def y(self, new_value): # the more modern python way for setter
        self.__y = new_value


e = Example("a", "b")

print(e.y) # will print b, will execute the method y(self)
e.y = "c" # __y will become "c", the method y(self, new_value) will be executed
```

More info:

https://www.programiz.com/python-programming/class

https://www.w3schools.com/python/python_classes.asp