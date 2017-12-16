#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2

from picamera import PiCamera
from time import  sleep

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

camera = PiCamera()
camera.start_preview()

# 画像サイズの指定
ret = capture.set(3, 480)
ret = capture.set(4, 320)

i = 0
while True:
    start = time.clock() # 開始時刻
    ret, image = capture.read() # 画像を取得する作業
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30))

    if len(face) > 0:
        for rect in face:
            cv2.rectangle(image, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)

    get_image_time = int((time.clock()-start)*1000) # 処理時間計測
    # 1フレーム取得するのにかかった時間を表示
    cv2.putText( image, str(get_image_time)+"ms", (10,10), 1, 1, (0,255,0))

    cv2.imshow("Camera Test",image)
    # キーが押されたら保存・終了
    if cv2.waitKey(10) == 32: # 32:[Space]
        cv2.imwrite(str(i)+".jpg",image)
        i+=1
        print("Save Image..."+str(i)+".jpg")
    elif cv2.waitKey(10) == 27: # 27:Esc
        capture.release()
        cv2.destroyAllWindows()
        break

    sleep(10)
camera.stop_preview()
