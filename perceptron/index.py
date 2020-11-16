import numpy as np
import matplotlib.pyplot as plt
import random

from multi_layer_perceptron import MultiLayerPerceptron
from sklearn.datasets import load_iris

iris_data = load_iris()

iris_dataset = np.column_stack(
    (iris_data.data, iris_data.target.T))  # Join X and Y

iris_dataset = list(iris_dataset)
random.shuffle(iris_dataset)

train_percent = 80
size = len(iris_dataset)
train_size = size * train_percent

train = iris_dataset[:train_size]
test = iris_dataset[train_size:]

train_x = np.array([i[:4] for i in train])
train_y = np.array([i[4] for i in test])
test_x = np.array([i[:4] for i in train])
test_y = np.array([i[4] for i in test])

dictionary = {
    'inputLayer': 4,
    'hiddenLayer': 5,
    'numberOfClasses': 3,
    'learningRate': 0.005,
    'maxEpochs': 700,
}

perceptron = MultiLayerPerceptron(dictionary)
perceptron.fit(train_x, train_y)
