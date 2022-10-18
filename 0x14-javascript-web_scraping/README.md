#JavaScript - Web scraping README.

### Mandatory Tasks

***0. Script that reads and prints the content of a file***

	* 1st arg. is the file path
	* The content of the file must be read in utf-8
	* If an error occurred during the reading, print the error object 

***1. Script that writes a string to a file.***

	* 1st arg. is the file path
	* 2nd arg. is the string to write
	* The content of the file must be written in utf-8
	* If an error occurred during while writing, print the error object

***2. Script that display the status code of a GET request.***

	* 1st arg. is the URL to request (GET)
	* The status code must be printed like this: code: <status code>
	* Use the module request

***3. Script that prints the title of a Star Wars movie where the episode number matches a given integer.***

	* 1st arg. is the movie ID
	* Use the Star wars API (https://swapi-api.hbtn.io/) with the endpoint https://swapi-api.hbtn.io/api/films/:id
	* Use the module request

***4. Script that prints the number of movies where the character “Wedge Antilles” is present.***

	* 1st arg. is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
	* Wedge Antilles is character ID 18 - the script must use this ID for filtering the result of the API
	* Use the module request

***5. Script that gets the contents of a webpage and stores it in a file.***

	* 1st arg. is the URL to request
	* 2nd arg. is the file path to store the body response
	* The file must be UTF-8 encoded
	* Use the module request

***6. Script that computes the number of tasks completed by user id.***

	* 1st arg. is the API URL: https://jsonplaceholder.typicode.com/todos
	* Only print users with completed task
	* Use the module request
