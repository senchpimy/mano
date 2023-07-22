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
    #if mapear>referencia:return 180
    v = referencia/350
    p = v*mapear
    if int(p)>180:return 180
    return int(p) 

while webcam.isOpened():
    succes, img = webcam.read()
    if not succes:break
    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mitad = distancia(hand.landmark[mp_hand.HandLandmark.WRIST],hand.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_MCP])
            medio = distancia(hand.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_TIP],hand.landmark[mp_hand.HandLandmark.MIDDLE_FINGER_MCP])
            pulgar = distancia(hand.landmark[mp_hand.HandLandmark.THUMB_TIP],hand.landmark[mp_hand.HandLandmark.THUMB_MCP])
            indice = distancia(hand.landmark[mp_hand.HandLandmark.INDEX_FINGER_MCP],hand.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP])
            ring = distancia(hand.landmark[mp_hand.HandLandmark.RING_FINGER_MCP],hand.landmark[mp_hand.HandLandmark.RING_FINGER_TIP])
            pinky = distancia(hand.landmark[mp_hand.HandLandmark.PINKY_MCP],hand.landmark[mp_hand.HandLandmark.PINKY_TIP])
            print(regla_de_tres(mitad,medio))
            print(regla_de_tres(mitad,indice*1.12)) # Relacion 0.9:1 con el medio
            print(regla_de_tres(mitad,ring*1.26)) # Relacion 0.8:1 con el medio
            print(regla_de_tres(mitad,pinky*1.58)) # Relacion 0.6:1 con el medio
            #print(regla_de_tres(mitad,pulgar*1.25)) # Relacion 0.8:1 con el medio
            print(mitad)
            print(medio)
            mp_drawing_utils.draw_landmarks(img,hand, mp_hand.HAND_CONNECTIONS)

    cv2.imshow("image",img)
    cv2.waitKey(1)
webcam.release()
cv2.destroyAllWindows()
