from PIL import Image, ImageFilter
import os

image = Image.open('pup1.jpg')
# image.show()
image.thumbnail((300, 300))
image.rotate(90).save('pup1_mod.jpg')
image.convert(mode='L').save('pup1_mod.jpg')
image.filter(ImageFilter.GaussianBlur()).save('pup1_mod.jpg')
image.save('pup4.png')
