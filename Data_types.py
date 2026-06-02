In python everything treated as object each value belong to specific data types 
the following are standard or built in data types in python.

  python data types
  Integer - Integer, float complex
  Dictionary, Boolean , set

  sequence data types - string , tuple, list

List - list are ordered and mutable collection used to stored multiple items in a single variable.
elements in a list can be different data types and are accessed using indexing.

a = [1,2,3]
print(a)
b = ["Geek","for","geek",4,5]
print(b[3])
print(b[-3])

Tuples - tuples are ordered and immutable collections used to stored multiple items in a single variable.
once created tuple items can not be modified and accessed using indexing.

Boolean data types - boolean data types represent one of two values

set - set is used to store unique items.
set is unordere element cannot be accessed using indexing. elements are usuaaly accessed by iterating through the set using loop.

s1 = {"a","a","b"}
print(s1)
for i in s1:
  print(i)
  Dictionary - its a key value pair where key should be unique othrwise its override a previous value
  key are case sensetive
  d = {1 : 'geek', 2: 'for', 3:'geek'}
  print(d.get(2))
