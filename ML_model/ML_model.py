# # -*- coding: utf-8 -*-
# """ML_PROJECT_UPDATED.ipynb

# Automatically generated by Colaboratory.

# Original file is located at
#     https://colab.research.google.com/drive/1y-92uQ1Rw36iOu6O-tRLMrmt7q1AVJNw
# """

# file_name = "./Data/StudentName.pkl"

# import pickle

# open_file = open(file_name, "rb")
# personNames = pickle.load(open_file)
# open_file.close()


# file_name = "./Data/StudentEncoding.pkl"

# open_file = open(file_name, "rb")
# encodeListKnown = pickle.load(open_file)
# open_file.close()


# import cv2
# import os

# folder = './Data/ClassroomPicture/'
    
# for filename in os.listdir(folder):
#     print(filename)
#     img = cv2.imread(os.path.join(folder,filename))
#     if img is not None:


#       Path = os.path.join(folder,filename)

#       image = face_recognition.load_image_file(Path)


#       detector = MTCNN()

#       faces = detector.detect_faces(image)

#       face_location1 = []
#       for face in faces:
#         x,y,w,h = face['box']

#         x1 = y
#         w1 = y+h
#         h1 = x
#         y1 = x+w

#         a = (x1, y1, w1, h1)
#         face_location1.append(a)


#       encodesCurrentFrame = face_recognition.face_encodings(image, face_location1)

      
#       ImageContours = cv2.imread(Path)
#       ImageContours = cv2.cvtColor(ImageContours,cv2.COLOR_BGR2RGB)

#       ReplicateImage = ImageContours.copy()

#       for cntr in face_location1:
#           x,y,w,h = cntr
#           cv2.rectangle(ReplicateImage, (h, x), (y, w), (0, 0, 255), 2)

#       cv2.imwrite('./Data/Output_Image/'+ filename ,ReplicateImage)

#       Name_Dist = {}
#       Not_sure = []
#       # Not_sure1 = []
#       for encodeFace, faceLoc in zip(encodesCurrentFrame, face_location1):
#               matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
              
#               faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#               # print(faceDis)
#               matchIndex = np.argmin(faceDis)
#               match_threshold = np.min(faceDis)
#               # print(matchIndex)
#               if faceDis[matchIndex] < 0.50:
#                   name = personNames[matchIndex].upper()
#                   # print(name)
#                   Name_Dist[name] = [match_threshold,faceLoc]
#               else:
#                   name = personNames[matchIndex].upper()
                  
#                   if name not in Not_sure:
#                     if name not in Name_Dist:

#                       enc = (name, match_threshold,faceLoc)
#                       Not_sure.append(enc)
                  


#                   # print('Unknown')
#                   # Name_Dist['Unknown'] = faceLoc
#       NOT_SURE_DIST = {}

#       for Face in Not_sure:
        
#         Name = Face[0]
#         if Name not in Name_Dist:
#           prop = []
#           prop.append(Face[1])
#           for temp_Face in Not_sure:
#             if Name == temp_Face[0]:
#               prop.append(Face[1])
#           min = np.min(prop)

#           for temp in Not_sure:
#             if temp[0] == Name and temp[1] == min:
#               NOT_SURE_DIST[Name] = [temp[1] ,temp[2]]
#               # print(Name)




#       image = Image.open('./Data/Output_Image/'+ filename)

#       draw = ImageDraw.Draw(image)

#       font = ImageFont.truetype('./Data/Roboto[wdth,wght].ttf', size=45)

#       for key in Name_Dist:
#         A = Name_Dist[key][1]
#         (x, y) = (A[1], A[0])
#         message = str(key)
#         color = 'rgb(0, 0, 0)'
#         # print(x,y)
#         draw.text((x, y), message, fill=color, font=font)

#       for key in NOT_SURE_DIST:
#         A = NOT_SURE_DIST[key][1]
#         (x, y) = (A[1], A[0])
#         message = str(key)
#         color = 'rgb(255, 0, 0)'
#         # print(x,y)
#         draw.text((x, y), message, fill=color, font=font)
      
#       image.save('./Data/Output_Image/'+ filename)

# """**Installing Face_Recognition Library**"""

# !pip install face_recognition
# !pip install -v --install-option="--no" --install-option="DLIB_USE_CUDA" dlib
# !pip install mtcnn

"""**Importing Libraries**"""

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

# from google.colab import drive
# drive.mount('/content/drive')

"""**Face Encoding Function**"""

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

"""**Dont Run This, If you dont add new student picture in Class data**

From Drive, Loading All images and Store the name of Student in a List, So that we can predict
"""

path = './Data/Student_Faces'
images = []
personNames = []
myList = os.listdir(path)
# print(myList)
for cu_img in myList:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_Img)
    personNames.append(os.path.splitext(cu_img)[0])
print(personNames)



file_name = "./Data/StudentName.pkl"

open_file = open(file_name, "wb")
pickle.dump(personNames, open_file)
open_file.close()

"""**Save  face Encoding**"""

encodeListKnown = faceEncodings(images)

import pickle

file_name = "./Data/StudentEncoding.pkl"

open_file = open(file_name, "wb")
pickle.dump(encodeListKnown, open_file)
open_file.close()

"""**Load Student and Face encoding Stored in Drive**"""

file_name = "./Data/StudentName.pkl"


open_file = open(file_name, "rb")
personNames = pickle.load(open_file)
open_file.close()


file_name = "./Data/StudentEncoding.pkl"

open_file = open(file_name, "rb")
encodeListKnown = pickle.load(open_file)
open_file.close()

"""**INFERENCE**
1. loading Image
2. Finding Faces in Group image
3. Find New Faces Encodings
"""

Path = './Data/ClassroomPicture/IMG_20220315_095343_1.jpg'


image = face_recognition.load_image_file(Path)


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

"""**Checking How many Faces detected**"""

print(len(face_location1))

"""**Draw Bounding Box across New Faces Detected**"""

import cv2
ImageContours = cv2.imread(Path)
ImageContours = cv2.cvtColor(ImageContours,cv2.COLOR_BGR2RGB)

ReplicateImage = ImageContours.copy()

for cntr in face_location1:
    x,y,w,h = cntr
    cv2.rectangle(ReplicateImage, (h, x), (y, w), (0, 0, 255), 2)

cv2.imwrite('./Data/Output_Image/Marked_Face_Image.jpg',ReplicateImage)

"""**Printing Size of Faces**"""

for cntr in face_location1:
    x,y,w,h = cntr
    print('Face Size =  ', w-x, ' , ', y-h)

import os
os.path.basename(Path)

"""**Comparing Both Encodings, Stored in Distionary**

"""

Name_Dist = {}
for encodeFace, faceLoc in zip(encodesCurrentFrame, face_location1):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        # print(matches)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        # print(matchIndex)
        if faceDis[matchIndex] < 0.50:
            name = personNames[matchIndex].upper()
            print(name)
            Name_Dist[name] = faceLoc
        else:
            print('Unknown')
            Name_Dist['Unknown'] = faceLoc

"""**Writing Name on the Faces**"""

image = Image.open('./Data/Output_Image/Marked_Face_Image.jpg')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('./Data/Roboto[wdth,wght].ttf', size=45)

for key in Name_Dist:
  A = Name_Dist[key][1]
  (x, y) = (A[1], A[0])
  message = str(key)
  color = 'rgb(0, 0, 0)'
  # print(x,y)
  draw.text((x, y), message, fill=color, font=font)

for key in NOT_SURE_DIST:
  A = NOT_SURE_DIST[key][1]
  (x, y) = (A[1], A[0])
  message = str(key)
  color = 'rgb(255, 0, 0)'
  # print(x,y)
  draw.text((x, y), message, fill=color, font=font)
 
image.save('./Data/Output_Image/Label_Face_Image_NOT_SURE.jpg')

for i in Not_sure:
  if i not in Name_Dist:
    Name_Dist[i] = Not_sure[i]

Name_Dist = {}
Not_sure = []
Not_sure1 = []
for encodeFace, faceLoc in zip(encodesCurrentFrame, face_location1):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        match_threshold = np.min(faceDis)
        # print(matchIndex)
        if faceDis[matchIndex] < 0.50:
            name = personNames[matchIndex].upper()
            print(name)
            Name_Dist[name] = [match_threshold,faceLoc]
        else:
            name = personNames[matchIndex].upper()
            print(name)
            # Not_sure[name] = [match_threshold,faceLoc]
            if name not in Not_sure:
              if name not in Name_Dist:
                enc = (name, match_threshold,faceLoc)
                Not_sure.append(enc)
            print('Unknown')
            # Name_Dist['Unknown'] = faceLoc

"""**Extra Code**"""

Name_Dist

Not_sure

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
        # print(Name)

image=cv2.imread(Path)
x, y, w, h = face_location1[5]
plt.imshow(image[  x:w,h:y])

# Path = './Data/ClassroomPicture/pp.jpg'

# image = face_recognition.load_image_file(Path)

# face_locations = face_recognition.face_locations(image)

# encodesCurrentFrame = face_recognition.face_encodings(image, face_locations)

# len(face_locations)

# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# from matplotlib import pyplot
# from matplotlib.patches import Rectangle
# from matplotlib.patches import Circle
# from mtcnn.mtcnn import MTCNN


# def draw_image_with_boxes(filename, result_list):

#     data = pyplot.imread(filename)
#     pyplot.imshow(data)

#     ax = pyplot.gca()
#     print('h1')
#     for result in result_list:

#        # a = 1

        

#         (x, y, width, height) = result['box']
#         print('Dimension:' ,width, height)
#         rect = Rectangle((x, y), width, height, fill=False, color='red')

#         ax.add_patch(rect)

#         for (key, value) in result['keypoints'].items():

#             dot = Circle(value, radius=2, color='red')
#             ax.add_patch(dot)

#     pyplot.show()


# # filename = 'pp.jpg'
# # filename = 'IMG_20220315_095307.jpg'

# # filename = '/content/IMG_20220315_095343_1.jpg'
# filename = './Data/ClassroomPicture/IMG_20220315_095343_1.jpg'

# pixels = pyplot.imread(filename)

# detector = MTCNN()

# faces = detector.detect_faces(pixels)
# print ('Face Detected: ', len(faces))

# draw_image_with_boxes(filename, faces)

# print(faces[0]['box'])

# x,y,w,h = faces[0]['box']

# plt.imshow(image[y:y+h, x:x+w])

# x,y,w,h = faces[0]['box']

# x1 = y
# w1 = y+h
# h1 = x
# y1 = x+w


# plt.imshow(image[  x1:w1,h1:y1])

# x, y, w, h = face_locations[0]
# plt.imshow(image[  x:w,h:y])

# print(face_locations)

# face_location1 = []
# for face in faces:
#   x,y,w,h = face['box']

#   x1 = y
#   w1 = y+h
#   h1 = x
#   y1 = x+w

#   a = (x1, y1, w1, h1)
#   face_location1.append(a)

# print(face_location1)

# file_name = "./Data/StudentName.pkl"


# open_file = open(file_name, "rb")
# personNames = pickle.load(open_file)
# open_file.close()


# file_name = "./Data/StudentEncoding.pkl"

# open_file = open(file_name, "rb")
# encodeListKnown = pickle.load(open_file)
# open_file.close()

# encodesCurrentFrame = face_recognition.face_encodings(image, face_location1)

# Name_Dist = {}
# for encodeFace, faceLoc in zip(encodesCurrentFrame, face_location1):
#         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
#         # print(matches)
#         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
#         # print(faceDis)
#         matchIndex = np.argmin(faceDis)
#         # print(matchIndex)
#         if faceDis[matchIndex] < 0.50:
#             name = personNames[matchIndex].upper()
#             print(name)
#             Name_Dist[name] = faceLoc
#         else:
#             print('Unknown')
#             Name_Dist['Unknown'] = faceLoc

