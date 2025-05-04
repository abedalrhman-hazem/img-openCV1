import cv2
facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('sswd.png')
cap=cv2.VideoCapture()

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
fac=facec.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in fac:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
print(len(fac))
cv2.imshow('img',img)
cv2.waitKey(0)