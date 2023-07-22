import cv2
import os
import numpy as np
import mediapipe as mp

webcam=cv2.VideoCapture(0)
mp_hand= mp.solutions.hands
hands = mp_hand.Hands()

mp_drawing_utils = mp.solutions.drawing_utils
print("bslsklhhsdkl")
while webcam.isOpened():
    print("bslsklhhsdkl")
    succes, img = webcam.read()
    if not succes:break
    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
#            print(f'Index finger tip coordinates: (',
#          f'{hand.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP].x }, '
#          f'{hand.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP].y})')
#            print(f'Thumb finger tip coordinates: (',
#          f'{hand.landmark[mp_hand.HandLandmark.THUMB_TIP].x }, '
#          f'{hand.landmark[mp_hand.HandLandmark.THUMB_TIP].y})')
            x=(hand.landmark[mp_hand.HandLandmark.THUMB_TIP].x-hand.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP].x)
            y=(hand.landmark[mp_hand.HandLandmark.THUMB_TIP].y-hand.landmark[mp_hand.HandLandmark.INDEX_FINGER_TIP].y)
            d = np.sqrt(x**2+y**2)
            print(f"distancia {d}")
            os.system(f'xrandr --output eDP-1 --brightness {d}')
            mp_drawing_utils.draw_landmarks(img,hand, mp_hand.HAND_CONNECTIONS)

    cv2.imshow("dfsg",img)
    cv2.waitKey(1)
webcam.release()
cv2.destroyAllWindows()
