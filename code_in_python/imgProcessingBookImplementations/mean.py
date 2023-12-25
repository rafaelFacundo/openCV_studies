"""
    In the book Concise Computer Vision An Introduction into Theory and Algorithms we see in the first chapter
    some basic statistics about images, the first one is the Mean that is defined by
    1/(Nrows * Ncols) * sum X=1 -> Ncols sum Y=1 -> Nrows I(x,y)
    But we simplify this formula like this
    first defining omega = Nrows * Ncols
    then the formula is 1/|omega| * sum (x,y) ∈ omega (I(x,y))
    We apply this formula to a gray scale image
"""
import cv2 as cv



def imageMean(grayScaleImage):
    numberOfColumns = int(grayScaleImage.shape[1]); #width of the image
    numberOfRows = int(grayScaleImage.shape[0]); #height of the image
    omega = numberOfColumns * numberOfRows;
    summatory = 0
    for x in range(numberOfColumns):
        for y in range(numberOfRows):
            summatory += grayScaleImage[y][x]
    return round(summatory / omega, 2)

doctorWhoImage = cv.imread("photos/doctor.jpg");


doctorWhoImageGrayScale = cv.cvtColor(doctorWhoImage, cv.COLOR_BGR2GRAY);

doctorWhoImageMean = imageMean(doctorWhoImageGrayScale);
stringWithTheMean = "The mean of this image is: " + str(doctorWhoImageMean)

""" puting text with the values of the mean in the image """
cv.putText(doctorWhoImageGrayScale, stringWithTheMean, (50,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2);

cv.imshow("Doctor who", doctorWhoImageGrayScale);
cv.waitKey(0);
