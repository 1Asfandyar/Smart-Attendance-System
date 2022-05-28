# %%
import os
from flask import Flask, jsonify, request

from flask import Flask
from flask_ngrok import run_with_ngrok
# %%
from log import debug, info, warning, error
from req_handler import present_students
from decode_img import decode
from encode_img import encode
from ML_Model_Function import takeAttendence, readPickleEncodingsFromFile

# %%
Name_list_path = "/content/drive/MyDrive/ML_Project/StudentName.pkl"
StudentFaces_Encoding_path = "/content/drive/MyDrive/ML_Project/StudentEncoding.pkl"

# %%
Name_list = readPickleEncodingsFromFile(Name_list_path)
StudentFaces_Encoding = readPickleEncodingsFromFile(StudentFaces_Encoding_path)

# %%
app = Flask(__name__)
run_with_ngrok(app)   

@app.route("/")
def home():
  body = request.get_json()
  img = decode(body["class_img"])
  headers = request.headers
  return jsonify(takeAttendence(Name_list, StudentFaces_Encoding, img))

app.run()