import cv2 as cv
face_model = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
cap=cv.VideoCapture(0)
while True:
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=face_model.detectMultiScale(gray,
    scaleFactor=1.1,minNeighbors=5,minSize=(20,20))
    for(x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
    cv.imshow("Real Time face detected",frame)
    if cv.waitKey(20) and 0xff==ord('q'):
        break
cap.release()
cv.destroyAllWindows()