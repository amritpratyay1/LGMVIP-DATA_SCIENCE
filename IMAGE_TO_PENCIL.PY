# By AMRIT PRATYAY

# IMAGE TO PENCIL SKETCH USING PYTHON

# TASH 1 (BEGINNER LEVEL)

#------------CODE----------------#



#importing the cv2 library
import cv2


# reading the colourful jpg format of pic to be converted
image = cv2.imread("dog.jpg")
cv2.imshow("IMAGE",image)
cv2.waitKey(0)

#converting the colourful pic to gray_image
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("NEW_IMAGE:",gray_image)
cv2.waitKey(0)

#inverting the gray_image
inverted_image = 255 - gray_image
cv2.imshow("INVERTED_IMAGE:",inverted_image)
cv2.waitKey(0)

#converting the inverted image to blurr
blurred = cv2.GaussianBlur(inverted_image,(21,21),0)

#dividing the gray_image with inverted_blurred image to get pencil_sketch look of colourful image 
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image,inverted_blurred,scale=256)
cv2.imshow("IMAGE_PENCIL_SKETCH:",pencil_sketch)
cv2.waitKey(0)


cv2.imshow("ORIGINAL_IMAGE_COLOURFUL:",image)
cv2.imshow("PENCIL_SKETCH:",pencil_sketch)
cv2.waitKey(0) 
