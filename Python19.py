from PIL import Image
import numpy as np
Image = Image.open('C:/Users/ABC/Desktop/PavementCrack2.jpg')

from numpy import asarray
data = asarray(Image)

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

img = load_img("C:/Users/ABC/Desktop/PavementCrack2.jpg")
#newdata = img_to_array(img)