import time
import cv2
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import mapper as map
import _thread
import math
import mediapipe as mp


class handDetector:
    def __init__(self, mode=False, maxHands=2, detectionConf=0.5, trackConf=0.5):
        self.mode = mode  # si mode = True alors statique (pas voulue)
        self.maxHands = maxHands
        self.detectionConf = detectionConf  # seuil de confiace de la detection
        self.trackConf = trackConf  # seuil de confiance du tracking

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.detectionConf, self.trackConf
        )
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(
            img, cv2.COLOR_BGR2RGB
        )  # conversion car le model prend image rgb mais cv2 donne image bgr
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if (
            self.results.multi_hand_landmarks and draw
        ):  # Si main detecteée et draw = True alors desiner traits entre points
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    img, handLms, self.mpHands.HAND_CONNECTIONS
                )
        return img

    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append(
                    [id, cx, cy]
                )  # remplit la liste avec l'id des marqueurs et leur pos
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax

            if draw:  # Desiner bounding boxe si draw = True
                cv2.rectangle(
                    img,
                    (bbox[0] - 20, bbox[1] - 20),
                    (bbox[2] + 20, bbox[3] + 20),
                    (0, 255, 0),
                    2,
                )

        return self.lmList, bbox

    def fingersUp(self):
        fingers = []
        # --- Pour le pouce : si le bout du pouce est au dessus de la falange alors le pouce est debout (1) ---
        if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # -----------------------------------------------------------------------------------------------------
        # --- Pour les 4 autres doigts : si le bout du doigt est au dessus de la deuxieme falange le doigt est debout (1) ---
        for id in range(1, 5):
            if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        # -------------------------------------------------------------------------------------------------------------------
        return fingers

    def findDistance(self, p1, p2, img, draw=True):

        x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
        x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        if draw:
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        length = math.sqrt((x2 - x1) ** 2, (y2 - y1) ** 2)  # calcule de l'hypotenus

        return length, img, [x1, y1, x2, y2, cx, cy]


faceCascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)


kinect = PyKinectRuntime.PyKinectRuntime(
    PyKinectV2.FrameSourceTypes_Body
    | PyKinectV2.FrameSourceTypes_BodyIndex
    | PyKinectV2.FrameSourceTypes_Color
    | PyKinectV2.FrameSourceTypes_Depth
    | PyKinectV2.FrameSourceTypes_Infrared
)

detector = handDetector(detectionConf=0.7, maxHands=1)

zoom = 0
zoomBar = 400
zoomPer = 0
area = 0
colorzoom = (255, 0, 0)
zooming = False

mintresh = 500  # distance min à laquelle doit être un objet pour qu'il soit détecté (en mm)
maxtresh = 2500  # distance max à laquelle doit être un objet pour qu'il soit détecté (en mm)
step = 41
stepD = 10

show_close_objects = False
show_face = False

pTime = 0

x_gauche = 72
x_droite = 109

# -- image vide pour eviter erreur dans programme de detection de visage à l'initialisation --
gray = np.zeros((1080 // 2, 1920 // 2), dtype="uint8")
# --------------------------------------------------------------------------------------------


def face_detection():
    global faces
    global gray
    while True:
        # -- Detection des traits specifié dans le Haar Cascade --
        faces = faceCascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35)
        )


face_thread = _thread.start_new_thread(face_detection, ())

# ---------- Fonction executée lors d'un clic ----------
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord = map.color_2_world(kinect, kinect._depth_frame_data, _CameraSpacePoint)
        coord_x = coord[(int(y) * 1920 // 2) + (1920 // 2 - int(x))].x
        coord_y = coord[(int(y) * 1920 // 2) + (1920 // 2 - int(x))].y
        z = coord[(int(y) * 1920 // 2) + (1920 // 2 - int(x))].z
        print(f"x = {coord_x} y = {coord_y}, z = {z}")

        A = floor_plan.x
        B = floor_plan.y
        C = floor_plan.z
        D = floor_plan.w
        dist_from_floor = abs(A * coord_x + B * coord_y + C * z + D) / math.sqrt(
            A ** 2 + B ** 2 + C ** 2
        )

        print(f"z = {z}, dist_from_floor = {dist_from_floor}, pixel_depth = {z}")


# ------------------------------------------------------


lunched = True
while lunched:
    if (
        kinect.has_new_body_frame()
        and kinect.has_new_body_index_frame()
        and kinect.has_new_color_frame()
        and kinect.has_new_depth_frame()
    ):
        # ----- Image couleur -----
        frame = kinect.get_last_color_frame()
        frame = np.reshape(frame, (1080, 1920, 4))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        frame = frame.astype(np.uint8)  # 0 to 255
        frame = cv2.flip(frame, 1)

        untouched = np.copy(frame)

        useful_info_frame = np.copy(frame)
        # -------------------------

        # ---- Image profondeur ----
        frameD = kinect.get_last_depth_frame()
        frameDepth = kinect._depth_frame_data
        frameD = np.reshape(frameD, (424, 512))
        frameD = frameD.astype(np.uint16)  # 0 to 65535
        frameD = cv2.flip(frameD, 1)
        frameD_test = cv2.resize(frameD, (773, 663))
        frameD_test = frameD_test[44 : frameD_test.shape[0] - 49, :]
        # --------------------------

        # -- utilisé pour la fonction de detection de visage --
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # -----------------------------------------------------

        face_frame_list = []
        for (x, y, w, h) in faces:
            y1 = y - 10
            y2 = y + h + 10
            x1 = x - 10
            x2 = x + w + 10
            if y1 > 0 and x1 > 0:
                face_cropped = frame[y1:y2, x1:x2]
                face_cropped = cv2.resize(face_cropped, (450, 450))
                face_frame_list.append((face_cropped))

            # -- Dessine un rectangle autour des visages reconnue --
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            # ------------------------------------------------------

        for face in face_frame_list:
            cv2.imshow("face", face)

        if face_frame_list == []:
            cv2.destroyWindow("face")

        # --- Trouver plan correspondant au sol ---
        bodyframe = kinect.get_last_body_frame()
        floor_plan = bodyframe.floor_clip_plane
        # -----------------------------------------

        frame = detector.findHands(frame)
        lmList, bbox = detector.findPosition(frame, draw=False)
        if len(lmList) != 0:

            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
            if 200 < area < 2000:

                # --- Trouver distance entre indexe et pouce ---
                length_t_i, frame, lineInfo_t_i = detector.findDistance(4, 8, frame)
                # ----------------------------------------------

                # --- Trouver distance entre poignet et pouce ---
                length_t_w, frame, lineInfo_t_w = detector.findDistance(
                    4, 0, frame, draw=False
                )
                # -----------------------------------------------

                # -- convertir le ratio (entre 0.1 et 1.2) en nombre entre 0 et 100 --
                zoomPer = np.interp(length_t_i / length_t_w, [0.1, 1.2], [0, 100])
                # --------------------------------------------------------------------

                # --- Palier de 10 en 10 pour rentre plus fluide ---
                smoothness = 10
                zoom = int(smoothness * round(zoomPer / smoothness) * 1.5)
                # --------------------------------------------------

                fingers = detector.fingersUp()

                # ----------------- Si auriculaire baissé -----------------
                if not fingers[4] and zoom > 0:
                    y1 = lineInfo_t_i[5] - int(200 - zoom)
                    y2 = lineInfo_t_i[5] + int(200 - zoom)
                    x1 = lineInfo_t_i[4] - int(200 - zoom)
                    x2 = lineInfo_t_i[4] + int(200 - zoom)
                    if y1 < 0:
                        y1 = 0
                    if x1 < 0:
                        x1 = 0
                    frame_rect = cv2.rectangle(
                        frame, (x1, y1), (x2, y2), (255, 0, 0), 2
                    )
                    zoomed_frame = untouched[y1:y2, x1:x2]
                    cv2.circle(
                        frame,
                        (lineInfo_t_i[4], lineInfo_t_i[5]),
                        15,
                        (0, 255, 0),
                        cv2.FILLED,
                    )
                    colorzoom = (0, 255, 0)
                    zoomed_frame = cv2.resize(zoomed_frame, (500, 500))
                    cv2.putText(
                        zoomed_frame,
                        f"{int(zoomPer)} %",
                        (10, 20),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.65,
                        (255, 0, 255),
                        2,
                    )
                    cv2.imshow("zoom", zoomed_frame)
                    zooming = True
                else:
                    colorzoom = (255, 0, 0)
                    cv2.destroyWindow("zoom")
                    zooming = False
                # --------------------------------------------------------

        if show_close_objects == True:

            # -- Cartographie les points de l'image couleur dans le monde réel --
            real_world_coords_color = map.color_2_world(
                kinect, kinect._depth_frame_data, _CameraSpacePoint
            )
            # -------------------------------------------------------------------

            for y in range(0, frame.shape[0], step):
                for x in range(0, frame.shape[1], step):

                    # -- Coordonée dans le monde réel (en m) du pixel de l'image couleur --
                    coord_x = real_world_coords_color[
                        (int(y) * 1920) + (1920 - int(x))
                    ].x
                    coord_y = real_world_coords_color[
                        (int(y) * 1920) + (1920 - int(x))
                    ].y
                    z = real_world_coords_color[(int(y) * 1920) + (1920 - int(x))].z
                    # ---------------------------------------------------------------------

                    # -- Constantes définissants le plan du sol --
                    A = floor_plan.x
                    B = floor_plan.y
                    C = floor_plan.z
                    D = floor_plan.w
                    # -----------------------------------------

                    # -- Distance du point par rapport au sol --
                    dist_from_floor = abs(
                        A * coord_x + B * coord_y + C * z + D
                    ) / math.sqrt(A ** 2 + B ** 2 + C ** 2)
                    # ------------------------------------------

                    # -- Si point compris dans le seuil et au dessus de 8cm du sol alors dessiner un rectangle centré sur ce pixel --
                    if mintresh <= z * 1000 < maxtresh and dist_from_floor > 0.08:
                        offset = step // 2
                        start_point = (x - offset, y - offset)
                        end_point = (x + offset, y + offset)
                        frame = cv2.rectangle(
                            frame, start_point, end_point, (0, 255, 0), -1
                        )
                        useful_info_frame = cv2.rectangle(
                            useful_info_frame, start_point, end_point, (0, 255, 0), -1
                        )
                    # ---------------------------------------------------------------------------------------------------------------

        real_world_coords = map.depth_2_world(
            kinect, kinect._depth_frame_data, _CameraSpacePoint
        )

        for y in range(0, frameD.shape[0], stepD):
            for x in range(0, frameD.shape[1], stepD):
                coord_x = real_world_coords[(int(y) * 512) + (512 - int(x))].x
                coord_y = real_world_coords[(int(y) * 512) + (512 - int(x))].y
                z = real_world_coords[(int(y) * 512) + (512 - int(x))].z

                A = floor_plan.x
                B = floor_plan.y
                C = floor_plan.z
                D = floor_plan.w
                dist_from_floor = abs(
                    A * coord_x + B * coord_y + C * z + D
                ) / math.sqrt(A ** 2 + B ** 2 + C ** 2)

                if dist_from_floor < 0.05:
                    gray_tone = 255
                else:
                    gray_tone = frameD[y, x] * 5.1
                color = (gray_tone, gray_tone, gray_tone)
                start_point = (x - int(stepD / 2), y - int(stepD / 2))
                end_point = (x + int(stepD / 2), y + int(stepD / 2))
                frameD = cv2.rectangle(frameD, start_point, end_point, color, -1)

        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        useful_info_frame = cv2.resize(useful_info_frame, (0, 0), fx=0.5, fy=0.5)

        # --- Garde seulement la partie ou la dection de profondeur est possible ---
        frame_crop = useful_info_frame[:, x_gauche : frame.shape[1] - x_droite]
        # --------------------------------------------------------------------------

        # ---- Place les images zoomée au Milieu de l'écran ----
        if face_frame_list != [] and show_face:
            H, W, C = frame_crop.shape
            h, w, c = face.shape
            frame_crop[
                H // 2 - h // 2 : H // 2 + h // 2, W // 2 - w // 2 : W // 2 + w // 2
            ] = face
        elif zooming:
            H, W, C = frame_crop.shape
            h, w, c = zoomed_frame.shape
            frame_crop[
                H // 2 - h // 2 : H // 2 + h // 2, W // 2 - w // 2 : W // 2 + w // 2
            ] = zoomed_frame
        # ------------------------------------------------------

        # --- Formate l'image pour être vu dans le casque VR ---
        frame_crop1 = frame_crop[:, : frame_crop.shape[1] - 10]
        frame_crop2 = frame_crop[:, 10:]
        images_1_2_v = np.hstack((frame_crop1, frame_crop2))
        # ------------------------------------------------------

        # --- Frame rate ---
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(
            frame_crop,
            f"FPS: {int(fps)}",
            (40, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.75,
            (255, 0, 255),
            2,
        )
        # ------------------

        cv2.imshow("depth", frameD)
        cv2.imshow("frame", frame)
        cv2.imshow("frame crop", frame_crop)
        cv2.imshow("final", images_1_2_v)

        cv2.setMouseCallback("frame crop", click_event)

    key = cv2.waitKey(1)

    if key == ord("7"):
        step += 1
    if key == ord("1"):
        if step > 1:
            step -= 1

    if key == ord("p"):
        stepD += 1
    if key == ord("m"):
        if stepD > 1:
            stepD -= 1

    if key == ord("8"):
        maxtresh += 100
    if key == ord("2"):
        maxtresh -= 100

    if key == ord("9"):
        mintresh += 100
    if key == ord("3"):
        mintresh -= 100

    if key == ord("o"):
        if show_close_objects:
            show_close_objects = False
        else:
            show_close_objects = True

    if key == ord("f"):
        if show_face:
            show_face = False
        else:
            show_face = True

    if key == ord("q"):
        cv2.destroyAllWindows()
        break


print(f"step : {step}, stepD : {stepD}")
print(f"minthresh : {mintresh}, maxtresh : {maxtresh}")
