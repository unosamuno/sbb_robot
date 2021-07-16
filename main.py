import numpy as np
import os
from typing import List

# name all color images as string values
test1_imgs: str = '/home/samuel/data/sbb_initial/test1_imgs/color'
test2_imgs: str = '/home/samuel/data/sbb_initial/test2_imgs/color'
test3_imgs: str = '/home/samuel/data/sbb_initial/test3_imgs/color'
test4_imgs: str = '/home/samuel/data/sbb_initial/test4_imgs/color'

nrof_imgs1: List[str] = len(os.listdir(test1_imgs)) #704
nrof_imgs2: List[str] = len(os.listdir(test2_imgs)) #351
nrof_imgs3: List[str] = len(os.listdir(test3_imgs)) #938
nrof_imgs4: List[str] = len(os.listdir(test4_imgs)) #1605
nrof_imgs_tot = nrof_imgs4+nrof_imgs3+nrof_imgs1+nrof_imgs2 #3598

print(nrof_imgs_tot)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


