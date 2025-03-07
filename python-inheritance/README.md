1. What is a superclass, baseclass, or parentclass?
A superclass, baseclass, or parentclass is a class that is inherited from. In object-oriented programming (OOP), a superclass contains common methods and attributes that can be shared with its subclasses. These allow for code reuse and organization of shared functionality.

2. What is a subclass?
A subclass is a class that inherits from another class (the superclass). It can extend or modify the behavior of the superclass. Subclasses inherit attributes and methods from their superclass, and they can also override these methods or add their own unique behavior.

3. How to list all attributes and methods of a class or instance?
You can use the built-in function dir() to list all attributes and methods of a class or instance.

4. When can an instance have new attributes?
An instance can have new attributes at any time, even after the object is created. You can dynamically add attributes to an instance by simply assigning them.

5. How to inherit a class from another?
To inherit a class from another, you specify the superclass inside parentheses when defining the subclass.

6. How to define a class with multiple base classes?
You can inherit from multiple classes by specifying all the base classes in the parentheses, separated by commas. This is called multiple inheritance.

7. What is the default class every class inherits from?
Every class in Python inherits from the built-in object class by default. This is the base class for all new-style classes (introduced in Python 3).

8. How to override a method or attribute inherited from the base class?
You can override a method or attribute by redefining it in the subclass. This allows you to modify or extend the behavior of the superclass methods.

9. Which attributes or methods are available by inheritance to subclasses?
Subclasses inherit all public and protected attributes and methods from the superclass. Private attributes (those prefixed with __) are not directly accessible from subclasses, but they still exist in the parent class and can be accessed via name mangling.

10. What is the purpose of inheritance?
Inheritance allows you to create a new class based on an existing class, enabling code reuse and the creation of hierarchies. The main purposes of inheritance are:

Reusability: Reuse code from the parent class.
Extensibility: Extend the functionality of the parent class.
Specialization: Create specialized subclasses that inherit common functionality from a superclass but implement specific behavior.



EXERCISES


Requirements


Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
All your files must be executable
The length of your files will be tested using wc
Python Test Cases
Allowed editors: vi, vim, emacs
All your files should end with a new line
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
We strongly encourage you to work together on test cases, so that you don’t miss any edge case
Documentation
Do not use the words import or from inside your comments, the checker will think you are trying to import some modules


0. Lookup
mandatory
Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module


1. My list
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module


2. Exact same object
mandatory
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module


3. Same class or inherit from
mandatory
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module


4. Only sub class of
mandatory
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module


5. Geometry module
mandatory
Write an empty class BaseGeometry.

You are not allowed to import any module


6. Improve Geometry
mandatory
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module


7. Integer validator
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module


8. Rectangle
mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator


9. Full rectangle
mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>


10. Square #1
mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented


11. Square #2
mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>