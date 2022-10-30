# JavaScript - Web jQuery

### Mandatory Tasks

***0. JavaScript script that updates the text color of the <header> element to red (#FF0000)***

	* Use document.querySelector to select the HTML tag
	* Don't use the JQuery API

- Test file:
	guillaume@ubuntu:~/0x15$ cat 0-main.html 
	<!DOCTYPE html>
	<html lang="en">
	  <head>
	    <title>Holberton School</title>
	  </head>
	  <body>
	    <header> 
	      First HTML page
	    </header>
	    <footer>
	      Holberton School - 2017
	    </footer>
	    <script type="text/javascript" src="0-script.js"></script>
	  </body>
	</html>
	guillaume@ubuntu:~/0x15$ 

***1. JavaScript script that updates the text color of the <header> element to red (#FF0000):***

	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:
	guillaume@ubuntu:~/0x15$ cat 1-main.html 
	<!DOCTYPE html>
	<html lang="en">
	  <head>
	    <title>Holberton School</title>
	    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	  </head>
	  <body>
	    <header> 
	      First HTML page
	    </header>
	    <footer>
	      Holberton School - 2017
	    </footer>
	    <script type="text/javascript" src="1-script.js"></script>
	  </body>
	</html>
	guillaume@ubuntu:~/0x15$ 

***2. JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:***

	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:
	guillaume@ubuntu:~/0x15$ cat 2-main.html 
	<!DOCTYPE html>
	<html lang="en">
	  <head>
	    <title>Holberton School</title>
	    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	  </head>
	  <body>
	    <header> 
	      First HTML page
	    </header>
	    <div id="red_header">Red header</div>
	    <footer>
	      Holberton School - 2017
	    </footer>
	    <script type="text/javascript" src="2-script.js"></script>
	  </body>
	</html>
	guillaume@ubuntu:~/0x15$

***3. JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header***

	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:- Test file:
	guillaume@ubuntu:~/0x15$ cat 3-main.html 
	<!DOCTYPE html>
	<html lang="en">
	  <head>
	    <title>Holberton School</title>
	    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	    <style>
	      .red {
	        color: #FF0000;
	      }
	    </style>
	  </head>
	  <body>
	    <header> 
	      First HTML page
	    </header>
	    <div id="red_header">Red header</div>
	    <footer>
	      Holberton School - 2017
	    </footer>
	    <script type="text/javascript" src="3-script.js"></script>
	  </body>
	</html>
	guillaume@ubuntu:~/0x15$ 

***4. JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:***

	* The <header> element must always have one class: red or green, never both in the same time and never empty.
	* If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:- Test file:
	guillaume@ubuntu:~/0x15$ cat 4-main.html 
	<!DOCTYPE html>
	<html lang="en">
	  <head>
	    <title>Holberton School</title>
	    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
	    <style>
	      .red {
	        color: #FF0000;
	      }
	      .green {
	        color: #00FF00;
	      }
	    </style>
	  </head>
	  <body>
	    <header class="green"> 
	      First HTML page
	    </header>
	    <div id="toggle_header">Toggle header</div>
	    <footer>
	      Holberton School - 2017
	    </footer>
	    <script type="text/javascript" src="4-script.js"></script>
	  </body>
	</html>
	guillaume@ubuntu:~/0x15$ 
