Polymorphism means many forms 

Polymorphism - same msg given to generalize things for same behaviour but iplimented differently is nothing but polymorphism.

Mainly there are two types of polymorphism

Compile time and runtime
Method overloading using *args and **kargs are supported by compile time polymorphism 

Method overriding, duck typing, Operator overloading are falls under runtime polymorphism 

Class Calculator:
	Def add(self, *args):
		return sum(args)

calc = Calculator()
		Print(calc.add(5,10))
		Print(calc.add(5,10,15))
		Print(calc.add(1,2,3,4))
		

		


		

Compile time polymoprphism -
At compile time object decide which function definetion have to bind with object at compile time .
Python using default argument *args/**kwargs

In python method overloading is not supported like C++, java but it can be achieved with the help of default or argument variable 


Class calculator :
	Def multiply(self, a=1, b=1, *args):
	{
		Result = a*b;
		
		For nums in args:
		
		Result = Result* nums
		
		Return result
		
	}
	
	#create object
	Calc = calculator()
	
	#using default argument
	Print(calc.multiply())
	Print(calc.multiply(4))
	
	#using multiple argument
	Print(calc.multiply(2,3))
	
	Print(calc.multiply(2,3,4))
	
	Runtime Polymorphism - 
	
	Object decide at runtime that which method have to bind with object.
	
	Method Overriding, duck typing, Operator overloading falls under runtime polymorphism.
	
	-Method Overriding - Subclass redefine method from its parent class.
	-Duck Typing -  Duck typing in a python is a dynamic typing where type of object or Class is less important than method and properties it has.
	Means instead of checking instance , we can call method we need.
	If the object implements it, it works - regardless of its actual type.
	
	In short it works with any object that has required method.
	
	If an object implements the required method, it works regardless of its type.
	-Operator Overloading - Special Methods(__add__, __sub__,etc)redefines how operators behave for user-defined objects.
	
	Method Overriding eg.
	
	Class Animals:
		Def sound(self):
		Return "generic sound"
		
	Class Dog(Animal):
		Def sound(self):
		Return "Bark"
		
	Class Cat(Animal):
		Def sound(self):
		Return "Meow"
	-Duck Typing
	
		
#polymorphic behaviour

Animal = [Dog(),Cat(),Animal()]

For animal in Animal:
	Print(animal.sound())
	
Polymorphism in built in functions:
Pythons built in functions like len() and max() are polymorphic they work different with different data types 
Print(len("Hello"))
Print(len[1,2,3])


Operator Overloading

In python, same operator (+) can perform different task depending on operand type. This is known as operator overloading.

Print(5+10)
Print("Hello"+"World!")


	
	

 
