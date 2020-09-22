import cv2
 
def funcRotate(degree=0):
    degree = cv2.getTrackbarPos('degree','Frame')
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    rotated_image = cv2.warpAffine(original, rotation_matrix, (width, height))
    cv2.imshow('Rotate', rotated_image)
 
if __name__== '__main__':
    image=cv2.imread('Scan ITEM9.jpg')
    image_resize=cv2.resize(image,(1300,500),interpolation=cv2.INTER_AREA)
    cv2.imshow('Area Based Scaling',image_resize)
    cv2.imwrite("Scan ITEM9a.jpg",image_resize)
    cv2.waitKey(0)
    original=cv2.imread("Scan ITEM9a.jpg",1)
    height, width = original.shape[:2]
    cv2.namedWindow('Frame')
    degree=0
    cv2.createTrackbar('degree','Frame',degree,360,funcRotate)
    funcRotate(0)
    cv2.imshow('Frame',original)
    cv2.waitKey(0)
 
cv2.destroyAllWindows()