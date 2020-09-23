# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 23:25:07 2020
@author: yuehchuan
"""

import os
import getpass
from PIL import Image

USERNAME=getpass.getuser()

saveImgDirPath = '/home/'+USERNAME+'/kneron/data/pic/'
image_files = os.listdir(saveImgDirPath)
for idx, file in enumerate(image_files):
    filenamePNG = os.path.splitext(file)[1]
    if (filenamePNG == '.png'):
        print(file)
        ImgFile=saveImgDirPath+file
        im = Image.open(ImgFile)

        width, height = im.size

        # Setting the points for cropped image
        left = 70
        top = 70
        right = 293
        bottom = 293

        # Cropped image of above dimension
        im1 = im.crop((left, top, right, bottom))
        newsize = (224, 224)
        im1 = im1.resize(newsize)
        # Shows the image in image viewer
        im1.show()
        im1.save(ImgFile)

print ('Great!!! Now, everyone is happy! (◕ ‿ ◕ )!')
