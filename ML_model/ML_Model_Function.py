# %%
import face_recognition
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import pickle
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN

# %%
def savePickleEncodingsToFile(file_name:str, py_obj):
  """
  This function saves a Python Object of any type in Pickle encoded form to a file.
  INPUTS:
    file_name:
      name of the file to which encodings have to store.
    py_obj:
      Any Python object which is to be stored in pickle form to the file.
  """
  open_file = open(file_name, "wb")
  pickle.dump(py_obj, open_file)
  open_file.close()

# %%
def readPickleEncodingsFromFile(file_name:str):
  """
  This function read a Pickle encoded file and returns the decoded python object.
  INPUTS:
    file_name:
      name of the file from which encodings have to read.
  OUPUTS:
    returns a python object with decoded pickle file
  """
  open_file = open(file_name, "rb")
  decode_obj = pickle.load(open_file)
  open_file.close()
  return decode_obj

# %%
def encodeToPickleEncodings(py_obj):
  """
  This function returns Pickle encoded form of Python Object.
  INPUTS:
    py_obj:
      Any Python object which is to be encoded in pickle form.
  """
  return pickle.dump(py_obj)

# %%
def decodeFromPickleEncodings(obj):
  """
  This function read a Pickle encoded object and returns the decoded python object.
  INPUTS:
    obj:
      encoded object which is to be decoded.
  OUPUTS:
    returns a python object with decoded pickle file
  """
  return pickle.load(obj)

# %%
def faceEncodings(images):
  """
  this function takes a list of images and return list of encoded images.
  INPUTS:
    images: list of images (numpy array)
  OutPUTS:
    list of encoded images
  """
  encodeList = []
  for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)
  return encodeList

# %%
def EncodeFaces(path_to_std_img_dir, std_names_file_name, std_enc_file_name):
  """
  This function encode all the images in a folder and save the encodings in pickel form to the specified folder.
  INPUTS:
    path_to_std_img_dir: 
      reletive or absolute path to folder in which all the student images are present
    
    std_names_file_name: 
      file name to store all the student names in pickle encoded form 
    
    std_enc_file_name:
      file name to store encodings of students faces in pickle form
  OUPUTS:
    it returns nothing, but save the results to files in pickle form
  """
  
  images = []
  personNames = []
  myList = os.listdir(path_to_std_img_dir)
  for cu_img in myList:
    current_Img = cv2.imread(f'{path_to_std_img_dir}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
  print(personNames)

  savePickleEncodingsToFile(std_names_file_name, personNames)

  encodeListKnown = faceEncodings(images)

  savePickleEncodingsToFile(std_enc_file_name, encodeListKnown)

# %%
def takeAttendenceFromFiles(enc_names_file, enc_std_faces_file, class_room_img):
  """
  This function detects and recongnize faces in the image of whole class and returns a dict with all the present and absent students 
  INPUTS:
  enc_names_file:
    pickle encoded file name which have names of student in it.
  enc_std_faces_file:
    pickle encoded file name which have all the face encodings of students in it.
  class_room_img:
    a camera taken image file of the whole class for attendence.
  OUTPUTS:
    it returns the dict object like
    {
      'total_detected_stds':21,
      'present_stds':[{name:'name', id:'id', status:'present'}],
      'absent_stds':[{name:'name', id:'id', status:'absent'}]
    }
  """

  personNames = readPickleEncodingsFromFile(enc_names_file)

  encodeListKnown = readPickleEncodingsFromFile(enc_std_faces_file)

  image = face_recognition.load_image_file(class_room_img)


  detector = MTCNN()

  faces = detector.detect_faces(image)

  face_location1 = []
  for face in faces:
    x,y,w,h = face['box']

    x1 = y
    w1 = y+h
    h1 = x
    y1 = x+w

    a = (x1, y1, w1, h1)
    face_location1.append(a)


  encodesCurrentFrame = face_recognition.face_encodings(image, face_location1)
  total_faces = len(face_location1)
  print('Total Faces detected: ', total_faces)

  Name_Dist = {}
  Not_sure = []
  for encodeFace, faceLoc in zip(encodesCurrentFrame, face_location1):
          matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
          
          faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
          matchIndex = np.argmin(faceDis)
          match_threshold = np.min(faceDis)
          if faceDis[matchIndex] < 0.50:
              name = dec_names_lst[matchIndex].upper()
              Name_Dist[name] = [match_threshold,faceLoc]
          else:
              name = dec_names_lst[matchIndex].upper()
              
              if name not in Not_sure:
                if name not in Name_Dist:

                  enc = (name, match_threshold,faceLoc)
                  Not_sure.append(enc)

  NOT_SURE_DIST = {}

  for Face in Not_sure:
    
    Name = Face[0]
    if Name not in Name_Dist:
      prop = []
      prop.append(Face[1])
      for temp_Face in Not_sure:
        if Name == temp_Face[0]:
          prop.append(Face[1])
      min = np.min(prop)

      for temp in Not_sure:
        if temp[0] == Name and temp[1] == min:
          NOT_SURE_DIST[Name] = [temp[1] ,temp[2]]

  return {'total_detected_stds':total_faces,
        'present_stds':list(Name_Dist),
        'absent_stds':list(NOT_SURE_DIST)}

# %%
def takeAttendence(dec_names_lst, dec_std_faces, dec_class_room_img):
  """
  This function detects and recongnize faces in the image(as numpy array) of whole class and returns a dict with all the present and absent students 
  INPUTS:
  dec_names_lst:
    a lsit of names fo students.
  dec_std_faces:
    list of students face encodings (not pickled form) but from face_recog lib.
  dec_class_room_img:
    image file of the whole class for attendence in numpy array form.
  OUTPUTS:
    it returns the dict object like
    {
      'total_detected_stds':21,
      'present_stds':[{name:'name', id:'id', status:'present'}],
      'absent_stds':[{name:'name', id:'id', status:'absent'}]
    }
  """

  detector = MTCNN()

  faces = detector.detect_faces(dec_class_room_img)

  face_location1 = []
  for face in faces:
    x,y,w,h = face['box']

    x1 = y
    w1 = y+h
    h1 = x
    y1 = x+w

    a = (x1, y1, w1, h1)
    face_location1.append(a)


  encodesCurrentFrame = face_recognition.face_encodings(dec_class_room_img, face_location1)
  total_faces = len(face_location1)
  print('Total Faces detected: ', total_faces)

  Name_Dist = {}
  Not_sure = []
  for encodeFace, faceLoc in zip(encodesCurrentFrame, face_location1):
          matches = face_recognition.compare_faces(dec_std_faces, encodeFace)
          
          faceDis = face_recognition.face_distance(dec_std_faces, encodeFace)
          matchIndex = np.argmin(faceDis)
          match_threshold = np.min(faceDis)
          if faceDis[matchIndex] < 0.50:
              name = dec_names_lst[matchIndex].upper()
              Name_Dist[name] = [match_threshold,faceLoc]
          else:
              name = dec_names_lst[matchIndex].upper()
              
              if name not in Not_sure:
                if name not in Name_Dist:

                  enc = (name, match_threshold,faceLoc)
                  Not_sure.append(enc)

  NOT_SURE_DIST = {}

  for Face in Not_sure:
    
    Name = Face[0]
    if Name not in Name_Dist:
      prop = []
      prop.append(Face[1])
      for temp_Face in Not_sure:
        if Name == temp_Face[0]:
          prop.append(Face[1])
      min = np.min(prop)

      for temp in Not_sure:
        if temp[0] == Name and temp[1] == min:
          NOT_SURE_DIST[Name] = [temp[1] ,temp[2]]

  return {'total_detected_stds':total_faces,
        'present_stds':list(Name_Dist),
        'absent_stds':list(NOT_SURE_DIST)}