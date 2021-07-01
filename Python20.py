import cv2
import numpy as np
import matplotlib.pyplot as plt
import  matplotlib.image as mping

 # % matplotlib notebook

img = cv2.imread('C:/Users/ABC/Desktop/PavementCrack2.jpg')

# Convert the image to GrayScale

image = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Print the number of shapes found

print("Number of Shapes {0}".format(len(contours)))

# Now lets draw the Contours

for cnt in contours:
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    img = cv2.drawContours(img, [box], 0, (0,255,0), 3)

plt.figure("Example 1")
plt.imshow(img)
plt.title('Binary contours in an Image')
plt.show()
