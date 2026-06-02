variables are used to store data.
Its a name given to memory.
Naming variables - 
  - Names contain letter digit and underscore
  - first character cannot be a digit.
  - Names are Case- sensitive so Myvar and myvar treated different.
  - keywords cannot be used as variable name.
Global and local variables in python 

variable defined inside function or block called local variable there scope is limited to that function they are not accessbile outside of a function.

def greet():
  msg = "greet from function"
  print(msg)

greet()

Global variable - global variables declared outside function and can be access anywhere in the program, including inside function.

If global and local variables have the same name local variable shadows global variable inside function 
  we cant modify global variable inside function if want to do need to declare it as global there otherwise it will throw error.
