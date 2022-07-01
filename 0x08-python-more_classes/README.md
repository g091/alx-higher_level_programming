# More Classes & Objects README.

**MANDATORY TASKS**

***0. Write an empty class Rectangle that defines a rectangle***
	
	* No importing modules

***1. Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
		* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* No importing modules

***2. Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
		* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter is equal to 0
	* No importing modules

***3. Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character #: (see example below)
		* if width or height is equal to 0, return an empty string
	* No importing modules.

***4. Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character #: (see example below)
		* if width or height is equal to 0, return an empty string
	* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval() (see example below)
	* No importing modules

***5. Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character #:
		* if width or height is equal to 0, return an empty string
	* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
	* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
	* No importing modules

***6. Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Public class attribute number_of_instances:
		* Initialized to 0
		* Incremented during each new instance instantiation
		* Decremented during each instance deletion
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character #:
		* if width or height is equal to 0, return an empty string
	* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
	* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
	* No importinng modules

***7. Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Public class attribute number_of_instances:
		* Initialized to 0
		* Incremented during each new instance instantiation
		* Decremented during each instance deletion
	* Public class attribute print_symbol:
		* Initialized to #
		* Used as symbol for string representation
		* Can be any type
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character(s) stored in print_symbol:
		* if width or height is equal to 0, return an empty string
	* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
	* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
	* No importing modules

***8. Write a class Rectangle that defines a rectangle by: (based on 7-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Public class attribute number_of_instances:
		* Initialized to 0
		* Incremented during each new instance instantiation
		* Decremented during each instance deletion
	* Public class attribute print_symbol:
		* Initialized to #
		* Used as symbol for string representation
		* Can be any type
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character #:
		* if width or height is equal to 0, return an empty string
	* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
	* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
	* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
		* rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
		* rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
		* Returns rect_1 if both have the same area value
	* No importing modules

***9. Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)***

	* Private instance attribute: width:
		* property def width(self): to retrieve it
		* property setter def width(self, value): to set it:
			* width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
			* if width is less than 0, raise a ValueError exception with the message width must be >= 0
	* Private instance attribute: height:
		* property def height(self): to retrieve it
		* property setter def height(self, value): to set it:
			* height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
			* if height is less than 0, raise a ValueError exception with the message height must be >= 0
	* Public class attribute number_of_instances:
		* Initialized to 0
		* Incremented during each new instance instantiation
		* Decremented during each instance deletion
	* Public class attribute print_symbol:
		* Initialized to #
		* Used as symbol for string representation
		* Can be any type
	* Instantiation with optional width and height: def __init__(self, width=0, height=0):
	* Public instance method: def area(self): that returns the rectangle area
	* Public instance method: def perimeter(self): that returns the rectangle perimeter:
		* if width or height is equal to 0, perimeter has to be equal to 0
	* print() and str() should print the rectangle with the character #:
		* if width or height is equal to 0, return an empty string
	* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
	* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
	* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
		* rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
		* rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
		* Returns rect_1 if both have the same area value
	* Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size
	* No importing modules

**ADVANCED TASKS**
