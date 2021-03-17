# Hydro-api
[Currently under development]
## Install Dependencies
```
pip install -r requirements.txt
```
## Running the app

Run main.py to launch the flask server at http://127.0.0.1:5000/

## Endpoints

API documentation will soon be available via swagger. All data is returned in json format. Currently the exposed endpoints are as follows:
* /health
    - Returns "health" if app is running properly
* /ec
    - Get all the current electrical conductivity sensor logs
    - Post new electrical conductivity readings
* /ec/log_id
    - Get an ec reading by ID
* /ph
    - Get all the current ph sensor logs
    - Post new ph readings
* /ph/log_id
    - Get a ph reading by ID
* /temp
    - Get all the current temperature sensor logs
    - Post new temperature readings
* /temp/log_id
    - Get a temperature reading by ID


## Architecture
This app uses mainly the following packages:
* flask
    - The main framework used to create the application
* flask-restx
    - A flask extension that adds support for the API features
* sqlalchemy and flask-sqlalchemy
    - Adds pythonic ways to communicate with our database
* marshmallow
    - Adds data serilization and validation via schemas

The structure of the application follows flask-restx reccomendations found [here](https://flask-restx.readthedocs.io/en/latest/scaling.html)


## Database
A local sqlite database is used for data storage. To see the database schema please see app/apis/resources/models.py.

