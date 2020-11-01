from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import numpy as np

n = input("Enter matrix size: ") 
size = int(n)
X = np.random.rand(size,size)

# single-linkage clustering (min)
Z = linkage(X, 'single')
plt.subplot(1, 2, 1)
plt.title("Single-linkage clusterting")
dn = dendrogram(Z)

# complete-linkage clustering (max)
Z = linkage(X, 'complete')
plt.subplot(1, 2, 2)
plt.title("Complete-linkage clusterting")
dn = dendrogram(Z)
plt.show()