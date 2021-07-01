import cv2
import numpy as np

#read image
src = cv2.imread('C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack12.jpg', cv2.IMREAD_UNCHANGED)
print(src.shape)

# extract green channel
green_channel = src[:,:,1]

# create empty image with same shape as that of src image
green_img = np.zeros(src.shape)

#assign the green channel of src to empty image
green_img[:,:,1] = green_channel
print(green_channel)
#save image
# cv2.imwrite('D:/cv2-green-channel.png',green_img)
