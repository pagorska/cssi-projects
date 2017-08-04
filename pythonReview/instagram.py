from PIL import Image

corgo = Image.open("corgi.jpg")
print corgo.getdata()[200]

def getRed(pixel):
    return pixel[0]

def getGreen(pixel):
    return pixel[1]

def getBlue(pixel):
    return pixel[2]

def getAverage(pixel):
    pixelColor = pixel[0] + pixel[1] + pixel[2]
    return (pixelColor/3,pixelColor/3,pixelColor/3)

#
# for pixel in corgo.getdata():
#     #new_pixels.append(pixel)
#     red_value = pixel[0]
#     green_value = pixel[1]
#     blue_value = pixel[2]
#     #new_pixel = (0,green_value, blue_value)
#     new_pixel = (getAverage(pixel),getAverage(pixel),getAverage(pixel))
#     new_pixels.append(new_pixel)

def purple(image):
    new_pixels = []
    for pixel in image.getdata():
        new_pixel = (getGreen(pixel),getBlue(pixel),getRed(pixel))
        new_pixels.append(new_pixel)
    return new_pixels

def gray(image):
    new_pixels = []
    for pixel in corgo.getdata():
        new_pixel = (getAverage(pixel),getAverage(pixel),getAverage(pixel))
        new_pixels.append(new_pixel)
    return new_pixels

def cyan(image):
    new_pixels = []
    for pixel in image.getdata():
        new_pixel = (getBlue(pixel),getRed(pixel),getGreen(pixel))
        new_pixels.append(new_pixel)
    return new_pixels

def pink(image):
    new_pixels = []
    for pixel in image.getdata():
        new_pixel = (getRed(pixel),getBlue(pixel),getGreen(pixel))
        new_pixels.append(new_pixel)
    return new_pixels
#
# new_pixels = []
# size = corgo.height * corgo.width
# old_pixels = corgo.getdata()
# for i in range(size):
#     old_pixel = old_pixels[i]
#     if (i > size /2):
#         new_pixel = getAverage(old_pixel)
#     else:
#         new_pixel = old_pixel
#     new_pixels.append(new_pixel)


# new_pixels = []
# size = corgo.height * corgo.width
# old_pixels = corgo.getdata()
# for i in range(size):
#     old_pixel = old_pixels[i]
#     if (i > (size/3)*2):
#         new_pixel = (getGreen(old_pixel),getBlue(old_pixel),getRed(old_pixel))
#     elif (i > size/3):
#         new_pixel = getAverage(old_pixel)
#     else:
#         new_pixel = old_pixel
#     new_pixels.append(new_pixel)
new_pixels = []
size = corgo.height * corgo.width
colnum = 0
old_pixels = corgo.getdata()
for i in range(size):
    old_pixel = old_pixels[i]
    if (colnum > (corgo.width/3)*2):
        new_pixel = (getGreen(old_pixel),getBlue(old_pixel),getRed(old_pixel))
    elif (colnum > corgo.width/3):
        new_pixel = getAverage(old_pixel)
    else:
        new_pixel = old_pixel
    new_pixels.append(new_pixel)
    colnum += 1
    if (colnum == corgo.width):
        colnum = 0
print new_pixels[200]

new_image = Image.new("RGB", corgo.size)
new_image.putdata(new_pixels)
new_image.show()

new_image = Image.new("RGB", (corgo.width,corgo.height*2))
#new_image = Image.new("RGB", corgo.size)
new_image.putdata(pink(corgo))
offset = (0, corgo.height)
new_image.paste(corgo, offset)
new_image.show()
