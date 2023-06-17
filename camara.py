import cv2
import mediapipe as mp

webcam=cv2.VideoCapture(2)
mp_hand= mp.solutions.hands
hands = mp_hand.Hands()

mp_drawing_utils = mp.solutions.drawing_utils

while webcam.isOpened():
    succes, img = webcam.read()
    if not succes:break
    result = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mp_drawing_utils.draw_landmarks(img,hand, mp_hand.HAND_CONNECTIONS)

    cv2.imshow("dfsg",img)
    cv2.waitKey(1)
webcam.release()
cv2.destroyAllWindows()
