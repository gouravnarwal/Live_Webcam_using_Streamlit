import cv2
import streamlit as st
from datetime import datetime


st.title("Motion Detector")

if "running" not in st.session_state:
    st.session_state.running = False

if not st.session_state.running:
    if st.button("Start Camera", key="start_camera"):
        st.session_state.running = True


if st.session_state.running:
    container = st.container()
    with container:
        streamlit_image = st.image([])
        video = cv2.VideoCapture(0)

        # Stop Camera button
        if st.button("Stop Camera", key="stop_camera"):
            st.session_state.running = False
            video.release()
            st.write("Camera stopped.")
            container.empty()

        while st.session_state.running:

            check,frame = video.read()
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            now = datetime.now()

            cv2.putText(img=frame,text=now.strftime("%A"),org=(30,80),
                        fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=2,color=(20,100,200),
                        thickness=2,lineType=cv2.LINE_AA)
            cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                        thickness=2, lineType=cv2.LINE_AA)

            streamlit_image.image(frame)

            # Break the loop if the stop button is pressed
            if not st.session_state.running:
                break

        video.release()




