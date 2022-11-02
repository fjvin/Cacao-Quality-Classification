import cv2 
import uuid
import os
import time

camID = 2
cam = cv2.VideoCapture(camID)

IMAGES_PATH = "images\collectedImages"

while True:
    check, frame = cam.read()

    cv2.imshow('video', frame)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        time.sleep(2)
        print('Label Image Software Closed')

    if key & 0xFF == ord('s'):
        imgName = os.path.join(IMAGES_PATH, '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgName, frame)
        time.sleep(2)
        print('Image saved as "{}"'.format(imgName))        

cam.release()
cv2.destroyAllWindows()