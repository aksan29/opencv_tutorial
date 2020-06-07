import cv2
import pyzbar.pyzbar as pyzbar

cap= cv2.VideoCapture(0)
while True :
    _,frame = cap.read()
    objectDecode = pyzbar.decode(frame)
    for obj in objectDecode:
        print(obj.data)
        cv2.putText(frame , str(obj.data) ,(50,50) , cv2.FONT_HERSHEY_PLAIN,2 , (255,0,0),2)
    cv2.imshow('Barcode',frame)
    k = cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()