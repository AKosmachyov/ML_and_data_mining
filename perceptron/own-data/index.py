import os
import sys
import inspect
import numpy as np

# code for import multi_layer_perceptron from parent folder
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from prepare_img import imageprepare
from multi_layer_perceptron import MultiLayerPerceptron, load
from mnist_loader import vectorized_result

x1 = np.array(imageprepare('own-data/5.png')).reshape((784, 1))
X = [x1]

net = load("digit_net.json")
result = net.predict(X)
print(result)