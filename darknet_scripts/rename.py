import glob
import pandas as pd
import cv2 as cv

img_list, txt_list = glob.glob("*.jpg"), glob.glob("*.txt")
img_list = glob.glob("/home/samuel/data/sbb_initial/train/ds_roboflow/train/*.png")
txt_list = glob.glob("/home/samuel/data/sbb_initial/train/ds_roboflow/train/*.txt")
img_list.sort()
txt_list.sort()

print(len(img_list))
print(len(txt_list))
i = 0

for idx in range(len(img_list)):
    img = cv.imread(img_list[idx])
    new_name = "img_"
    if i<10:
        new_name += "00" + str(i) 
    elif i<100:
        new_name += "0" + str(i) 
    else:
        new_name += str(i) 
    cv.imwrite(new_name+".jpg", img)
    
    data = pd.read_csv(txt_list[idx], header=None, index_col=None, sep=" ")
    data.to_csv(new_name+".txt", sep=" ", index=False, header=False)
    i += 1
    
