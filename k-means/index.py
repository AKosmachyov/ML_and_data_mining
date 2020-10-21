# pip3 install -U scikit-learn
# pip3 install -U matplotlib

import matplotlib.pyplot as plt

n_samples = 1000
marker_size = 10

from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=n_samples, centers=4,
                  cluster_std=0.7, random_state=1)
plt.subplot(3, 3, 1)
plt.scatter(X[:, 0], X[:, 1], s=marker_size)
plt.title("Initial")

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4).fit(X)
y_kmeans = kmeans.predict(X)

plt.subplot(3, 3, 2)
# cmap - color theme, c - colors
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=marker_size, cmap='viridis')
plt.title("K means")

centers = kmeans.cluster_centers_
plt.subplot(3, 3, 3)
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=marker_size)
plt.title("K means center")

plt.show()