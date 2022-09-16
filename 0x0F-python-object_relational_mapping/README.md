# Object-relational Mapping README.

#### Mandatory Tasks

***0. Write a script that lists all states from the database hbtn_0e_0_usa:*** 

	* The script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
	* Must use the module MySQLdb (import MySQLdb)
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by states.id
	* The code should not be executed when imported

***1. Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:***

	* The script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
	* Must use the module MySQLdb (import MySQLdb)
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by states.id
	* The code should not be executed when imported

***2. Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.***

	* The script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
	* Must use the module MySQLdb (import MySQLdb)
	* The script should connect to a MySQL server running on localhost at port 3306
	* Must use format to create the SQL query with the user input
	* Results must be sorted in ascending order by states.id
	* The code should not be executed when imported

***3. Write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!***

	* The script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
	* Must use the module MySQLdb (import MySQLdb)
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by states.id
	* The code should not be executed when imported

***4. Write a script that lists all cities from the database hbtn_0e_4_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module MySQLdb (import MySQLdb)
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by cities.id
	* Use only execute() once
	* The code should not be executed when imported

***5. Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa***

	* The script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
	* Must use the module MySQLdb (import MySQLdb)
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by cities.id
	* Use only execute() once
	* The code should not be executed when imported

***6. Write a python file that contains the class definition of a State and an instance Base = declarative_base():***

	* State class:
		* inherits from Base Tips
		* links to the MySQL table states
		* class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		* class attribute name that represents a column of a string with maximum 128 characters and can’t be null
	* Must use the module SQLAlchemy
	* The script should connect to a MySQL server running on localhost at port 3306
	* WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)

***7. Write a script that lists all State objects from the database hbtn_0e_6_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by states.id
	* The code should not be executed when imported

***8. Write a script that prints the first State object from the database hbtn_0e_6_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* The state you display must be the first in states.id
	* Don't fetch all states from the database before displaying the result
	* The results must be displayed as they are in the example below
	* If the table states is empty, print Nothing followed by a new line
	* The code should not be executed when imported

***9. Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by states.id
	* The results must be displayed as they are in the example below
	* The code should not be executed when imported

***10. Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa***

	* The script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* Assume you have one record with the state name to search
	* Results must display the states.id
	* If no state has the name you searched for, display Not found
	* The code should not be executed when imported

***11. Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* Print the new states.id after creation
	* The code should not be executed when imported

***12. Write a script that changes the name of a State object from the database hbtn_0e_6_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* Change the name of the State where id = 2 to New Mexico
	* The code should not be executed when imported

***13. Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa***

	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* The code should not be executed when imported

***14. Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.***

	* City class:
		* inherits from Base (imported from model_state)
		* links to the MySQL table cities
		* class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		* class attribute name that represents a column of a string of 128 characters and can’t be null
		* class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
	* Must use the module SQLAlchemy

	Write a script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa:
	
	* The script should take 3 arguments: mysql username, mysql password and database name
	* Must use the module SQLAlchemy
	* Must import State and Base from model_state - from model_state import Base, State
	* The script should connect to a MySQL server running on localhost at port 3306
	* Results must be sorted in ascending order by cities.id
	* The code should not be executed when imported	
