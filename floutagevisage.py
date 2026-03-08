import cv2

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x,y,w,h) in faces :
        img = cv2.rectangle(frame, (x,y), (x + w, y + h), (0,0,255))
        img [y:y+h, x:x+w] = cv2.medianBlur(img[y:y+h, x:x+w], 55)
    
    cv2.imshow('image', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows
