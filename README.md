# SILVEROCELOT

## What is it?
An intentionally vulnerable web application with 4 preexisting vulnerabilities to demonstrate fluency in complex web application security.  
## Design Choices
* Webserver = Apache
* Database = MariaDB
* Performing user requests = CGI/Python
* Displaying content = Javascript/HTML/CSS

We decided to use apache as our main webserver because it is well documented but it also has support for CGI. CGI allows us to, when a user tries to perform an action, call a python script to manipulate the database and display things to the user. This also allows us to work on parts of the website independently as they will be their own python script. Python gives us the flexibility to use any library we require to create the website. Our database of choice is MariaDB to allow us to implement one of the 4 vulnerabilities.

## Preexisting Vulnerabilities
* SQL Injection
* Blind SQL Injection
* Command Injection
* SSRF
