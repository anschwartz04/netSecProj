# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 13:38:55 2021

@author: ansch
"""

from image_slicer import slice
from PIL import Image

#path = "C://Users/ansch/Desktop/Nova/ECE/GitRepo/netSecProj/"
slices = slice('sunflower.jpg', 8)
photoBreak = []
for row in range(1,2):
    for col in range(1,4):
        # print("row",row,"col",col)
        photoBreak.append("sunflower_0"+str(row)+"_0"+str(col)+".png")
for index in photoBreak:
    img = Image.open(index)
    img.show()
    

# import cv2
# import math

# img = path+"stock_flowers.jpg" # 512x512

# img_shape = img.shape
# tile_size = (256, 256)
# offset = (256, 256)

# for i in xrange(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
#     for j in xrange(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
#         cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]
#         # Debugging the tiles
#         cv2.imwrite("debug_" + str(i) + "_" + str(j) + ".png", cropped_img)