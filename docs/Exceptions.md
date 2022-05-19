We have seen that code can go wrong and errors appear (red writing in the console). We do not have to let the user see them or let them stop the execution of the program.

To `catch` them we have the following syntax in Python:

```
try:
    int('aaaa')
except:
    print('we need a int')
```

The syntax above catches ALL exceptions. We can catch specifix exceptions.

```
try:
    int('aaaa')
except ValueError:
    print('it is not a number')
```

We can access the exception as a Python object. This is usually done to retrieve the error message.

```
try:
    int('aaaa')
except ValueError as e:
    print("We could not conver to int. Error message: " + str(e))
```

We can catch multiple exceptions and do different things depending on the failure reason.
```
try:
    request.get("coinmarketcap.com/api/v1/coins")
except ConnectionError as e:
    print("We could not connect to the website. Error message: " + str(e))
except Timeout as e:
    print("The request did not come back after 2min. We'll exit!")
```

We can have code that executes on success & failure too.
```
try:
    request.get("coinmarketcap.com/api/v1/coins")
except Exception as e:
    print("We failed to reach coinmarketcap. Error: " + str(e))
finally:
    print("We print this always. If exception and if no exception too")
```

Exceptions are not raised only by Python, we can create and raise our own.

```
class OurError(Exception):
    def __init__():
        super().__init__("an error message")

raise OurError()
```

**More info about exceptions**

https://www.programiz.com/python-programming/user-defined-exception

https://docs.python.org/3/tutorial/errors.html

https://realpython.com/python-exceptions/

https://www.programiz.com/python-programming/exception-handling
