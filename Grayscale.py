import cv2
import imutils
image1=cv2.imread("C:\\New folder (3)\\front\\5.jpg")
image=imutils.resize(image1,height=500)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray image",gray)
cv2.imwrite("C:\\New folder (3)\\front\\5a.jpg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()