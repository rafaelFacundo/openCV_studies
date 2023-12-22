import cv2 as cv
import numpy as np

blankImage = np.zeros((500,500, 3), dtype='uint8')

""" doctorWhoImage = cv.imread('photos/doctor.jpg');
cv.imshow("DOctor", doctorWhoImage); """

""" paint the image a certain colour """
""" blankImage[:] = 0,255,0 """



""" draw a rectangle """
#cv.rectangle(blankImage, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)

""" draw a circle """
#cv.circle(blankImage, (blankImage.shape[1]//2,blankImage.shape[0]//2), 40, (0,0,255), thickness=3 )

""" draww a line """
#cv.line(blankImage, (0,0), (250,250), (0,255,0), thickness=2)

""" write text """
cv.putText(blankImage, "HEllo", (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)

cv.imshow("GReen", blankImage)
cv.waitKey(0)