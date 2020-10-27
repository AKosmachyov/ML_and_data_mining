import numpy as np
from sklearn.datasets import make_blobs

from maximin import Maximin

n_samples = 9

# X, y = make_blobs(n_samples=n_samples, centers=4,
#                   cluster_std=0.7, random_state=1)


arr = np.array([
    [0.96, 0.57],
    [1, 0.57],
    [0.81, 0.71],
    [0.77, 0.14],
    [0.69, 0.43],
    [0.98, 0.57],
    [0.61, 0.29],
    [0.89, 1],
    [0.91, 0.57]
])

maximin = Maximin()
maximin.fit(arr)