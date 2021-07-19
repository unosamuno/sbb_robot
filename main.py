import numpy as np
import os, shutil, glob
from typing import List

# name all color images as string values
test1_imgs: str = '/home/samuel/data/sbb_initial/test1_imgs/color'
test2_imgs: str = '/home/samuel/data/sbb_initial/test2_imgs/color'
test3_imgs: str = '/home/samuel/data/sbb_initial/test3_imgs/color'
test4_imgs: str = '/home/samuel/data/sbb_initial/test4_imgs/color'
test_imgs_merged: str = '/home/samuel/data/sbb_initial/test_imgs_merged'

#count images
nrof_imgs1: List[str] = len(os.listdir(test1_imgs)) #704
nrof_imgs2: List[str] = len(os.listdir(test2_imgs)) #351
nrof_imgs3: List[str] = len(os.listdir(test3_imgs)) #938
nrof_imgs4: List[str] = len(os.listdir(test4_imgs)) #1605
nrof_imgs_tot: List[str] = len(os.listdir(test_imgs_merged)) #3597
print(nrof_imgs_tot)

#rename colorized images in folder test_imgs_merged so that it's iterable
#only run once!
"""
path = '/home/samuel/data/sbb_initial/test_imgs_merged/'
i = 0
for filename in os.listdir(path):
    dst = str(i) + ".png"
    src = path + filename
    dst = path + dst
    os.rename(src, dst)
    i += 1
"""