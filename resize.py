import cv2 as cv
img=cv.imread("D:\Machinelearing\OpenCV\op1.jpeg")
resized_img=cv.resize(img,(300,300))
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('OG',img)
cv.imshow('Reszie',resized_img)

cv.imshow('gray scale',gray)
cv.waitKey(0)
cv.destroyAllWindows()