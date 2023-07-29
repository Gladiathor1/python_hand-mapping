import cv2
import imutils as imutils
import mediapipe as mp
import os
from os import path

from google.protobuf.json_format import MessageToDict

mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils
# cap = cv2.VideoCapture(0)
# cap = cv2.imread("my.jpg")
try:
    my_file_name="p19_both21"
    path1=my_file_name+"_results/"
    if not path.exists(path1):
        os.mkdir(path1)

    for filename in os.listdir("./JB/"+my_file_name):
        myhandsleft = []
        myhandsright = []
        myhands = []
        center_points=[]
        widths=[]

        src = cv2.imread("./JB/"+my_file_name+"/"+filename)
        frame = src
        # frame = imutils.resize(frame, width=200, height=200)
        # _, frame = cap.read()
        #
        h, w, c = frame.shape


        src = cv2.imread("./JB/"+my_file_name+"/"+filename)
        frame = src
        # frame = cv2.VideoCapture(0)
        # frame = imutils.resize(frame, width=1366, height=768)
        framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(framergb)
        hand_landmarks = result.multi_hand_landmarks
        # for rect in result.multi_handedness:
        #     print (rect)
        # print (type(result.multi_handedness))
        # print(result.multi_handedness[0].classification[0].label)
        # print("result", result.multi_handedness)
        try:
            for rest in result.multi_handedness:
                # if (rest.classification[0].label=="Left"):
                #     print("left jb")
                # elif(rest.classification[0].label=="Right"):
                #     print("right jb")
                # d = MessageToDict(rest.classification)
                # print(type(rest.classification))
                myhands.append(rest.classification[0].label)
                # print(myhands)
                # print(hand_landmarks)
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
                        cv2.rectangle(frame, (int(x_min - 40), int(y_min - 30)), (int(x_max + 40), int(y_max + 40)),
                                      (0, 255, 0), 2)
                        dw = 1. / w
                        dh = 1. / h
                        xx = ((x_min - 40) + (x_max + 40)) / 2.0
                        yy = ((y_min - 30) + (y_max + 40)) / 2.0
                        ww = (x_max + 40) - (x_min - 40)
                        hh = (y_max + 40) - (y_min - 30)
                        my_other_x = xx * dw
                        my_width = ww * dw
                        my_other_y = yy * dh
                        my_height = hh * dh

                        center_points.append(my_other_x)
                        center_points.append(my_other_y)
                        # print(center_points)
                        widths.append(my_width)
                        widths.append(my_height)
                        # print(widths)
                        # cv2.circle(frame, (int(myx), int(myy)), radius=5, color=(255, 0, 0), thickness=2)
                        # cv2.circle(frame, (int(x_min), int(y_min)), radius=5, color=(255, 0, 0), thickness=2)
                        # cv2.circle(frame, (int(x_max), int(y_max)), radius=5, color=(255, 0, 0), thickness=2)
                        # print((x_min-50.0, y_min-50.0), (x_max+20.0, y_max+20.0))
                        # mp_drawing.draw_landmarks(frame, handLMs, mphands.HAND_CONNECTIONS)
                cv2.imshow("frame", frame)

                cv2.waitKey(1)
        except Exception as e:
            print(e)
        try:
            outputL=[]
            outputR=[]
            leftstr=""
            rightstr=""
            myset = set(myhands)
            data = filename.split(".")
            file1 = open(path1+data[0]+".txt", "w")
            for handss in myset:
                # print(handss)
                if handss=="Left":
                    leftstr+=(str(0))
                    leftstr+=(" ")
                    leftstr+=(str(center_points[0]))
                    leftstr+=(" ")
                    leftstr+=(str(center_points[1]))
                    leftstr+=(" ")
                    leftstr+=(str(widths[0]))
                    leftstr+=(" ")
                    leftstr+=(str(widths[1]))
                    leftstr+=("\n")

                    # outputL.append(1)
                    # outputL.append(round(center_points[0], 6))
                    # outputL.append(round(center_points[1], 6))
                    # outputL.append(round(widths[0], 6))
                    # outputL.append(round(widths[1], 6))
                if handss=="Right":
                    rightstr+=(str(1))
                    rightstr +=(" ")
                    rightstr +=(str(center_points[2]))
                    rightstr+=(" ")
                    rightstr +=(str(center_points[3]))
                    rightstr+=(" ")
                    rightstr +=(str(widths[2]))
                    rightstr +=(" ")
                    rightstr+=(str(widths[3]))


                    # outputR.append(0)
                    # outputR.append(round(center_points[2],6))
                    # outputR.append(round(center_points[3],6))
                    # outputR.append(round(widths[2],6))
                    # outputR.append(round(widths[3],6))
            # print(filename)
            # print(leftstr)
            # print(rightstr)
            if leftstr:
                file1.write(leftstr)
            if rightstr:
                file1.write(rightstr)
            # if outputL:
            #     print(outputL)
            #     for element in outputL:
            #         file1.write(str(element))
            #         file1.write(" ")
            #     file1.write("\n")
            # if outputR:
            #     print(outputR)
            #     for element in outputR:
            #         file1.write(str(element))
            #         file1.write(" ")
            file1.close()
        except Exception as e:
            print("second")
            print(e)
except:
    print("lol")
