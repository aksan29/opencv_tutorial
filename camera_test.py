import cv2

cap = cv2.VideoCapture(0)

def camera_test(cap):
    while True :
        _, frame = cap.read()
        cv2.imshow('frame' , frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

camera_test(cap)
cap.release()
cv2.destroyAllWindows()