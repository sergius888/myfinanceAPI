We can read and write to files. For this we can use an object already defined in Python, `File`. To obtain this object we use the function `open` .

**To read from a file**
```
file = open("path/to/file") # opened the file for reading
file_contents = file.read() # we will get the file's content as string
```

**To write in a file**
```
file = open("path/to/file", "w") # opened the file for writing
file.write("new stuff") # this will overwrite the file's content and the file will contain only what we give to the write method
```

**To add to a file**
```
file = open("path/to/file", "a") # opened the file for appending, everything we write will go at the end of the file without modifying what we currently have
file.write("a line\n")
file.write("2nd line\n") # the file will have both lines
```

