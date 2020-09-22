# Python program to illustrate 
# template matching 
import cv2 
import numpy as np 
#from pyimagesearch.transform import four_point_transform
from transform import four_point_transform
import numpy as np
import argparse
import cv2
import imutils
from skimage.filters import threshold_local
import pytesseract
from PIL import Image

# Read the main image 
image=cv2.imread("Scan ITEM99.jpg")
image=cv2.resize(image,(500,600))
cv2.imwrite("Scan orig.jpg",image)
#image=str(image)
img_rgb = cv2.imread("Scan orig.jpg") 
cv2.imshow("original",img_rgb)

# Convert it to grayscale 
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow("original gray",img_gray) 

# Read the template 
template = cv2.imread("C:\\New folder (3)\\Scan orig43.jpg",0)
cv2.imshow("template gray",template)
cv2.imwrite("template.jpg",template) 

# Store width and heigth of template in w and h 
w, h = template.shape[::-1] 

# Perform match operations. 
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED) 

# Specify a threshold 
threshold = 0.8

# Store the coordinates of matched area in a numpy array 
loc = np.where( res >= threshold) 

# Draw a rectangle around the matched region. 
for pt in zip(*loc[::-1]): 
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,0), 10) 

# Show the final image with the matched area.    
cv2.imshow('Detected',img_rgb) 
cv2.imwrite("detect.jpg",img_rgb)

image=cv2.imread("detect.jpg")   #read in the image
ratio = image.shape[0] / 500.0 #resizing because opencv does not work well with bigger images
orig=image.copy()
image = imutils.resize(image, height = 500)
(h, w, d) = image.shape
print("w: {}, h: {}, d: {}".format(w, h, d))
# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
 
# show the original image and the edge detected image
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)

#Building a Document Scanner App using Python, OpenCV, and Computer VisionPython
# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
#print(cnts)
# loop over the contours
for c in cnts:
    p=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*p,True)
    print(len(approx))
    if len(approx)==4:
    	target=approx
    	break


   
print(target)
print(target)
# show the contour (outline) of the piece of paper
print("STEP 2: Find contours of paper")
cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)

# apply the four point transform to obtain a top-down
# view of the original image
warped = four_point_transform(orig, target.reshape(4, 2) * ratio)
cv2.imshow("warped1",warped)
cv2.imwrite("warped1.jpg",warped)

gray1 = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (5, 5), 0)
edged1 = cv2.Canny(gray1, 100, 200)
cv2.imshow("edged",edged1)
cv2.imwrite("edgednow.jpg",edged1)

TESSDATA_PREFIX="C:\\Program Files (x86)\\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img4=Image.open("edgednow.jpg")
result=pytesseract.image_to_string(img4)
print(result)


 





cv2.waitKey(0)
cv2.destroyAllWindows()
