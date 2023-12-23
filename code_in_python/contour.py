import cv2 as cv

img = cv.imread("photos/doctor.jpg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY);

""" blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT);


canny = cv.Canny(blur, 125, 175)
 """

ret, thresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print("counts :", len(contours))

cv.imshow("doc", thresh)
cv.waitKey(0);