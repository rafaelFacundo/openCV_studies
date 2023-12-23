import cv2 as cv
import numpy as np 

doctorWhoImage = cv.imread('photos/doctor.jpg');

blankImag = np.zeros(doctorWhoImage.shape[:2], dtype='uint8');

b,g,r = cv.split(doctorWhoImage);

blue = cv.merge([b, blankImag, blankImag])
green = cv.merge([g, blankImag, blankImag])
red = cv.merge([r, blankImag, blankImag])

merged = cv.merge([b,g,r])

cv.imshow("Doctor who", blue);
cv.waitKey(0);