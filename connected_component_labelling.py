from PIL import Image

#Convert Image to binary
img = Image.open('Lab4-image.png')
img = img.convert('L').point((lambda x : 255 if x > 128 else 0), mode = '1')
img.show()