import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack4.jpg')
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

divb = np.split(b,8)  # divide b in submatrices 8x8?
divg = np.split(g,8)  # divide g in submatrices 8x8?
divr = np.split(r,8)  # divide r in submatrices 8x8?

print('blue:', b)
print('red:', g)
print('green:', r)

cv2.imshow('img',img)