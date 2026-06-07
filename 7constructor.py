Constructor - 
Constructor is a special type of function which gets called automatically at the time of object creation.
For every object constructor gets called seperatly and only once.

The method __new__ is a constructor in class. It create new instance of class while
__init__ is a initializer set up instance attribute after creation.
These methods work together and setup object creation and initialisation.

difference between init and new
__new__ : method 
__new__ in python is a special method thats responsible for actually creating  a new instance of class.

  Its a step where object come into existance, even before it gets initialised with specific value.it gets called before __init__.

__init__ - method 
__init__  is a special method known as initialiser or constructor. It is called automatically when new instance of the class is created.


	There are some types of constructor-
	
	Default constructor - constructor doesn’t take any parameter except self . It is used to initialize object using default values.
	
		Def __init__(self):
			Self.geek = "Geeksforgeeks"
			
	Parameterized constructor - This constructor accepts argument from user and initializes
	The object with those values.
		Def __init__(self,f,s):
		 
		
	__new__ Method - 
		This method is responsible creating new instance of a class. It allocates memory and return new object. It is called before init.
		
	__init__ Method - 
		This method initializes newly created instance and commonly used as constructor in python.
		It is called immediately object created by __new__ method. This method responsible for initializing attributes of instance.
		 



