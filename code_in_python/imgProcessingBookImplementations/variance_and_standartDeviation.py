"""
    In the same book that we used to implement the mean, we see the variance and the standart deviation too
    and we have two ways to calculate these statistics
    let's do it
"""
import math
from mean import imageMean
from helpFunctions import convertImageToGrayScale, returnDoctorWhoImage

""" first way """
def imageVarianceFirstWay(grayScaleImage):
    meanOfTheGrayScaleImage = imageMean(grayScaleImage);
    numberOfColumns = int(grayScaleImage.shape[1]); #width of the image
    numberOfRows = int(grayScaleImage.shape[0]); #height of the image
    omega = numberOfColumns * numberOfRows;
    summatory = 0
    for x in range(numberOfColumns):
        for y in range(numberOfRows):
            summatory += pow((grayScaleImage[y][x] - meanOfTheGrayScaleImage), 2);
    return round(summatory / omega, 2)

""" second way """
def imageVarianceSecondWay(grayScaleImage):
    numberOfColumns = int(grayScaleImage.shape[1]); #width of the image
    numberOfRows = int(grayScaleImage.shape[0]); #height of the image
    omega = numberOfColumns * numberOfRows;
    meanSummatory = 0
    varianceSummatory = 0
    for x in range(numberOfColumns):
        for y in range(numberOfRows):
            I_value = grayScaleImage[y][x];
            varianceSummatory += pow(I_value, 2);
            meanSummatory     += I_value
    Mean = meanSummatory/omega;
    variance = (varianceSummatory/omega) - pow(Mean, 2)
    return round(variance, 2)


def standartDeviation(variance):
    return math.sqrt(variance);

""" doctorWhoImageGrayScale = convertImageToGrayScale(returnDoctorWhoImage());
dcWhoImageVariance = imageVarianceFirstWay(doctorWhoImageGrayScale);

print("Variance first way: ", dcWhoImageVariance);
print("Variance second way: ", imageVarianceSecondWay(doctorWhoImageGrayScale));
print("Standart deviation: ", standartDeviation(dcWhoImageVariance)); """

