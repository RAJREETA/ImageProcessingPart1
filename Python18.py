import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def Histogram_Computation(Image):
    Image_Height = Image.shape[0]
    Image_Widhth = Image.shape[1]

    Histogram = np.zeros([256], np.int32)

    for x in range(0,Image_Height):
        for y in range(0, Image_Widhth):
            Histogram[Image[x,y]] = + 1

    return Histogram

def Plot_Histogram(Histogram):
    plt.figure()
    plt.title("GrayScale Histogram")
    plt.xlabel("Intensity Level")
    plt.ylabel("Intensity Frequency")
    plt.xlim([0.256])
    plt.plot(Histogram)
    plt.savefig("Histogram_GrayScale.jpg")

def main():

    Input_Image = cv.imread("C:/Users/ABC/Desktop/PavementCrack2.jpg", 0)
    Histogram_GrayScale = Histogram_Computation(Input_Image)

    for i in range(0, len(Histogram_GrayScale)):
        print("Histogram[", i ,"]", Histogram_GrayScale[i])

    Plot_Histogram(Histogram_GrayScale)
    input("Please Enter to Continue...")

#if  _name_ == '_main_':
    main()



