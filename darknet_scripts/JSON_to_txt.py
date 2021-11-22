import json
import pandas as pd
with open("_annotations.coco.json") as f:
    data = json.load(f)
for img in data["images"]:
    h, w = img["height"], img["width"]
    id = img["id"]
    file_name = img["file_name"][:-3] + "txt"
    label, x_c_all, y_c_all, w_c_all, h_c_all = [], [], [], [], []
    for annot in data["annotations"]:
        if annot["image_id"] == id:
            x_r, y_r, w_r, h_r = annot["bbox"][0], annot["bbox"][1], annot["bbox"][2], annot["bbox"][3]
            x_c, y_c = (x_r+w_r/2)/w, (y_r+h_r/2)/h
            w_c, h_c = w_r/w, h_r/h
            x_c_all.append(x_c)
            y_c_all.append(y_c)
            w_c_all.append(w_c)
            h_c_all.append(h_c)
            label_temp = annot["category_id"]
            label.append(label_temp)
    temp_dict = {"label": label, "x_c": x_c_all,
                 "y_c": y_c_all, "w_c": w_c_all, "h_c": h_c_all}
    df = pd.DataFrame(temp_dict)
    df.to_csv(file_name, sep=' ', header=False, index=False)