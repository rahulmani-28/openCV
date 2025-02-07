import cv2 as cv
img = cv.imread("C:\\Users\\Thatikonda\\Pictures\\Screenshots\\Screenshot 2025-01-31 110612.png")
cv.imshow('cost',img)
cv.waitKey(0)
cap=cv.VideoCapture("C:\\Users\\Thatikonda\\Pictures\\Screenshots\\Screenshot 2025-01-31 110612.png")
while True:
    istrue,frame=cap.read()
    cv.imshow('vid',frame)
    if(cv.waitKey(0) and 0xff==ord('d')):
        break
cap.release()
cv.destroyAllWindows()