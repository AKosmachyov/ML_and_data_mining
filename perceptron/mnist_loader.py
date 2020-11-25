import numpy as np

from sklearn.datasets import fetch_openml


def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth position and
    zeroes elsewhere. This is used to convert a digit (0...9) into a
    corresponding desired output from the neural network."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


def load_data():
    """Return the MNIST data as a tuple containing the training data and the test
    data. (list(x.shape(784, 1)), list(y.shape(10, 1)))"""

    # Load data from https://www.openml.org/d/554
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True)
    X = X / 255

    data = [(image.reshape((784, 1)), vectorized_result(int(label)))
            for image, label in zip(X, y)]

    train_size = 60000
    test_size = 50

    train, test = data[:train_size], data[-test_size:]
    
    return (train, test)
