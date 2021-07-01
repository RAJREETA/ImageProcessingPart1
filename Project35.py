import cv2
import numpy as np
import matplotlib from pyplot as plt

img = cv2.imread('C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack12.jpg')
b,g,r = cv2.split(img)       # get b,g,r
rgb_img = cv2.merge([r,g,b])
plt.imshow(rgb_img)

x,y,z = np.shape(img)
red = np.zeros((x,y,z),dtype=int)
green = np.zeros((x,y,z),dtype=int)
blue = np.zeros((x,y,z),dtype=int)
for i in range(0,x):
    for j in range(0,y):
        red[i][j][0] = rgb_img[i][j][0]
        green[i][j][1]= rgb_img[i][j][1]
        blue[i][j][2] = rgb_img[i][j][2]
plt.imshow(red)
plt.imshow(green)
plt.imshow(blue)

cv2.imshow(red)
cv2.imshow(green)
cv2.imshow(blue)

#Now we will again create the original image from these Red, Blue and Green Images

retrack_original = np.zeros((x, y, z), dtype=int)
for i in range(0,x):
    for j in range(0,y):
        retrack_original[i][j][0] = red[i][j][0]
        retrack_original[i][j][1] = green[i][j][1]
        retrack_original[i][j][2] = blue[i][j][2]
plt.imshow(retrack_original)
cv2.waitKey(0)


