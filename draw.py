import cv2 as cv
img=cv.imread("D:\Machinelearing\OpenCV\op1.jpeg")
img2=cv.resize(img,(500,500))
cv.line(img2,(0,50),(100,250),(0,255,255),3)
cv.rectangle(img2,(0,50),(100,150),(255,0,155),3)
cv.circle(img2,(300,350),5,(255,255,255),-1)
cv.imshow('img',img2)
cv.waitKey(0)
cv.destroyAllWindows()