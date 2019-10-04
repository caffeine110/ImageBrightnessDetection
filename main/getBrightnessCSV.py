###########################################################################
"""     AIM : Image Brightness Detection
        
            : input     : filename.jpg/png
            : output    : Predicted Brightness Value
            : Author    : Gaurav Gaukar
            : Client    : SIGNZY
            : Date      : 02:47 on 5th Oct 2019

"""


###########################################################################
#importing required dependencies
from PIL import Image
from PIL import ImageStat
import math
import os
import sys

# for visualisation
import matplotlib.pyplot as plt



###########################################################################
# Function to print Meta Data of Image
def getMetaData(filePath):
    # create object
    img = Image.open(filePath)
    Stats = ImageStat.Stat(img)

    # print size of image
    size = img.size
    print("Size of Image is :", size)

    # print pixels in image
    print("Number of (R G B) pixels is : ", Stats.count)
    print("Min/max values for each band in the image : ",Stats.extrema)
    print("Total number of pixels for each band in the image : ",Stats.count)
    print("Sum of all pixels for each band in the image : ",Stats.sum)
    print("Squared sum of all pixels for each band in the image : ",Stats.sum2)
    print("Average (arithmetic mean) pixel level for each band in the image : ",Stats.mean)
    print("Median pixel level for each band in the image : ",Stats.median)
    print("RMS (root-mean-square) for each band in the image : ",Stats.rms)
    print("Variance for each band in the image : ",Stats.var)
    print("Standard deviation for each band in the image : ",Stats.stddev)
    print("\n")



###########################################################################
# Mean of rgb pixels
def getMeanBrightenss(filePath):
    img = Image.open(filePath)
    Stats = ImageStat.Stat(img)
    r,g,b = Stats.mean
    MeanB255 = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    
    MeanB10 = ( MeanB255/255 )* 10
    return MeanB255, MeanB10


# Median
def getMedianBrightness(filePath):
    img = Image.open(filePath)
    Stats = ImageStat.Stat(img)
    r,g,b = Stats.median
    MeanB255 = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

    MeanB10 = ( MeanB255/255 )* 10
    return MeanB255, MeanB10


# RMS
def getRMSBrightness(filePath):
    img = Image.open(filePath)
    Stats = ImageStat.Stat(img)
    r,g,b = Stats.rms
    MeanB255 = math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))

    MeanB10 = ( MeanB255/255 )* 10
    return MeanB255, MeanB10



###########################################################################
# plot the Image with Its Predicted Brightness Value
def plotData(filePath):
    img = Image.open(filePath)

    fig = plt.figure()
    a = fig.add_subplot()
    imgplot = plt.imshow(img)

    print("Measured Value :: \t\t ( From 0-255 || From 0-10 )")
    meanB = "Mean Brightness Detected :\t" + str(getMeanBrightenss(filePath))
    medianB = "Median Brightness Detected :\t" + str(getMedianBrightness(filePath))
    rmsB = "RMS Brightness Detected :\t" + str(getRMSBrightness(filePath))
    
    fB = ( getMeanBrightenss(filePath)[1] + getMedianBrightness(filePath)[1] + getRMSBrightness(filePath)[1] )/3

    finalB = "Final Predicted Value for Brightness in range of (0-10) is : " + str(fB)

    plt.show()
    print(meanB)
    print(medianB)
    print(rmsB)
    print()
    print(finalB)
    print()




###########################################################################
# Save Predicted Brightness Value in .csv file
import csv

def generateCSV(dirPath):
    # optn file in write mode
    with open('finalBrightness.csv', mode='w') as csv_file:
        fieldnames = ['MeanB', 'MedianB', 'RMSB', 'FinalB']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        # list all the images in dirictory
        Li_img = os.listdir(dirPath)

        for i in Li_img:
            filePath = dirPath + i

            meanB = getMeanBrightenss(filePath)[1]
            medianB = getMedianBrightness(filePath)[1]
            rmsB = getRMSBrightness(filePath)[1]
            finalB = ( getMeanBrightenss(filePath)[1] + getMedianBrightness(filePath)[1] + getRMSBrightness(filePath)[1] )/3

            #print(meanB, medianB, rmsB, finalB)
            writer.writerow({'MeanB':meanB , 'MedianB':medianB , 'RMSB':rmsB , 'FinalB':finalB })
 



###########################################################################
# main method
def main():
    #filePath = "test/.png"
    argumentList = sys.argv
    dirPath = argumentList[1]

    #print(argumentList)
    #print("Program for || BRIGHTNESS DETECTION ||")
    #print("\nFilePath to be opened is : ", filePath)
    #print()

    #getMetaData(filePath)
    generateCSV(dirPath)


###########################################################################
# call to main
if __name__ == "__main__":
    main()




print("Program Exicuted Succesfully...EOF...!!")