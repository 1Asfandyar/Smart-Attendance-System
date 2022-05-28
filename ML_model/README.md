# Content
- [Content](#content)
- [Requirments](#requirments)
  - [Using venev](#using-venev)
    - [**Install all the required modules**](#install-all-the-required-modules)
    - [**Update requirements.txt file**](#update-requirementstxt-file)
  - [setup .env file](#setup-env-file)
    - [**using .env file**](#using-env-file)
- [Routes](#routes)
  - ['/'](#)
- [Deployment](#deployment)
- [Useful links](#useful-links)
# Requirments
- setup virtual environment
- - Using venev
- - Using Anaconda
- Install all the required modules
- setup .env file

## Using venev
Create and activate a virtual environment using the following command:
Create virtual environment with 'venv' name.
> python3 -m venv venv

> . .venv/bin/activate

### **Install all the required modules**
> pip3 install -r requirements.txt

### **Update requirements.txt file**
> pip3 freeze > requirements.txt

## setup .env file
App is configured to use environment variables. These can be set directly from terminal or can be setup using .env file.
### **using .env file**
Create a .env file under ML_model
> touch .env

Now set all the required variables in it, below are the list of all the required variables to be set.

- PORT

example of .env file
> PORT=4000

# Routes
All the routes which are available in the app and there functionality
is listed below
## '/'
- GET
# Deployment
All different ways to deploy flask to production is given [here](https://flask.palletsprojects.com/en/2.1.x/deploying/)
# Useful links
[How to Set Environment Variables in Linux](https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/)

[venv docs](https://docs.python.org/3/library/venv.html)

[Basics of README.md files](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

[REST API using Flask](https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24)

[Send Image Files in an API POST request](https://nimesha-dilini.medium.com/send-image-files-in-an-api-post-request-aa1af1c4a7fb)

[Convert image to base64](https://codebeautify.org/image-to-base64-converter)

[Convert base64 to image](https://codebeautify.org/base64-to-image-converter)