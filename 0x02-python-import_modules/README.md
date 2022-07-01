**IMPORT & MODULES README**

0. Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
	* use print function with string format to display integers
	* assign:
		* the value 1 to a variable called a
		* the value 2 to a variable called b
		* and use those two variables as arguments when calling the functions add and print
	* a and b must be defined in 2 different lines: a = 1 and another b = 2
	* The program should print: <a value> + <b value> = <add(a, b) value> followed with a new line.
	* Only use the word add_0 once in your code
	* Don't use * for importing or __import__
	* The code should not be executed when imported - by using __import__

1. Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
	* Do not use the function print (with string format to display integers) more than 4 times
	* define:
		* the value 10 to a variable a
		* the value 5 to a variable b
		* and use those two variables only, as arguments when calling functions (including print)
	* a and b must be defined in 2 different lines: a = 10 and another b = 5
	* The program should call each of the imported functions. See example below for format
	* the word calculator_1 should be used only once in your file
	* Don't use * for importing or __import__
	* The code should not be executed when imported

2. Write a program that prints the number of and the list of its arguments.
	* The output should be:
		* Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
		* : (or . if no arguments were passed) followed by
		* a new line, followed by (if at least one argument),
		* one line per argument:
	* the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
	* The code should not be executed when imported
	* The number of elements of argv can be retrieved by using: len(argv)

3. Write a program that prints the result of the addition of all arguments
	* The output should be the result of the addition of all arguments, followed by a new line
	* You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
	* The code should not be executed when imported

4. Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).
	* Print one name per line, in alpha order
	* Print only names that do not start with __
	* The code should not be executed when imported

5. Write a program that imports the variable a from the file variable_load_5.py and prints its value.
	* Don't use * for importing or __import__
	* The code should not be executed when imported
