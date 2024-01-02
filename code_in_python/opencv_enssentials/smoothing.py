import cv2 as cv
import numpy as np 

doctorWhoImage = cv.imread('photos/doctor.jpg');

""" averaging """
average = cv.blur(doctorWhoImage, (7,7))

""" gaussian - less blur, but more natural, because of the weights"""
""" zero is the standart deviation in the x direction """
gauss = cv.GaussianBlur(doctorWhoImage, (7,7), 0)

""" median blur - less noise """
median = cv.medianBlur(doctorWhoImage, 7)

""" bilateral - most effective - it blurs the image but retain the edges"""
bilateral = cv.bilateralFilter(doctorWhoImage, 50, 15, 15)


cv.imshow("Doctor who", bilateral);
cv.waitKey(0);