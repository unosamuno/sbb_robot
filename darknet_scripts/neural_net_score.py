import glob
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

data = pd.read_csv("/home/samuel/sbb_robot/results_color.csv", header=None)

pylon_scores = []
human_scores = []
train_scores = []

for i in range(0, len(data)):
    name = data[0][i]
    if name == "pylon":
        p = int(data[1][i])
        pylon_scores.append(p)
    elif name == "human":
        h = int(data[1][i])
        human_scores.append(h)
    elif name == "train":
        t = int(data[1][i])
        train_scores.append(t)
    else:
        pass

pylon_avg_score = int(np.mean(pylon_scores))
human_avg_score = int(np.mean(human_scores))
train_avg_score = int(np.mean(train_scores))

plt.hist(pylon_scores, label='pylon scores color', color='blue')
plt.ylabel("Frame Count")
plt.xlabel("Score")
plt.text(30, 350, s="Average Score: "+ str(pylon_avg_score))
plt.legend()
plt.show()

plt.hist(human_scores, label='human scores color', color='orange')
plt.ylabel("Frame Count")
plt.xlabel("Score")
plt.text(30, 200, s="Average Score: "+ str(human_avg_score))
plt.legend()
plt.show()


plt.hist(train_scores, label='train scores color', color='green')
plt.ylabel("Frame Count")
plt.xlabel("Score")
plt.text(40, 3, s="Average Score: "+ str(train_avg_score))
plt.legend()
plt.show()

plt.hist(pylon_scores, label='pylon scores color')
plt.hist(human_scores, label='human scores color')
plt.hist(train_scores, label='train scores color')
plt.ylabel("Frame Count")
plt.xlabel("Score")
plt.legend()
plt.show()
