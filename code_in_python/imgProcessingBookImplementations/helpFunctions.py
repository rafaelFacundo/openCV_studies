import cv2 as cv

"""
    this function just returns the doctor who image that we are using
    to study.
"""
def returnDoctorWhoImage():
    return cv.imread("photos/doctor.jpg");

"""
    This function returns a gray scale image of the image passed as parameter.
"""
def convertImageToGrayScale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY);

"""
    this function returns three scalar images each corresponding to
    a color channel. 
    Blue, red and green
"""
def decompseImageInRGBchannels(image):
    return cv.split(image);

"""
    this function just shows a image
"""
def displayImage(image, nameOfTheWindow="image"):
    cv.imshow(nameOfTheWindow, image);
    cv.waitKey(0)