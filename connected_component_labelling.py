from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

#binarize image
img = cv2.imread("Lab4-image.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval,threshold = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

#make matrix of dimension that of image
height,width = img.shape[0],img.shape[1]
matrix = np.zeros((height,width))

#Algorithm implementation
label = 1
dic = {}
for x in range(height):
    for y in range(width):
        value = threshold[x,y]
        if value == 0:
            left = matrix[x,y-1]
            top  = matrix[x-1,y]
            if left > 0 and top > 0:
                matrix[x,y] = min(left,top)
                if left != top:
                    dic.update([ ( max(left,top),min(left,top) ) ])
            elif left > 0:
                matrix[x,y] = left
            elif top > 0:
                matrix[x,y] = top
            else: 
                label = label+1
                matrix[x,y] = label
            
key = list(dic.keys())
val = list(dic.values())

for x in range(0,height):
    for y in range(0,width):
        values = matrix[x,y]
        for z in range(len(key)):
            if values == key[z]:
                matrix[x,y] = val[z]

plt.imshow(matrix,cmap="nipy_spectral")
plt.show()