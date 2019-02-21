from PIL import Image

#Convert Image to binary
img = Image.open('Lab4-image.png')
img = img.convert('L').point((lambda x : 255 if x > 128 else 0), mode = '1')
#Uncomment to show binarized image in output
#img.show()

#Getting dimensions of image
(width, height) = img.size
#Making a matrix of same dimensions
matrix = [[0 for x in range(width)] for y in range(height)]
#Populating matrix
for x in range(width):
    for y in range(height):
        value = img.getpixel((x, y))    #getting pixel value at every point
        if value > 0:
            matrix[y][x] = 1
        else:
            matrix[y][x] = 0
