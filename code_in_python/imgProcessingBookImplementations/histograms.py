import cv2 as cv
""" import matplotlib.pyplot as plt """
from helpFunctions import returnDoctorWhoImage


""" doctorWhoImage = returnDoctorWhoImage();

b, r, g = cv.split(doctorWhoImage); """

def computerHistogram(oneChannelImage):
    values = {i: 0 for i in range(256)};
    numberOfColumns = oneChannelImage.shape[1]; #width
    numberOfRows = oneChannelImage.shape[0];    #rows
    for x in range(numberOfColumns):
        for y in range(numberOfRows):
            frenquency = oneChannelImage[y][x]
            values[frenquency] += 1;
    return (list(values.keys()), list(values.values()));

""" (frenquencies, occurances) = computerHistogram(r); """

""" plt.plot(occurances);
plt.ylabel("occurances");
plt.xlabel("frequencies");
plt.show() """

""" doctHist = cv.calcHist([doctorWhoImage], [1], None, [256], [0,256]);
plt.plot(doctHist);
plt.ylabel("occurances");
plt.xlabel("frequencies");
plt.show(); """