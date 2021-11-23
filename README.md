# HSLU Project for SBB - S-Bot

For autonomous navigation a neural network yolov3 from [AlexeyAB](https://github.com/AlexeyAB/darknet) is used for training validation and testing.
A gaming computer was used and followed by this [manual](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
![Image](pictures/deepbrain_detection.png)

## Procedure
### Data
Image sets were counted, sorted and merged with a [python script](./count_sort.py).
For training, validation and testing another [python script](./darknet_scripts/create_txt.py) was used to make a list of all images to feed the computer.

### Labeling
For Labeling [VoTT](https://github.com/microsoft/VoTT) was used. Training and Testing was divided into two projects.
This created a `.json` Document with all the bounding boxes for each image. But for the neural network of AlexeyAB `.txt` files for the bounding boxes and `.jpg` images were needed to feed into the network.

To transform the data from VoTT JSON Format into YOLO file Format [vott2yolo](https://cnpmjs.org/package/vott2yolo) was used.

### Training
After training with 200 labeled training images with the pre-trained weights-file (yolov4.conv.137), a chart and new weights were the output.
![chart](./pictures/chart1.png)

Train with the following command: \
`./darknet detector train <path_to>/obj.data cfg/yolo-obj.cfg cfg/yolov4-tiny.conv.29 -map`

### Testing
A video was fed into the network to see if and how objects are detected.
To test the neural network type: \
`./darknet detector map <path_to_>/obj.data cfg/yolo-obj.cfg backup/yolo-obj_final.weights`
With this we get an output like: \

> class_id = 0, name = train, ap = 92.50%   	 (TP = 4, FP = 1)
> class_id = 1, name = human, ap = 87.68%   	 (TP = 212, FP = 30) 
> class_id = 2, name = pylon, ap = 74.89%   	 (TP = 608, FP = 176) 


### Validation
After Testing, a validation set with 100 labeled images were fed into the network. \
To feed multiple (validation) images into the network and get the output as a .txt file: \
`./darknet detector test /home/tbhuser/data/evaluation3_color/valid/obj.data cfg/yolo-obj.cfg backup/yolo-obj_best.weights -dont_show -ext_output < /home/tbhuser/data/evaluation3_color/train/train.txt > result.txt` \
The output then was analysed with another [python script](./darknet_scripts/neural_net_score.py). \

#### 



