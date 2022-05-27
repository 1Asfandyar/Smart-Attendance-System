# %% [markdown]
# <a href="https://colab.research.google.com/github/1Asfandyar/Smart-Attendance-System/blob/flask_api/app.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
# install required pakages
!pip install flask
!pip install flask-ngrok

!pip install face_recognition
!pip install -v --install-option="--no" --install-option="DLIB_USE_CUDA" dlib
!pip install mtcnn

# %%
# if you are surving HTML content then you need to run this
# downloading, extracting, and saving configs ngrok
!wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
!tar -xvzf ngrok-v3-stable-linux-amd64.tgz
!./ngrok config add-authtoken 29ifuhUWiH23ARpVC0PyPdnBSrj_4q2eJgbA1qthKRH4LevY
! rm *.tgz*

# %%
import os
from flask import Flask, jsonify, request

from flask import Flask
from flask_ngrok import run_with_ngrok

# %%
# please first uploade all file from helper folder
# and updated_ml_function.py from ML_model foler

# %%
from log import debug, info, warning, error
from req_handler import present_students
from decode_img import decode
from encode_img import encode
from ML_Model_Function import takeAttendence, readPickleEncodingsFromFile

# %%
from google.colab import drive
drive.mount('/content/drive')

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

# %%



