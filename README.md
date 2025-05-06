# food-recipe-app

## General Info
This application is a recipe database website. Authorized users can create, delete, and view recipes. The recipe database can be seen by any authorized users.
	
## Technologies
This project is created with:
* Flask version: 2.0.1
* Flask-SQLAlchemy version: 2.5.1
* Flask-WTF version: 0.15.1
* Flask-Login version: 0.5.0
	
## Setup
To run this project, create a virtual evironment:
```
$ python3 -m venv venv
```
Activate the virtual environment macOS / Linux:
```
$ source venv/bin/activate
```
Activate the virtual environment Windows (cmd / PowerShell):
```
$ .\venv\Scripts\activate
```

Install the necessary libraries from [Technologies](#technologies) using:
```
$ pip install -r requirements.txt
```
Then run the application using:
```
$ flask run
```