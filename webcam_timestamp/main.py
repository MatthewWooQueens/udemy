import streamlit as st
import cv2
from time import localtime, strftime

st.title("Motion Detector")
but = st.button("Start Camera")

if but:
    st_image = st.image([])
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tm = localtime()
        day = strftime('%A',tm)
        txt = strftime('%H:%M:%S',tm)
        cv2.putText(img=frame, text=day, org=(50,50), 
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, 
                    color=(20,100,200), thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=txt, org=(50,100), 
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, 
                    color=(20,100,200), thickness=2, lineType=cv2.LINE_AA)
        st_image.image(frame)

