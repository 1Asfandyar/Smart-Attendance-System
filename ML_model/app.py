import os
from dotenv import load_dotenv
from flask import Flask, jsonify

from log import debug, info, warning, error
from req_handler import present_students

load_dotenv()
PORT = os.getenv('PORT')

app = Flask(__name__)
app.register_blueprint(present_students, url_prefix='/')

# use_reloader → When use_reloader is set to True , 
# the server will automatically restart when code changes. 
# Defaults to False
app.run(host='0.0.0.0', port=PORT, use_reloader=True)