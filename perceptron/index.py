import numpy as np
import matplotlib.pyplot as plt
import random

import mnist_loader
from multi_layer_perceptron import MultiLayerPerceptron

train, y_test = mnist_loader.load_data()

net = MultiLayerPerceptron([784, 30, 10])
net.SGD(train, 30, 10, 3.0, test_data=y_test)

plt.figure(figsize=(10, 5))
for i in range(10):
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(train[0][i].reshape(28, 28), cmap=plt.cm.gray)
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    l1_plot.set_xlabel('Class %s' % train[1][i])

plt.show()
