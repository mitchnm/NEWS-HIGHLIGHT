# NEWS-HIGHLIGHT
News highlight is an application that gives a user an easy time locating the kind of news they
want to follow up on by the category or by the source

#### Author
*Bright Mukonesi*
#### Date made
*17/5/2019*

## Technologies used
1. Python3.7
2. Html
3. Bootstrap
4. Python extensions
5. Flask

## Using the application
* You require a minimum python version 3.6 to run the application on your local machine
* clone the repository and get to install flask using _git clone https://github.com/Brightmuk/News-highlight_
* Run the application using _./start.sh_ command
* Click on the link on the terminal as you press ctrl and use the application in the browser

##### Creating a virtual environment
* sudo apt-get install python3.6-venv
* python3.6 -m venv virtual
* source virtual/bin/activate
##### Installing dependencies
pip install -r requirements
##### Running Tests
python -m unittest tests/test_models.py
##### Running in development
python run.py
Open the app on your browser, by default on 127.0.0.1:5000.

Deploying to heroku
Make sure you have requirements.txt
# should be in virtual
* pip freeze > requirements.txt
* create a Procfile with the following content
* web: gunicorn 'app:create_app()' --access-logfile - --error-logfile -
* If deploying for the first time, make sure you have heroku cli installed then create app by running
heroku create appname
* Make sure you have committed all changes then run
* git push heroku master

###LICENSE
