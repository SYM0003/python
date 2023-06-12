import requests
import cv2
import numpy as np
import imutils
url ="http://192.168.43.172/shot.jpg"

while true:
    img_rsp=requests.get(url)
    img_arr=np.array(bytearray(img_rsp.content),dtype=np.uint8)
    img=cv2.imdecode(img_arr,-1)
    img=imutils.resize(img,width=1000,height=1800)
    cv2.imshow("Android_cam",img)

    if cv2.waitkey(1)==27:
        beak
cv2.destroyallwindows()