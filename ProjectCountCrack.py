# To count number of whites from the eroded image to know the severity of the crack

# Worked Result given Output
# Final Project

import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1. path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack26.jpg' # 400,500 -- 14

# 2. path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack19.jpg' # 300,400 = 201

# 3. path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack22.jpg'  # (280,340) == 63

# 4. path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/Paveementcrack5.jpg' #(470, 550) = 186

# 5. path = 'C:/Users/ABC/Downloads/ProjectPictures/WallCrack/WallCrack9.jpg' # (450, 500) = 52


# 6. path = 'C:/Users/ABC/Downloads/ProjectPictures/GlassCrack/GalssCrack9.jpg' #(300, 450) = 58

# 7. path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack21.jpg' #(350, 400) = 56

img= cv2.imread(path)
Kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)

imgCanny = cv2.Canny(img, 450, 540)

imgDialated = cv2.dilate(imgCanny, Kernel, iterations=1)
imgEroded = cv2.erode(imgDialated, Kernel, iterations=1)

(cnt, hierarchy) = cv2.findContours(imgEroded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

plt.imshow(rgb)

print("Pavement Crack 22")

print('Number of Cracks', len(cnt))
if ((len(cnt)) < 50):
    print("Small Crack")
if (((len(cnt)) > 50) and ((len(cnt)) < 100)):
    print("Medium Crack")
if ((len(cnt)) > 150):
    print("Large Crack")