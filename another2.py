import cv2
import imutils as imutils
import mediapipe as mp
import os
from os import path

mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils

src = cv2.imread("./JB/P13_both1/P13_both1_100.jpg")
frame = src
# frame = imutils.resize(frame, width=200, height=200)
# _, frame = cap.read()
#
h, w, c = frame.shape

framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
cv2.imshow("myframe",framergb)
result = hands.process(framergb)
hand_landmarks = result.multi_hand_landmarks
# while True:
try:
    print("result" , result.multi_handedness)
    for rest in result.multi_handedness:
        # d = MessageToDict(rest.classification)
        # print(rest.classification[0].label)
        # myhands.append(rest.classification[0].label)
        # print(myhands)
        if hand_landmarks:
            for handLMs in hand_landmarks:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                for lm in handLMs.landmark:
                    x, y = (lm.x * w), (lm.y * h)
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
                cv2.rectangle(frame, (int(x_min - 40), int(y_min - 30)), (int(x_max + 40), int(y_max + 40)),(0, 255, 0), 2)
                mp_drawing.draw_landmarks(frame, handLMs, mphands.HAND_CONNECTIONS)
        cv2.imshow("frame", frame)

        cv2.waitKey(1000)
except Exception as e:
    cv2.imshow("frame", frame)
    print(e)