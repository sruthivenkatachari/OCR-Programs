import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import imutils
from imutils import contours
from PIL import Image
import pytesseract


#to read image and print it
img=cv2.imread("C:\\New folder (3)\\imag\\Scan ITEM1.jpg",0)
#print(img)
#to resize it and print it as orginal
image=imutils.resize(img,height=500)
#to crop the image
heigt,width=image.shape[:2]
start_row,start_col=int(heigt*0.06),int(width*.76)
end_row,end_col=int(heigt*0.2),int(width*.98)
cropped=image[start_row:end_row,start_col:end_col]
#to print resized and cropped image 
cv2.imshow("cropped",cropped)

#save the ropped image

cv2.imwrite("C:\\New folder (3)\\outputs\\Scan ITEM5.jpg",cropped)
cv2.waitKey(0)
#cv2.imshow("orginal",img)
cv2.imshow("resize",image)
cv2.waitKey(0)
#finding contours
#to blur and edge it
image1=cv2.imread("C:\\New folder (3)\\outputs\\Scan ITEM5.jpg")

gray=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
edged=cv2.Canny(blurred,50,200,255)
####finding the contours#####
cnts=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("no of shapes {0}",format(len(cnts)))
cnts = imutils.grab_contours(cnts)
#for c in cnts:
	# approximate the contour
	#rect=cv2.minAreaRect(c)
	#box=cv2.boxPoints(rect)
	#box=np.int0(box)
	#img=cv2.drawContours(image1,[box],0,(0,255,0),2)
#plt.figure("example1")
#plt.imshow(image1)
#plt.title("binary contours")
#plt.show()
#####polygon approximation#####
for cnt in cnts:
	epsilon=0.01*cv2.arcLength(cnt,True)
	approx=cv2.approxPolyDP(cnt,epsilon,True)
	img1=cv2.drawContours(image1,[approx],0,(0,255,0),1)
plt.figure("example1")
plt.imshow(img1)
plt.title("binary contours")
plt.show()

###to read the content in the image####
TESSDATA_PREFIX="C:\\Program Files (x86)\\Tesseract-OCR"
#uncomment below line if you dont want to set "Environment variables" path
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe" 
img4=Image.open('C:\\New folder (3)\\outputs\\Scan ITEM5.jpg')
result=pytesseract.image_to_string(img4)
with open('magic.txt',mode='w') as file:
	file.write(result)
	print('open the file and see') 
print(result)
cv2.waitKey(0)
cv2.destroyAllWindows()










