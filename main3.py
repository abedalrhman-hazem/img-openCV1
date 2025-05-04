import cv2
import numpy as np
img = np.zeros((600,600,3),np.uint8)
#img[:] =60,100,2
print(img.shape)
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
#cv2.rectangle(img,(50,50),(500,500),(0,50,23),2)
cv2.circle(img,(300,300),150,(100,52,50))
cv2.putText(img,'OPENCV ABED',(20,200),cv2.FONT_HERSHEY_COMPLEX,1,(200,255,35),1)
cv2.imshow('img',img)
cv2.waitKey(0)