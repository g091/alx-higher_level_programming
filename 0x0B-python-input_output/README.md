# Input/Output README.

**Mandatory Tasks**

***0. Write a function that reads a text file (UTF8) and prints it to stdout***

	* Prototype: def read_file(filename=""):
	* You must use the with statement
	* No need to manage file permission or file doesn't exist exceptions.
	* No importing modules

***1. Write a function that writes a string to a text file (UTF8) and returns the number of characters written***

	* Prototype: def write_file(filename="", text=""):
	* You must use the with statement
	* You don’t need to manage file permission exceptions.
	* The function should create the file if doesn’t exist.
	* The function should overwrite the content of the file if it already exists
	* No importing modules

***2. Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added***

	* Prototype: def append_write(filename="", text=""):
	* If the file doesn’t exist, it should be created
	* You must use the with statement
	* No need to manage file permission or file doesn't exist exceptions
	* No importing modules

***3. Write a function that returns the JSON representation of an object (string)***

	* Prototype: def to_json_string(my_obj): 
	* No need to manage exceptions if the object can’t be serialized

***4. Write a function that returns an object (Python data structure) represented by a JSON string***

	* Prototype: def from_json_string(my_str):
	* No need to manage exceptions if the JSON string doesn’t represent an object.

***5. Write a function that writes an Object to a text file, using a JSON representation***

	* Prototype: def save_to_json_file(my_obj, filename):
	* You must use the with statement
	* No need to manage exceptions if the object can’t be serialized
	* No need to manage file permission exceptions.

***6. Write a function that creates an Object from a “JSON file***

	* Prototype: def load_from_json_file(filename):
	* You must use the with statement
	* No need to manage exceptions if the JSON string doesn’t represent an object.
	* No need to manage file permissions / exceptions.

***7. Write a script that adds all arguments to a Python list, and then save them to a file***

	* You must use your function save_to_json_file from 5-save_to_json_file.py
	* You must use your function load_from_json_file from 6-load_from_json_file.py
	* The list must be saved as a JSON representation in a file named add_item.json
	* If the file doesn’t exist, it should be created
	* No need to manage file permissions / exceptions.

***8. Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object***

	* Prototype: def class_to_json(obj):
	* obj is an instance of a Class
	* All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
	* No importing modules

***9. Write a class Student that defines a student by***

	* Public instance attributes:
		* first_name
		* last_name
		* age
	* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	* Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
	* No importing modules

***10. Write a class Student that defines a student by: (based on 9-student.py)***

	* Public instance attributes:
		* first_name
		* last_name
		* age
	* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	* Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
		* If attrs is a list of strings, only attribute names contained in this list must be retrieved.
		* Otherwise, all attributes must be retrieve
	* No importing modules

***11. Write a class Student that defines a student by: (based on 10-student.py)***

	* Public instance attributes:
		* first_name
		* last_name
		* age
	* Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
	* Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
		* If attrs is a list of strings, only attributes name contain in this list must be retrieved.
		* Otherwise, all attributes must be retrieved
	* Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
		* Assume json will always be a dictionary
		* A dictionary key will be the public attribute name
		* A dictionary value will be the value of the public attribute
	* No importing modules

***12. Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n***

	* Returns an empty list if n <= 0
	* Assume n will be always an integer
	* No importing modules
