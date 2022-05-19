**Logging**
Logs are used for tracking what our application is doing and what errors it encounters. We can come at a later date & inspect problems so we can solve bugs.

```
import logging # logging is the python module used for logs

# we can configure multiple sutff, one is in which file to log (or files)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

# there are 5 levels of logging debug, info, warning, error & critical
logging.debug("Detailed message intented mostly for developers")
logging.info("General info about what action we are currently starting/finishing")
logging.warning("Some problem was encountered, but we were able to finish the task")
logging.error("Failed to do an action, maybe failed to add a new user")
logging.critical("Something bad happened, our whole app may stop")
```

**More info**
https://docs.python.org/3/howto/logging.html
https://realpython.com/python-logging/


**Formatting**

The code should be in all files in the same format. This makes reading and writing the code easier. Python has a standard format. Code will work even if not respecting the format, but your programmer life will be easier.

A good tool to format he code is `black`. https://pypi.org/project/black/

Python format standard: https://peps.python.org/pep-0008/

**Comments**
```
# this is a comment, this line will be ignored by the python interpreter

# can have multiple lines
# commented in a row
# comments are just for documenting things, most important WHY (not how)

"""
You
can write
on
multiple
lines
with 3 double quotes
"""
```