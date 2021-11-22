import cv2 as cv
import glob
import os


path_list = glob.glob(("/home/samuel/data/evaluation3_gray/train/*.jpg"))
path_list.sort()

nof_img = len(path_list)

img = cv.imread(path_list[0])
img_name = path_list[0]
print(img_name)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite(path_list[0], gray)

