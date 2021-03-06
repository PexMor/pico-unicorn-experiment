#!/usr/bin/env python3

from PIL import Image, ImageEnhance
import numpy

size =  16, 7
im = Image.open("img/ceye.jpg")

width, height = im.size
new_width = 16*15
new_height = 7*15
left = (width - new_width)/2
top = (height - new_height)/2 - 30
right = (width + new_width)/2
bottom = (height + new_height)/2 - 30

# Crop the center of the image
im2 = im.crop((left, top, right, bottom))
enhancer = ImageEnhance.Brightness(im2)
factor = 1.5
im3 = enhancer.enhance(factor)

im3.thumbnail(size, Image.ANTIALIAS)
im3.save("save.jpg", "JPEG")
np_im = numpy.array(im3)
print(np_im.shape)
amax, bmax, rgb = np_im.shape
buf = bytearray()
html = "<html><head><title>ColorMatrix</title></head><body><table>"
for a in range(amax):
    html += "<tr>"
    for b in range(bmax):
        hex_rgb = "%02x%02x%02x" % (np_im[a][b][0],np_im[a][b][1],np_im[a][b][2])
        html += "<td style='background-color:#"+hex_rgb+"'>@</td>"
        for c in range(rgb):
            #if a<4 and b<4 and c == 0:
            #    val = 255
            #else:
            #    val = 0
            val = np_im[a][b][c]
            buf.append(val)
            # buf.append(np_im[a][b][c])
    html += "</tr>";
html += "</body></html>"
with open("save.html", "w") as tf:
    tf.write(html)
print(buf)
