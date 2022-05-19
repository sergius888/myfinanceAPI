In object oriented programming we define classes & these classes have methods. The methods can be bound to an instance(object) or to the class. 

Every variable in a class initiated with `self` is an instance variable. This means it can be accessed only through the object. If we define a variable outside of the functions without `self` it is a class variable and can be access through the class.

**Example**

```
class A:
    x = 2 # this is a class variable

    def __init__(self, m):
        self.m = m # this is an instance variable

    def f_1(self): #this is an instance method
        return self.m

    @staticmethod 
    def f_2(): # this is a class method
        return A.x
	
    @classmethod
    def f_3(cls): # this is also a class method
        return cls.A


ob1 = A(4)
ob2 = A(6)

# static variables can be accessed through an object or directly through the class
# the variable x is attached to the class, so there is only 1 variable
print(ob1.x) # will print 2 
print(ob2.x) # will print 2
print(A.x) # will print 2

# instance variables are accessed through the object, for each object there is another variable
print(ob1.m) # will print 4
print(ob2.m) # will print 6
print(A.m) # error

# class methods can be called directly on the class or through instances, they can access only static data 
print(ob1.f_2()) # will print 2
print(ob2.f_2()) # will print 2
print(A.f_2()) # will print 2

# instance methods can only be called through objects and they can access the object's own data
print(ob1.f_1()) # will print 4
print(ob2.f_1()) # will print 6
print(A.f_1()) # error

```

**More info**
https://www.pythontutorial.net/python-oop/python-static-methods/
https://www.geeksforgeeks.org/class-method-vs-static-method-python/
