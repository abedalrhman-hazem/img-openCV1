import cv2

img =cv2.imread('Scr.png')
imgsize = img.shape
print (imgsize)
imgHSV =cv2.cvtColor(img,cv2.COLOR_RGB2HSV)

imgRes = cv2.resize(img,(1000,600))
print (imgRes.reshape)

imgcrop = img[100:200,200:900]

cv2.imshow('Scr.png',img)
cv2.imshow('Scr',imgHSV)
#cv2.imshow('imgRes',imgRes)
cv2.imshow('imgcrop',imgcrop)
cv2.waitKey(0)