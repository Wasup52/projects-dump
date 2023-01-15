import time
import cv2
from numpy.core.defchararray import add, greater, zfill
from numpy.core.fromnumeric import product, shape
from numpy.core.function_base import add_newdoc
from numpy.lib.function_base import disp
from numpy.lib.twodim_base import mask_indices
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import sys

kinect = PyKinectRuntime.PyKinectRuntime(
    PyKinectV2.FrameSourceTypes_Body
    | PyKinectV2.FrameSourceTypes_BodyIndex
    | PyKinectV2.FrameSourceTypes_Color
    | PyKinectV2.FrameSourceTypes_Depth
    | PyKinectV2.FrameSourceTypes_Infrared
)

lunched = True

faceCascade = cv2.CascadeClassifier(
    "cv2\\Facial recognition\\haarcascade_frontalface_default.xml"
)

while lunched:
    if (
        kinect.has_new_body_frame()
        and kinect.has_new_body_index_frame()
        and kinect.has_new_color_frame()
        and kinect.has_new_depth_frame()
    ):
        # ---- Get color frame ----
        frame = kinect.get_last_color_frame()
        frame = np.reshape(frame, (1080, 1920, 4))
        frame = frame.astype(np.uint8)  # 0 to 255
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        # -------------------------

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect features specified in Haar Cascade
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35)
        )
        # Draw a rectangle around recognized faces
        marge = 7
        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x - marge, y - marge),
                (x + w + marge, y + h + marge),
                (50, 50, 200),
                2,
            )

        frame = cv2.flip(frame, 1)

        # Display the resulting frame
        cv2.imshow("Video", frame)

    key = cv2.waitKey(1)

    if key == ord("7"):
        marge += 10
    if key == ord("1"):
        marge -= 10

    # Exit the camera view
    if key == ord("q"):
        cv2.destroyAllWindows()
        break
