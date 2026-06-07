Abstraction - 
Abstraction is nothing but selective ignorance or we can say hiding of a data.

It is process in which we are showing only essential details and hiding unessential details.

In python abstract base class is essential to achieve data abstraction by defining common interface for its derived class .

Abstraction in python is made up of key components like abstract method, concreate method, abstract properties and class instantiation rule.

Abstract method - abstract method are method without body present in base class they act as place holder and force subclasses to provide own specific implimentation.

Eg 

from abc import ABC, abstractmethod
Class Animal (ABC):
	@abstractmethod
	Def make_sound(self):
		pass:  #abstract method no implimentation here
		
Concrete Method  - 
	Concreate method are fully implimented method within abstract class . Subclasses can inherit and use them directly
	
	Eg
	From abc import ABC, abstractmethod
	Class Animal(ABC):
	@abstractmethod
	Def make_sound(self):
		Pass: #abstract method to be Implimeted by subclass
	
	Def move(self):
		Return "moving" #concrete method 
		
Abstract Property  

		Abstract properties work like abstract methods but are used for properties.
		These properties are declare with @property decorator and marked as abstract using @abstractmethod. Subclasses must implement these properties 
		
		
Abstract class Instantiation   
		Abstract class can not be implimented directly. This is because they contain one or more abstract method or properties that lack implementations.
		Attempting to instantiation  Abstract class result in type error.
		  
