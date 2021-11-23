import cv2 as cv
import glob
import os


path_list = glob.glob("/home/samuel/data/evaluation3_gray/valid/*.jpg")
path_list.sort()

nof_img = len(path_list)

img = cv.imread(path_list[0])
img_name = path_list[0]
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(0, nof_img):
    cv.imwrite(path_list[i], gray)

