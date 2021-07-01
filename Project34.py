import cv2
import numpy as np

#read image
src = cv2.imread('C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack12.jpg', cv2.IMREAD_UNCHANGED)
print(src.shape)

# extract red channel
red_channel = src[:,:,2]
cv2.imshow("Red Pic", red_channel)
# create empty image with same shape as that of src image
red_img = np.zeros(src.shape)
cv2.imshow("Red Pic", red_img)
#assign the red channel of src to empty image
red_img[:,:,2] = red_channel
cv2.imshow("Red Pic", red_img)
cv2.imshow("Red Pic", red_channel)


#save image
# cv2.imwrite('D:/cv2-red-channel.png',red_img)

cv2.waitKey(0)