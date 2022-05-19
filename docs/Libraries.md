A library is a piece of code external to the program. Some libraries are built into python (`json`, `sys`, `os`, `time` etc) and others are external. Libraries are very useful because we can import the work of others and not have to reinvent the wheel. We can even make a library ourselves if we have the same code in multiple projects.

Python libraries are found here: https://pypi.org/

They can be installed using `pip` 

```
pip install requests
```

This will install the package and make it available on the whole system. This may not be the best solution if we have multiple projects because we can create dependency isssues. We can create a virtual python environment for each project and install only its dependencies in its folder.

```
# go in your project's folder
cd my_project/

# create a new venv, you have to give a name to the venv folder; it can be anything, usually it is env or venv
python -m venv env/

# activate the venv
# on linux
source env/bin/activate
# on windows, I hope this is right :))
env\Scripts\activate.bat

# install your packages, these will be installed only in this folder
pip install requests
pip install fastapi
pip install uvicorn

# save your dependencies, the packages will not be pushed in the code; if another person works on the project he will clone the repo and just do a pip install
pip freeze > requirements.txt

# to exit the venv
deactivate

```

Additional resources:
https://docs.python.org/3/tutorial/venv.html
https://realpython.com/python-virtual-environments-a-primer/

There are also new python applications which manage libraries, but all of them are based on this solution built in python. One to notice and maybe checkout is poetry https://python-poetry.org/.