import Image
from PIL import image
import matplotlib.pyplot as plt
import numpy as np

img = np.array(Image.open(C:/Users/ABC/Downloads/ProjectPictures/PavementCrack5.jpg).convert('L'))
print(img)

L= R * (0.299 + C*(0.587) + B * (0.114))
plt.gray()
plt.imshow(img)
plt.figure('Example1')
plt.hist(in.flatten(),255)
plt.show()