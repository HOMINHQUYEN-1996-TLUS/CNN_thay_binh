
import numpy as np
from PIL import Image
from pandas import array
image_r = []
image_g = []
image_b = []
sum_rgb = list()
im = Image.open('100.png')
pixels = list(im.getdata())
for i in pixels:
    image_r.append("{:.2f}".format(i[0]*0.299))
print(image_r)
print('###################')
for i in pixels:
    image_g.append("{:.2f}".format(i[1]*0.587))
print(image_g)
print('###################')
for i in pixels:
    image_b.append("{:.2f}".format(i[2]*0.114))
print(image_b)
print('###################')
for i in range(69*52):
    sum_rgb.append("{:.2f}".format(float(image_r[i])+float(image_g[i])+float(image_b[i])))
print('List anh xam : ',sum_rgb)

B = np.array(sum_rgb).reshape(69,52)
print('Ma tran anh xam =', B)

filter = np.array([[1,0,1],[0,1,0],[1,0,1]])

print('filter = ',filter)