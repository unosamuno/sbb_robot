#HSLU Project for SBB - RoVeKo3

#####For autonomous navigation a neural network yolov3 from [AlexeyAB](https://github.com/AlexeyAB/darknet) is used for training validation and testing.
#####A gaming computer was used and followed by this [manual](https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects).
![Image](pictures/deepbrain_detection.png)

##Procedure
###Data
####Image sets were counted, sorted and merged with a [python script](./count_sort.py).
####For training, validation and testing another [python script](./darknet_scripts/create_txt.py) was used to make a list of all images to feed the computer.

###Labeling
####For Labeling [VoTT](https://github.com/microsoft/VoTT) was used. Training and Testing was divided into two projects.
####This created a `.json` Document with all the bounding boxes for each image. But for the neural network of AlexeyAB `.txt` files for the bounding boxes and `.jpg` images were needed to feed into the network.
####To transform and export the datasets into YOLO Darknet, [roboflow](https://roboflow.com/) was used. Additionally, for renaming and reformating the images another [python script](./darknet_scripts/rename.py) was implemented.

###Training and Validation
####After training with 200 labeled training images and 100 labeled validation images with the pre-trained weights-file (yolov4.conv.137), a chart and new weights were the output.
![chart](./pictures/chart1.png)

###Testing
####A video was fed into the network to see if and how objects are detected.
####



