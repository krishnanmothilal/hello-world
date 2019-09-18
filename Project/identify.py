import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while (True):
    #Capture Frame by Frame
    ret,frame=cap.read()
    #Display the resulting Frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

#When everything is done Release the capture
cap.release()
cv2.destroyAllWindows()
