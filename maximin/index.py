import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

from maximin import Maximin

n_samples = 9

# X, y = make_blobs(n_samples=n_samples, centers=4,
#                   cluster_std=0.7, random_state=1)


X = np.array([
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

plt.subplot(3, 3, 1)

plt.scatter(X[:, 0], X[:, 1])
plt.title("Initial")

maximin = Maximin()
maximin.fit(X)
y_maximin = maximin.predict(X)

plt.subplot(3, 3, 2)
# cmap - color theme, c - colors
plt.scatter(X[:, 0], X[:, 1], c=y_maximin, cmap='viridis')
plt.title("Clusters")

centers = maximin.cluster_centers
plt.subplot(3, 3, 3)
plt.scatter(centers[:, 0], centers[:, 1], c='black')
plt.title("Center")

plt.show()