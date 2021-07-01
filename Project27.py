import cv2
import numpy as np

print("Package Imported")

path = 'C:/Users/ABC/Downloads/ProjectPictures/GlassCrack/GalssCrack9.jpg'
img = cv2.imread(path)

Kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgCanny = cv2.Canny(img, 300, 400)

imgDialated = cv2.dilate(imgCanny, Kernel, iterations=1)
imgEroded = cv2.erode(imgDialated, Kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dia Image", imgDialated)
cv2.imshow("Ero Image", imgEroded)
cv2.waitKey(0)
# needed to install numpy, opencv, keras
