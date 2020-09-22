import cv2
import numpy as np 
import matplotlib.pyplot as plt 
from imutils import contours
import imutils
from imutils.perspective import four_point_transform
img=cv2.imread("C:\\New folder (3)\\imag\\Scan ITEM1.jpg")
image = imutils.resize(img, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
#to save the image
#cv2.imsave("")

cnts=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("no of shapes {0}",format(len(cnts)))
cnts = imutils.grab_contours(cnts)


#displayCnt = None
for c in cnts:
	# approximate the contour
	rect=cv2.minAreaRect(c)
	box=cv2.boxPoints(rect)
	box=np.int0(box)
	img=cv2.drawContours(image,[box],0,(0,255,0),3)
	#peri = cv2.arcLength(c, True)
	#approx = cv2.approxPolyDP(c, 0.02 * peri, True)
plt.figure("example1")
plt.imshow(img)
plt.title("binary contours")
plt.show()
#cv2.destroyAllWindows()
for cnt in cnts:
	epsilon=0.01*cv2.arcLength(cnt,True)
	approx=cv2.approxPolyDP(cnt,epsilon,True)
	img1=cv2.drawContours(image,[approx],0,(0,255,0),3)
plt.figure("example1")
plt.imshow(img1)
plt.title("binary contours")
plt.show()
cv2.destroyAllWindows()
