import cv2 as cv
import numpy as np


doctorWhoImage = cv.imread('photos/doctor.jpg');
blankImag = np.zeros(doctorWhoImage.shape[:2], dtype='uint8');



cv.imshow("Doctor who", doctorWhoImage);
cv.waitKey(0);