# NEWS-HIGHLIGHT

#### Description

#### By **MITCH MUHU**



## Technologies used
1. Python3.7
2. Html
3. Bootstrap
4. Python extensions
5. Flask

## Using the application
* You require a minimum python version 3.6 to run the application on your local machine
* clone the repository and get to install flask using _git clone "https://github.com/mitchnm/NEWS-HIGHLIGHT.git"
* Run the application using _./start.sh_ command
* Click on the link on the terminal as you press ctrl and use the application in the browser

##### Creating a virtual environment
* sudo apt-get install python3.6-venv
* python3.6 -m venv virtual
* source virtual/bin/activate
### Installing dependencies
pip install -r requirements
### Running Tests
python -m unittest tests/test_models.py
##### Running in development
python run.py
Open the app on your browser, by default on 127.0.0.1:5000.
## Deploying to heroku
* Make sure you have requirements.txt
* should be in virtual
* pip freeze > requirements.txt
* create a Procfile with the following content
* web: gunicorn 'app:create_app()' --access-logfile - --error-logfile -
* If deploying for the first time, make sure you have heroku cli installed then create app by running
heroku create appname
* Make sure you have committed all changes then run
* git push heroku master

### LICENSE
MIT License

Copyright (c) 2019 mitchnm

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.