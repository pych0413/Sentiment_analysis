import cv2
import os
import os.path
from os import path
import shutil
import streamlit as st
import numpy as np
import pandas as pd
import subprocess




st.title('Face Recognition System')
'Sentiment Analysis Model'
'By Paul Yuen'

uploaded_file = st.file_uploader(" Import the photo:", type="jpg")

if uploaded_file is not None:
    # Clear the yolov5 result file
    directory = r"./yolov5/runs/detect/exp"
    shutil.rmtree(directory, ignore_errors=True)
    if path.exists("test.jpg"):
        os.remove('test.jpg')

    if path.exists("face.jpg"):
        os.remove('face.jpg')

    if path.exists("resultimg.jpg"):
        os.remove('resultimg.jpg')

    # Import the photo
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    'Your photo:'
    st.image(opencv_image, channels="BGR")
    cv2.imwrite('test.jpg', opencv_image)

    # Read the input image
    cropimg = cv2.imread("test.jpg")
    
    # Convert into grayscale
    grayimg = cv2.cvtColor(cropimg, cv2.COLOR_BGR2GRAY)
  
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
  
    # Detect faces
    facesimg = face_cascade.detectMultiScale(grayimg, 1.2, 4)
  
    # Draw rectangle around the faces and crop the faces
    for (x, y, w, h) in facesimg:
        cv2.rectangle(cropimg, (x, y), (x+w, y+h), (0, 0, 255), 2)
        facesimg = cropimg[y:y + h, x:x + w]
        cv2.imshow("face",facesimg)
        cv2.imwrite('face.jpg', facesimg)
      
    if path.exists("face.jpg"):

        # Display the output of croped Face
        st.success("Face detected:")
        detectedimg = cv2.imread('face.jpg')
        st.image(detectedimg, channels="BGR")


        Facedetect_pred = st.button("Sentiment Analysis")
        if Facedetect_pred:

            #run the yolov5 model
            subprocess.call([r'connect_Yolov5.bat'])
            st.success("Sentiment analysis result:")
            resultimg = cv2.imread('./yolov5/runs/detect/exp/face.jpg')
            st.image(resultimg, channels="BGR")
            cv2.imwrite('resultimg.jpg',resultimg)
            st.balloons()

            with open("resultimg.jpg", "rb") as file:
                btn = st.download_button(
                    label="Download image",
                    data=file,
                    file_name="resultimg.jpg",
                    )


    else:

        st.error("_____________ (｡•ᴗ•｡) _____________")
        st.error("No face, plase try anther photos")
        st.error("_____________ (｡•ᴗ•｡) _____________")
        st.snow()
  

