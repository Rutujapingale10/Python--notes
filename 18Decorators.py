A decorator is a function that takes another function as an argument and return new function with enhanced functionality.

It is used in scenario such as logging, authentication and memorization, allow us to add additional functionality to existing functions or methods in a clean and reusable way.


Eg.
	def decorator(func):
		def wrapper():
			print("before calling the function")
			func()
			print("After calling the function")
		return wrapper
	@decorator  #applying decorator to function
	def greet():
		print("")
	greet()
	
	- Decorator takes greet function as an argument.
	- It returns a new function(wrapper) that first print a message, calls greet() and then prints another message.
	- @decorator syntax is a shorthand  for greet = decorator(greet)
	
	- Decorator with Parameter
	- Decorator often need to work with function that have arguments.
	- Def decorator_name(func):
		○ Def wrapper(*args,*kwargs
	
		

