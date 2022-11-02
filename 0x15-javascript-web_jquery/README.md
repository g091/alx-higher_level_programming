# JavaScript - Web jQuery

### Mandatory Tasks

***0. JavaScript script that updates the text color of the <header> element to red (#FF0000)***

	* Use document.querySelector to select the HTML tag
	* Don't use the JQuery API

- Test file:
	
<pre><code>guillaume@ubuntu:~/0x15$ cat 0-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;0-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
  </div>

  <div class="list-group">

***1. JavaScript script that updates the text color of the <header> element to red (#FF0000):***

	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:
	
<pre><code>guillaume@ubuntu:~/0x15$ cat 1-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;1-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
  </div>

  <div class="list-group">

***2. JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header:***

	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:

<pre><code>guillaume@ubuntu:~/0x15$ cat 2-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;2-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
  </div>

  <div class="list-group">

***3. JavaScript script that adds the class red to the <header> element when the user clicks on the tag DIV#red_header***

	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:- Test file:

<pre><code>guillaume@ubuntu:~/0x15$ cat 3-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;red_header&quot;&gt;Red header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;3-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
  </div>

  <div class="list-group">
  
***4. JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:***

	* The <header> element must always have one class: red or green, never both in the same time and never empty.
	* If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:- Test file:

<pre><code>guillaume@ubuntu:~/0x15$ cat 4-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;style&gt;
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    &lt;/style&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header class=&quot;green&quot;&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;div id=&quot;toggle_header&quot;&gt;Toggle header&lt;/div&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;4-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
  </div>

  <div class="list-group">
  
***5. JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item:***

	* The new element must be: <li>Item</li>
	* The new element must be added to UL.my_list
	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API

- Test file:

<pre><code>guillaume@ubuntu:~/0x15$ cat 5-main.html 
&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;add_item&quot;&gt;Add item&lt;/div&gt;
    &lt;br /&gt;
    &lt;ul class=&quot;my_list&quot;&gt;
      &lt;li&gt;Item&lt;/li&gt;
    &lt;/ul&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;5-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;
guillaume@ubuntu:~/0x15$ 
</code></pre>
  </div>

  <div class="list-group">
  
***6. JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header***
  
  	* Don't use document.querySelector to select the HTML tag
	* Use the JQuery API
  
- Test file:
  
  <pre><code>guillaume@ubuntu:~/0x15$ cat 6-main.html 
  &lt;!DOCTYPE html&gt;
  &lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      First HTML page
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;update_header&quot;&gt;Update the header&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;6-script.js&quot;&gt;&lt;/script&gt;
    &lt;/body&gt;
    &lt;/html&gt;
    guillaume@ubuntu:~/0x15$ 
    </code></pre>
    
    </div>
    
    <div class="list-group">
  
***7. JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json***
  
  	* The name must be displayed in the HTML tag DIV#character
	* Don’t use document.querySelector to select the HTML tag
	* Use the JQuery API
  
- Test file:
  
  <pre><code>guillaume@ubuntu:~/0x15$ cat 7-main.html 
  &lt;!DOCTYPE html&gt;
  &lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars character
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;character&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;7-script.js&quot;&gt;&lt;/script&gt;
  &lt;/body&gt;
  &lt;/html&gt;
  guillaume@ubuntu:~/0x15$ 
  </code></pre>

  </div>

  <div class="list-group">
  
***8. JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json***
  
	* All movie titles must be list in the HTML tag UL#list_movies
	* Don’t use document.querySelector to select the HTML tag
	* Use the JQuery API
  
- Test file:
  
  <pre><code>guillaume@ubuntu:~/0x15$ cat 8-main.html
  &lt;!DOCTYPE html&gt;
  &lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Star Wars movies
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;ul id=&quot;list_movies&quot;&gt;
    &lt;/ul&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;8-script.js&quot;&gt;&lt;/script&gt;
    &lt;/body&gt;
    &lt;/html&gt;
    guillaume@ubuntu:~/0x15$ 
    </code></pre>
    
    </div>
    
    <div class="list-group">
 
***9. JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.***
  
	* The translation of “hello” must be displayed in the HTML tag DIV#hello
	* Don’t use document.querySelector to select the HTML tag
	* Use the JQuery API
	* The script must work when it is imported from the <head> tag.
  
- Test file:
  
  <pre><code>guillaume@ubuntu:~/0x15$ cat 9-main.html 
  &lt;!DOCTYPE html&gt;
  &lt;html lang=&quot;en&quot;&gt;
  &lt;head&gt;
    &lt;title&gt;Holberton School&lt;/title&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-3.2.1.min.js&quot;&gt;&lt;/script&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;9-script.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt; 
      Say Hello!
    &lt;/header&gt;
    &lt;br /&gt;
    &lt;div id=&quot;hello&quot;&gt;&lt;/div&gt;
    &lt;br /&gt;
    &lt;footer&gt;
      Holberton School - 2017
    &lt;/footer&gt;
  &lt;/body&gt;
  &lt;/html&gt;
  guillaume@ubuntu:~/0x15$ 
  </code></pre>

  </div>

  <div class="list-group">


### Advanced Task

***10. JavaScript script that updates the text color of the \<header> element to red (#FF0000)***

	* Use document.querySelector to select the HTML tag
	* Don't use the jQuery API
	* The script must be imported from the <head> tag, not at the end of the HTML
