import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours :
         area = cv2.contourArea(cnt)
         print(area)
         if (area > 500):
           cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
           peri = cv2.arcLength(cnt,True)
           print(peri)
           approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
           print(len(approx))
           objCor = (len(approx))
           x, y, w, h = cv2.boundingRect(approx)
           cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 2) # I have to give the values of x, y, w, h. So to find Area and Perimeter.


path = 'C:/Users/ABC/Desktop/PavementCrack2.jpg'

img = cv2.imread(path)

imgContour = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)

imgCanny = cv2.Canny(imgBlur, 50, 50)

imgBlank = np.zeros_like(img)

cv2.imshow("Original Image", img)

cv2.imshow("Gray Image", imgGray)

cv2.imshow("Blur Image", imgBlur)

cv2.waitKey(0)

# I need to run the program of getting the coordinates where I click on the Image on the screen. Till now this program is not working.