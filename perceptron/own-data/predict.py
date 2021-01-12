import os
import sys
import inspect
import numpy as np
import random

# code for import multi_layer_perceptron from parent folder
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from prepare_img import imageprepare
from multi_layer_perceptron import MultiLayerPerceptron, load
from mnist_loader import vectorized_result

# Variables
predict_for_symbol = "K"
directoryPath = current_dir + "/test_{}/".format(predict_for_symbol)

files = os.listdir(directoryPath)
files = list(filter(lambda x: x.endswith(".png"), files))
dataset_size = len(files)
X = []
Y = []

for i in range(dataset_size):
    fileName = files[i]
    isK = fileName.startswith(predict_for_symbol)
    Y.append(0 if isK else 1)
    x = np.array(imageprepare(directoryPath + fileName)).reshape((784, 1))
    X.append(x)

net = load("own_{}_data_net.json".format(predict_for_symbol))
result = net.predict(X)
print("Result (real-predicted)")
for x, y, fileName in zip(result, Y, files):
    print(fileName, y, "-", x)


import matplotlib.pyplot as plt
data_visualization = list(zip(X, files))[: 10]
fig = plt.figure(figsize=(10, 5))
fig.suptitle("Is {} symbol?".format(predict_for_symbol))
for i in range(len(data_visualization)):
    x, fileName = data_visualization[i][0], data_visualization[i][1]
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(x.reshape(28, 28), cmap=plt.cm.gray)
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    text = "yes" if fileName.startswith(predict_for_symbol) else "no"
    l1_plot.set_xlabel(text)

plt.show()
