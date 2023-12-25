import cv2 as cv

def returnDoctorWhoImage():
    return cv.imread("photos/doctor.jpg");

def convertImageToGrayScale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY);