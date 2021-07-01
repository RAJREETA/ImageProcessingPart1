# import required module
from PIL import Image

# get image
filepath =  'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack26.jpg' # 400,500 -- 14

#path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack19.jpg' # 300,400 = 201

# path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack22.jpg'  # (280,340) == 63

# 4. path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/Paveementcrack5.jpg' #(470, 550) = 186

# 5. path = 'C:/Users/ABC/Downloads/ProjectPictures/WallCrack/WallCrack9.jpg' # (450, 500) = 52

# 6.path = 'C:/Users/ABC/Downloads/ProjectPictures/GlassCrack/GalssCrack9.jpg' #(300, 450) = 58
# path = 'C:/Users/ABC/Downloads/ProjectPictures/PavementCrack/PavementCrack21.jpg' #(350, 400) = 56


# 8. path = 'C:/Users/ABC/Downloads/ProjectPictures/GlassCrack/Glasscrack10.jpg' #(350,450)



img = Image.open(filepath)

# get width and height
width = img.width
height = img.height

# display width and height
print("The height of the image is: ", height)
print("The width of the image is: ", width)