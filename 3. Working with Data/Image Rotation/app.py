import cv2 as cv
import numpy as np
from PIL import Image
import streamlit as st


def rotate_image(image,angle):
    img = np.array(image)
    height , width = img.shape[:2]
    M = cv.getRotationMatrix2D((width/2, height/2),angle, 1)
    rotated_img = cv.warpAffine(img, M, (width, height))
    return rotated_img

st.title('Image Rotator')
st.subheader('Upload an image file : ')
img_file = st.file_uploader("Upload your image", type = ['png','jpg','jpeg'])

st.subheader('Rotate the Image : ')
angle = st.slider('Chose the Angle : ', -180, 180, 0 , 1)

if img_file is not None:
    image = Image.open(img_file)
    rotated_img = rotate_image(image, angle)
    st.image(rotated_img)
