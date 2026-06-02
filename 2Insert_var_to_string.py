The goal is to insert a variable into a string in python.
eg . if we have variable containing the word "hello" and another containing "world". We want to combine them into a single string 
"Hello World". Lets explore different method to insert variables into string.

Using fString
fstring - its a formatted string literal were introduce in python 3.6 and have quickly become most recommended way to insert variables
into string 

a = "python"
res = f"This is {a} programming"
print(res)

#Using format method 
Before fstring, the .format() method was standard way to insert variable into string 
it was widely used in projects required compatibility with python 3.6 version

Using + operator 
+ operator is a basic method to combine strings and variables but it can be messy with multiple variables or different data types
a = "hello"
b= "world"
res = a+" "+b
print(res)

- Using % formatting 
this method was used in earlier versions of python and still supported, but its less preferred today due to better alternative like 
format() and f-string()
a = "Python"
res = "This is %s programming!" %a
print(res)
