import os
import sys
import inspect
import numpy as np
import random

random.seed(10)

# code for import multi_layer_perceptron from parent folder
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from prepare_img import imageprepare
from multi_layer_perceptron import MultiLayerPerceptron, load
from mnist_loader import vectorized_result

train_for_symbol = "K"

def getY(fileName):
    isK = fileName.startswith(train_for_symbol)
    return vectorized_result(0, 2) if isK else vectorized_result(1, 2)

def load_test():
    directoryPath = "{}/test_{}/".format(current_dir, train_for_symbol)
    files = os.listdir(directoryPath)
    files = list(filter(lambda x: x.endswith(".png"), files))
    dataset_size = len(files)
    test_data = []

    for i in range(dataset_size):
        fileName = files[i]
        y = getY(fileName)
        x = np.array(imageprepare(directoryPath + fileName)).reshape((784, 1))
        test_data.append((x,y))
    
    return test_data

# Variables
directoryPath = "{}/train_{}/".format(current_dir, train_for_symbol)

files = os.listdir(directoryPath)
files = list(filter(lambda x: x.endswith(".png"), files))
dataset = []
dataset_size = len(files)

for i in range(dataset_size):
    fileName = files[i]
    y = getY(fileName)
    x = np.array(imageprepare(directoryPath + fileName)).reshape((784, 1))
    row = (x, y)
    dataset.append(row)

random.shuffle(dataset)

test = load_test()
train = dataset
print("Train size", len(train), "Validation size", len(test))

net = MultiLayerPerceptron([784, 64, 2])
net.SGD(train, 12, 10, 1.5, test_data=test)
net.save("own_{}_data_net.json".format(train_for_symbol))
