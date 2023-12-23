import cv2 as cv
#import matplotlib.pyplot as plt

img = cv.imread("photos/doctor.jpg")


""" bgr to grayscale """
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


""" bgr to hsv """
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

""" bgr to l x a x b """
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

""" bgr to rgb """
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow("Doctor who", rgb);
cv.waitKey(0);
