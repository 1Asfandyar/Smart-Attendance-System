import os
from dotenv import load_dotenv
from flask import Flask

from log import debug, info, warning, error
# from home import home_bp

load_dotenv()
PORT = os.getenv('PORT')

app = Flask(__name__)
@app.route('/')
def home():
    return "Home page"
# app.register_blueprint(home_bp, url_prefix='/home')

# use_reloader → When use_reloader is set to True , 
# the server will automatically restart when code changes. 
# Defaults to False
app.run(host='0.0.0.0', port=PORT, use_reloader=True)