import numpy as np
from PIL import Image

width, height = 600, 800

img = np.zeros((height, width, 3), dtype = np.uint8)

img[:] = (35, 29, 43) #background/sky

img[int(height*0.85):height, 0:width] = (35, 55, 43) #grass

img[int(height*0.1):int(height*0.9),  #Building
    int(width*0.2):int(width*0.8) ] = (94, 101, 107)

for row in range(6):
    for column in range(5):
        if np.random.randint(0,8) == 5:
            window_colour = (240, 230, 140)
        else:
            window_colour = (28,28,35)
        img[
            int(height*0.1 + 100*row + 20): int(height*0.1 + 100*row  + 60 + 20),
            int(width*0.2 + 75*column  + 15): int(width*0.2 + 75*column  + 30 + 15)
            ] = window_colour

location = 0
shade = 0
n_shades = 255

# for i in range(n_shades):
#     img[0:height, location:location+width//n_shades, 0] = shade
#     location += width//n_shades
#     shade += 255//n_shades

#Create blank image
Image.fromarray(img).save("my_image2.png")



