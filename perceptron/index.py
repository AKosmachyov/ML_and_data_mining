import numpy as np
import matplotlib.pyplot as plt
import random

from multi_layer_perceptron import MultiLayerPerceptron
from sklearn.datasets import load_iris

iris_data = load_iris()

random.seed(123)

def separate_data():
    A = iris_dataset[0:40]
    tA = iris_dataset[40:50]
    B = iris_dataset[50:90]
    tB = iris_dataset[90:100]
    C = iris_dataset[100:140]
    tC = iris_dataset[140:150]
    train = np.concatenate((A, B, C))
    test = np.concatenate((tA, tB, tC))
    return train, test

iris_dataset = np.column_stack(
    (iris_data.data, iris_data.target.T))  # Join X and Y
iris_dataset = list(iris_dataset)

train, test = separate_data()

train_x = np.array([i[:4] for i in train])
train_y = np.array([i[4] for i in train])
test_x = np.array([i[:4] for i in test])
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
perceptron.predict(test_x, test_y)
