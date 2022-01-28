
from PIL import Image
from numpy import asarray
import sys

# load the image
image = Image.open(sys.argv[1])
new_image = image.resize((150, 50))
data = asarray(new_image)
print(type(data))
print(data.shape)
image2 = Image.fromarray(data)
print(type(image2))
print(image2.mode)
print(image2.size)

for i in data:
        for j in i:
            if j > 0:
                print('x', end="")
            else:
                print(' ', end="")
        print()
