Python is a object oriented programming language, allowing you to structure your code using classes and objects for better organisation and reusability

Advantages of OOP - 
- provides a clear structure to a program 
- Makes code easier to maintain and debug
- Allow you to build resusable applications with less code

  Object - 
  In python everything is a object with its properties and method.
  Object is a something which has state behaviour and responsibilities.

  class - class is a blueprit for real world entity.


  class Myclass:
    x = 5 ------->creating class

  p1 = MyClass()
  print(p1.x)


#deleting object 
del p1

Class - 
Class is a way of implimenting incapsulation it is representation of real world intity

It represent blue print for object .it is a collection of object 

In python attributes are always public and represnted by . Operator


Creating class

Class dog:
	Species = "canien" //class atribute 
	
	def __init__(self,age,name):
	Self.name = name  //instance attribute
	Self.age = age
	
	
	__init__ : it is method initialises attributes when object is get created
	
	
Object :
Object is an instance of class. Object is something which has 
State, behaviour, identity and responsibility

Creating object in class
Creating object in class involves instantitating  instance of that class

Class dog:
	Species = "canien"
	
	Def __init__(self,age,name):
		Self.name = name
		Self.age = age
//creating object of that class 
	Dog1  = Dog("Buddy",3)
	
Print(dog1.name)
Print(dog1.age)
-- Self parameter - 
Self parameter is a reference to the current instance of a class
It allow us to access to the current instance of a class.

-- __init__ - this method is constructor in python. It is used to initilize object of class

Class variable -
These are variables inside a class present outside any method. All object of class share same value for class variable unless explicitly overridden by object

Instance variable :
Variable present inside __init__ method or other instance method . Each object consist its own copy of instance variable.  




		
		
	
	  


