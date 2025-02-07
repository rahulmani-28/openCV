import cv2 as cv
img=cv.imread("D:\Machinelearing\OpenCV\op1.jpeg")
cv.putText(img,"Hello",(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
cv.imshow('With Text',img)
cv.waitKey(0)
cv.destroyAllWindows()
