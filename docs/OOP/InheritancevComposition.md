**Inheritance**

In OOP we can construct subtypes of a class which *inherit* the data and functions from the parent class.

It is very useful if we have multiple classes which have common code.

```
class Person:
    def __init__(self, name: str, surname: str, email: str, worktype: str):
        self.name = name
        self.surname = surname
        self.email = email
        self.worktype = worktype
	
    def get_name(self) -> str:
        return self.name
	
    def get_worktype(self):
        return self.worktype
	
    def get_a_number(self):
        return 2

# the following class extends Person
class Engineer(Person):
    # we can change the constructor in the child class
    # usually a child class has fewer params because is a subtype, a more specialized version
    def __init__(self, name: str, surname: str, email: str)
        # we can call the parent constructor
        super().__init__(name, surname, email, 'engineering')
	
    # we can override a function from the parent class with a different implementation
    # it is recommended that this method behaves the same way, returns the same type of data or receives the same input of data
    def get_a_number(self):
        return 3

eng = Engineer('name', '2nd name', 'name@mail.com')
# we can call the parent's functions
eng.get_worktype() # will return 'engineering'
eng.get_a_number() # will return 3
```

**Compositon**

Another way to use code from a class in another class is *composition*. This means we have another object as a variable in a class.

```
class Engine:
    def start(self):
        pass
	
    def stop(self):
        pass


class Lights:
    def start(self):
        pass
	
    def stop(self):
        pass


class Car:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()
	
    def start(self):
        self.engine.start()
        self.lights.start()
	
    def stop(self):
        self.engine.stop()
	    self.lights.stop()


my_car = Car() # will create inside an object Engine and an object Ligths
my_car.start() # will call the Engine object's method start, the same for Lights object 
```

https://betterprogramming.pub/inheritance-vs-composition-2fa0cdd2f939

https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)

https://www.thoughtworks.com/insights/blog/composition-vs-inheritance-how-choose
