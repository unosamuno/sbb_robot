import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import glob


img_list, lbl_list = glob.glob("/home/samuel/data/Videos/detection_video3/*.png"), glob.glob("/home/samuel/data/Videos/detection_video3/*.txt")
img_list.sort()
lbl_list.sort()
print(lbl_list)

for idx in range(len(img_list)):

    img = cv.imread(img_list[idx])
    lbl = pd.read_csv(lbl_list[idx], header=None, index_col=None, sep=" ")
    w, h = img.shape[1], img.shape[0]

    for jdx in range(len(lbl)):
        x_c, y_c, w_c, h_c = lbl.loc[jdx][1], lbl.loc[jdx][2], lbl.loc[jdx][3], lbl.loc[jdx][4]
        w_r, h_r = w_c*w, h_c*h
        x_r, y_r = x_c*w-w_r/2, y_c*h-h_r/2
        start_point = (int(x_r), int(y_r))
        end_point = (int(x_r+w_r), int(y_r+h_r))
        pic = cv.rectangle(img, start_point, end_point, (0, 0, 255), 2)
    name = "pic" + str(idx)
    #cv.imshow(name, pic)
    cv.imwrite(name, pic)

"""
    for kdx in range(len(lbl_list[idx])):
        name = "pic" + str(kdx)
        cv.imwrite(name, img_list[kdx])
"""