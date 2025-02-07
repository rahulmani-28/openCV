import cv2 as cv
face_model = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
img=cv.imread('D:\Machinelearing\OpenCV\image.png')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255),3)
cv.imshow("Faces",img)
cv.waitKey(0)
cv.destroyAllWindows()