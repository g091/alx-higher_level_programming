# SQL More Queries README.

#### Mandatory Tasks

***.0 Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).***

***1. Write a script that creates the MySQL server user user_0d_1***

	- user_0d_1 should have all privileges on your MySQL server
	- The user_0d_1 password should be set to user_0d_1_pwd
	- If the user user_0d_1 already exists, your script should not fail

***2. Write a script that creates the database hbtn_0d_2 and the user user_0d_2***

	- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
	- The user_0d_2 password should be set to user_0d_2_pwd
	- If the database hbtn_0d_2 already exists, your script should not fail
	- If the user user_0d_2 already exists, your script should not fail

***3. Write a script that creates the table force_name on your MySQL server***

	- force_name description:
		* id INT
		* name VARCHAR(256) can’t be null
	- The database name will be passed as an argument of the mysql command
	- If the table force_name already exists, your script should not fail

***4. Write a script that creates the table id_not_null on your MySQL server.***

	- id_not_null description:
		* id INT with the default value 1
		* name VARCHAR(256)
	- The database name will be passed as an argument of the mysql command
	- If the table id_not_null already exists, your script should not fail

***5. Write a script that creates the table unique_id on your MySQL server.***

	- unique_id description:
		* id INT with the default value 1 and must be unique
		* name VARCHAR(256)
	- The database name will be passed as an argument of the mysql command
	- If the table unique_id already exists, your script should not fail

***6. Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.***

	- states description:
		* id INT unique, auto generated, can’t be null and is a primary key
		* name VARCHAR(256) can’t be null
	- If the database hbtn_0d_usa already exists, your script should not fail
	- If the table states already exists, your script should not fail

***7. Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.***

	- cities description:
		* id INT unique, auto generated, can’t be null and is a primary key
		* state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
		* name VARCHAR(256) can’t be null
	- If the database hbtn_0d_usa already exists, your script should not fail
	- If the table cities already exists, your script should not fail

***8. Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.***

	- The states table contains only one record where name = California (but the id can be different, as per the example)
	- Results must be sorted in ascending order by cities.id
	- No use of the JOIN keyword
	- The database name will be passed as an argument of the mysql command

***9. Write a script that lists all cities contained in the database hbtn_0d_usa.***

	- Each record should display: cities.id - cities.name - states.name
	- Results must be sorted in ascending order by cities.id
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***10. Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.***

###### Import the database dump from hbtn_0d_tvshows to your MySQL server (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

	- Each record should display: tv_shows.title - tv_show_genres.genre_id
	- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***11. Write a script that lists all shows contained in the database hbtn_0d_tvshows.***

###### Import the database dump of hbtn_0d_tvshows to your MySQL server (q10)

	- Each record should display: tv_shows.title - tv_show_genres.genre_id
	- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
	- If a show doesn’t have a genre, display NULL
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***12. Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.***

###### Import the database dump of hbtn_0d_tvshows to your MySQL server (q11)

	- Each record should display: tv_shows.title - tv_show_genres.genre_id
	- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***13. Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.***

###### Import the database dump of hbtn_0d_tvshows to your MySQL server (q12)

	- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
	- First column must be called genre
	- Second column must be called number_of_shows
	- Don’t display a genre that doesn’t have any shows linked
	- Results must be sorted in descending order by the number of shows linked
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***14. Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.***

###### Import the database dump of hbtn_0d_tvshows to your MySQL server (q13)

	- The tv_shows table contains only one record where title = Dexter (but the id can be different)
	- Each record should display: tv_genres.name
	- Results must be sorted in ascending order by the genre name
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***15. Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.***

###### Import the database dump of hbtn_0d_tvshows to your MySQL server (q14)

	- The tv_genres table contains only one record where name = Comedy (but the id can be different)
	- Each record should display: tv_shows.title
	- Results must be sorted in ascending order by the show title
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command

***16. Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.***

###### Import the database dump of hbtn_0d_tvshows to your MySQL server (q15)

	- If a show doesn’t have a genre, display NULL in the genre column
	- Each record should display: tv_shows.title - tv_genres.name
	- Results must be sorted in ascending order by the show title and genre name
	- Use only one SELECT statement
	- The database name will be passed as an argument of the mysql command
