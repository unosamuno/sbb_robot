import glob
import json

img_list = glob.glob("/home/tbhuser/data/train*.jpg")
img_list.sort()

with open("train.txt", 'w') as f:
    for item in img_list:
        f.write("%s\n" % item)

