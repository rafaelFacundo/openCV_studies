from helpFunctions import returnDoctorWhoImage, decompseImageInRGBchannels, displayImage
import matplotlib.pyplot as plt


doctorWhoImage = returnDoctorWhoImage();

def intensityProfileInARow(image, lineIndex):
    """
        taking the width to run trought the columns of a specific row specified
        in the parameter lineIndex
    """
    width = image.shape[1];
    height = image.shape[0]; #taking the height, i.e the number of lines in the image
    intensityValues = [];
    if lineIndex >=0 and lineIndex < height:
        b, r, g = decompseImageInRGBchannels(image);
        for x in range(width):
            intensityValues.append((b[lineIndex][x] + r[lineIndex][x] + g[lineIndex][x])/3)
    return intensityValues;

doctorWhoImageIntesityInrow = intensityProfileInARow(doctorWhoImage, 50);

""" displayImage(doctorWhoImage); """

""" plt.plot(doctorWhoImageIntesityInrow);
plt.xlabel("index in x axis");
plt.ylabel("intesity values");
plt.show();
     """

