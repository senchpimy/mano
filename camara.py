import cv2
import os
import numpy as np
import mediapipe as mp

webcam=cv2.VideoCapture(0)
mp_hand= mp.solutions.hands
hands = mp_hand.Hands()

mp_drawing_utils = mp.solutions.drawing_utils

def distancia(
        punto1,#:mp.framework.formats.landmark_pb2.NormalizedLandmark
        punto2#:mp.framework.formats.landmark_pb2.NormalizedLandmark
        )->float:
    x=(punto1.x-punto2.x)
    y=(punto1.y-punto2.y)
    return np.sqrt(x**2+y**2)*1000

def regla_de_tres(referencia:float, mapear:float)->int:
    if mapear>referencia:return 180
    v = referencia*180
    p = v/mapear
    return int(p) 

while webcam.isOpened():
    succes, img = webcam.read()
    if not succes:break
    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mitad = distancia(hand.landmark[mp_hand.HandLandmark.WRIST],hand.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_MCP])
            d = distancia(hand.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP],hand.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_MCP])
            print(regla_de_tres(mitad,d))
            print(mitad)
            print(d)
            mp_drawing_utils.draw_landmarks(img,hand, mp_hand.HAND_CONNECTIONS)

    cv2.imshow("image",img)
    cv2.waitKey(1)
webcam.release()
cv2.destroyAllWindows()
