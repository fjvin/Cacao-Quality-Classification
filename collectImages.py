import cv2 
import uuid
import os
import time

# change camera ID here
camID = 2
cam = cv2.VideoCapture(camID)

# images location
IMAGES_PATH = "images\collectedImages"

while True:
    # access camera
    check, frame = cam.read()

    # render frame
    cv2.imshow('video', frame)

    # read input keys
    key = cv2.waitKey(1)

    # if key == 'q'; quit the program
    if key & 0xFF == ord('q'):
        time.sleep(1)
        print('Label Image Software Closed')

    # if key == 's'; save the frame with unique ID to IMAGES_PATH
    if key & 0xFF == ord('s'):
        imgName = os.path.join(IMAGES_PATH, '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgName, frame)
        time.sleep(1)
        print('Image saved as "{}"'.format(imgName))        

cam.release()
cv2.destroyAllWindows()