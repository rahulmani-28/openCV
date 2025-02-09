import cv2 as cv
eye_model=cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_eye.xml")
cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    eyes=eye_model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(20,20))
    for(x,y,w,h) in eyes:
        cv.rectangle(frame,(x,y),(x+w,y+h),(221,22,67),3)
    cv.imshow("Real Time Eyes detected",frame)
    if cv.waitKey(20) and 0xff==ord('q'):
        break
cap.release()
cv.destroyAllWindows()