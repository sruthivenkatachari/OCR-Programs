import cv2
import numpy as np
import pytesseract
from PIL import Image
import imutils

# Path of working folder on Disk
src_path = "C:\\New folder (3)\\front-invert"
img_path="C:\\New folder (3)\\front-invert\\102a.jpg"


img = cv2.imread(img_path)
img1=imutils.resize(img,height=100)
cv2.imshow("img",img1)
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow("img1",img)

# Apply dilation and erosion to remove some noise
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
# Write image after removed noise
cv2.imwrite(src_path + "\\ removed_noise.png", img)
#  Apply threshold to get image with only black and white
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
# Write the image after apply opencv to do some ...
cv2.imwrite(src_path + "\\thres.png", img)
# Recognize text with tesseract for python
TESSDATA_PREFIX="C:\\Program Files (x86)\\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img1=Image.open(src_path + "\\thres.png")
print(img1)
result=pytesseract.image_to_string(img1)
print(result)
cv2.waitKey(0)
cv2.destroyAllWindows()

			



cv2.waitKey(0)
cv2.destroyAllWindows()
