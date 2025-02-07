import cv2 as cv
img=cv.imread('D:\Machinelearing\OpenCV\image.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges=cv.Canny(gray,200,300)
cv.imshow("OG",img)
cv.imshow("edges",edges)
cv.waitKey(0)
cv.destroyAllWindows()