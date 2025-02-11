import cv2 as cv
face_model = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_frontalface_default.xml")
cap=cv.VideoCapture(0)
if face_model.empty():
    print("Error: Haar cascade model not loaded!")
    exit()
while True:
    ret,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    

    faces=face_model.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    for(x,y,w,h) in faces:
        face=frame[y:y+h,x:x+w]
        blurred_face = cv.GaussianBlur(face,(99,99),20)  
        frame[y:y+h, x:x+w] = blurred_face

    cv.imshow('blurry',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv.destroyAllWindows()