import numpy as np
import matplotlib.pyplot as plt
import random
import os,sys,inspect

from multi_layer_perceptron import MultiLayerPerceptron, load

import mnist_loader

random.seed(1)

train, test = mnist_loader.load_data()
validation = test[-1000:]

net = MultiLayerPerceptron([784, 30, 10])
net.SGD(train, 75, 10, 0.5)
net.save("digit_net.json")

# net = load("digit_net.json")
valid_count = net.evaluate(validation)
validation_size = len(validation)
percent = valid_count / len(validation) * 100
print("accuracy: {0}, size: {1}".format(percent, validation_size))

plt.figure(figsize=(10, 5))

data_visualization = test[: 10]
for i in range(len(data_visualization)):
    x, y = data_visualization[i][0], data_visualization[i][1]
    y_label = np.argmax(y)
    predicted_y = net.feedforward(x)
    predicted_label_y = np.argmax(predicted_y)
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(x.reshape(28, 28), cmap=plt.cm.gray)
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    text = "Class y: {0},\npredicted: {1}".format(y_label, predicted_label_y)
    l1_plot.set_xlabel(text)

plt.show()
