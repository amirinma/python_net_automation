The function os.walk() generates a tuple containing the directory path, directory names, and filenames for or in a given directory. This is useful when you have to do something with files in a directory. Beginning on line 75, indented four spaces, type the following code:
for _ in os.walk('routers'): 
    print(_)

Using an underscore as a variable to represent values that, once used, are not important to the script anymore can help with readability. When you see an underscore used as a variable name, you know that data is not important in general or at that stage of computation.
