import cv2
import numpy as np

print("Package Imported")

# path = 'C:/Users/ABC/Desktop/PavementCrack2.jpg'

# path = 'C:/Users/ABC/Desktop/WallCrack5.jpg'
# path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/Paveementcrack5.jpg'

# path = 'C:/Users/ABC/Downloads/ProjectPictures/PlateCupCrack/PlateCrack2.jpg'

path = 'C:/Users/ABC/Downloads/good.jpg'

img = cv2.imread(path)
green_image = img[:,:,1]
print(green_image)
Kernel = np.ones((5, 5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 1000, 1000)

imgDialated = cv2.dilate(imgCanny, Kernel, iterations=1)
imgEroded = cv2.erode(imgDialated, Kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dia Image", imgDialated)
cv2.imshow("Ero Image", imgEroded)
cv2.waitKey(0)
# needed to install numpy, opencv, keras
