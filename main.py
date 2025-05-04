import cv2

img =cv2.imread('Scr.png')
imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlue=cv2.GaussianBlur(imgGray,(9,9),0)
imgCanny=cv2.Canny(img,200,200)
cv2.imshow('Scr.png',img)
cv2.imshow('Gray img', imgGray)
cv2.imshow('Blue img', imgBlue)
cv2.imshow('Canny img', imgCanny)
cv2.waitKey(0)