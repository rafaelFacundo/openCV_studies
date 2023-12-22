import cv2 as cv

doctorWhoImage = cv.imread('photos/doctor.jpg');
#cv.imshow("Doctor who", doctorWhoImage);

""" convert to gray scale """
#doctorWhoGray = cv.cvtColor(doctorWhoImage, cv.COLOR_BGR2GRAY)

""" blur image """
#blurDoctor = cv.GaussianBlur(doctorWhoImage, (13,13), cv.BORDER_DEFAULT)

""" edge cascade """
#cannyDoctor = cv.Canny(doctorWhoImage, 125, 175)

""" dilating the image """
cannyDoctor = cv.Canny(doctorWhoImage, 125, 175)
dilated = cv.dilate(cannyDoctor, (13,13), iterations=4)

""" eroding the image """
erodedDoctor = cv.erode(dilated, (3,3), iterations=1)

""" resize function from opencv """
#resized = cv.resize(doctorWhoImage, (500,500), interpolation=cv.INTER_AREA)

""" cropping """
cropped = doctorWhoImage[50:200, 200:400]

cv.imshow("Doctor who", cropped);
cv.waitKey(0);