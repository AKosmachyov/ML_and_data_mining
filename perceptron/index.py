import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.datasets import fetch_openml

from multi_layer_perceptron import MultiLayerPerceptron

# Load data from https://www.openml.org/d/554
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
X = X / 255

for n in range(y.shape[0]):
    valid_class = int(y[n])
    y[n] = np.zeros([10, 1])
    y[n][valid_class][0] = 1

train_size = 60000
test_size = 50

X_train, X_test = X[:train_size], X[-test_size:]
y_train, y_test = y[:train_size], y[-test_size:]

train = [(image.reshape((784, 1)), label) for image, label in zip(X_train, y_train)]
test = [(image.reshape((784, 1)), label) for image, label in zip(X_test, y_test)]

net = MultiLayerPerceptron([784, 30, 10])
net.SGD(train, 30, 10, 3, test_data=test)

plt.figure(figsize=(10, 5))
for i in range(10):
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(X[i].reshape(28, 28), cmap=plt.cm.gray)
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    l1_plot.set_xlabel('Class %s' % y[i])

plt.show()