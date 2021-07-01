import cv2


img = cv2.imread('C:/Users/ABC/Desktop/PavementCrack2.jpg')
b,g,r = cv2.split(img)

def sub_matrices(color_channel):
    matrices = []
    #How can you change how this loop iterates?
    #Also consider adding stopping conditions and/or additional loops for
    #excess parts of the image.
    for i in range(int(color_channel.shape[0]/8)):
        for j in range(int(color_channel.shape[1]/8)):
            matrices.append(color_channel[i*8:i*8 + 8, j*8:j*8+8])
    return matrices

#returns list of sub matrices
r_submatrices = sub_matrices(r)

print(r_submatrices)