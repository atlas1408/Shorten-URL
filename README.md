# URL shortening application
Creating a URL shortening application to simplify accessing complicated URL's.  
Users provide the application with the web URL/ local file URL and corresponding short keyword.  
These keywords are stored in ```urls.json``` and retrieved for future access.  
I built this application using Flask backend and Bootstrap for frontend.

## Table of Contents
1. [Pre-requisite](#pre-requisite)
1. [Implementation](#implementation)
1. [Technologies Used](#technologies-used)

## Pre-requisite
Install requirements.txt using ```pip install -r requirements.txt```.  
requirements.txt includes following libraries:  
- Flask
- Werkzeug
- pytest
- gunicorn


## Implementation
- Clone this respository.

- Change the secret key in __init__.py

- Move into Project(url-shortener) directory.

- Run command: ```export FLASK_APP=urlshort``` 

- Run command: ```flask run```

## Technologies Used
- Flask
- Python
- Bootstrap
- Pytest
- Gunicorn
