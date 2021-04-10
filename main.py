from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 

image = Image.open('sunflower.jpg')
plt.imshow(image)
print(image.size)
print(image.format)
print(image.mode)
plt.show()