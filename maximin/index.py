import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

from maximin import Maximin

n_samples = 1000

X, y = make_blobs(n_samples=n_samples, centers=4,
                  cluster_std=0.8, random_state=10)

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