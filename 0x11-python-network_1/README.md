# Python - Network #1 README.

### Mandatory Tasks

***0. A Python script that fetches https://alx-intranet.hbtn.io/status***

	* Use the package urllib
	* Don't import any packages other than urllib
	* The body of the response must be displayed like;

		guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
		Body response:$
		    - type: <class 'bytes'>$
		    - content: b'OK'$
		    - utf8 content: OK$
		guillaume@ubuntu:~/0x11$

	* Use a with statement

***1. A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.***

	* Use the packages urllib and sys
	* Don't import packages other than urllib and sys
	* The value of this variable is different for each request
	* No need to check arguments passed to the script (number or type)
	* Use a with statement

***2. A Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)***

	* The email must be sent in the email variable
	* Use the packages urllib and sys
	* Don't import packages other than urllib and sys
	* No need to check arguments passed to the script (number or type)
	* Use a with statement

***3. A Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).***

	* Manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
	* Use the packages urllib and sys
	* Don't import packages other than urllib and sys
	* No need to check arguments passed to the script (number or type)
	* Use a with statement

***4. A Python script that fetches https://alx-intranet.hbtn.io/status***

	* Use the package requests
	* Don't import packages other than requests
	* The body of the response must be display like;

		guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
		Body response:$
		    - type: <class 'str'>$
		    - content: OK$
		guillaume@ubuntu:~/0x11$

***5. A Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header***

	* Use the packages requests and sys
	* Don't import packages other than requests and sys
	* The value of this variable is different for each request
	* No need to check arguments passed to the script (number or type)

***6. A Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.***

	* The email must be sent in the variable email
	* Use the packages requests and sys
	* Don't import packages other than requests and sys
	* No need to check arguments passed to the script (number or type)

***7. A Python script that takes in a URL, sends a request to the URL and displays the body of the response.***

	* If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
	* Use the packages requests and sys
	* Don't import packages other than requests and sys
	* No need to check arguments passed to the script (number or type)

***8. A  Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.***

	* The letter must be sent in the variable q
	* If no argument is given, set q=""
	* If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
	* Else;
		* Display Not a valid JSON if the JSON is invalid
		* Display No result if the JSON is empty
	* Use the packages requests and sys
	* Don't import packages other than requests and sys

***9. A  Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id***

	* Use Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
		Basic Authentication: https://docs.github.com/en/rest/overview/other-authentication-methods
		Personal access token as password: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

	* The 1st argument will be your username
	* The 2nd argument will be your password (personal access token as password)
	* Use the packages requests and sys
	* Don't import packages other than requests and sys
	* No need to check arguments passed to the script (number or type)
