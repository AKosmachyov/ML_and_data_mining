import math
import numpy as np

class Maximin:

    k = 0
    cluster_centers = np.empty([0, 0])

    #  X: matrix of (n_samples, n_features). Training instances to cluster.
    def fit(self, X):
        # reset
        self.k = 0
        self.cluster_centers = np.empty([0, 0])

        # TODO add normalization in the future
        X_scaled = X

        n_samples = X_scaled.shape[0]
        # indexes of the sample from training data, which is the center of clusters
        sample_index_as_cluster_center = []
        # indexes of the cluster for each sample
        cluster_labels_for_samples = [0] * X_scaled.shape[0]
        # np.array with shape(n_samples, n_cluster)
        distance_to_each_cluster = np.empty([0, 0])

        max_valid_distance = 0
        new_cluster_indexes = []

        # use first sample as first cluster
        new_cluster_indexes.append(0)

        while len(new_cluster_indexes) > 0:

            distance_to_samples = np.empty(
                [n_samples, len(new_cluster_indexes)])

            for i_sample in range(0, n_samples):
                sample = X[i_sample]

                for j in range(len(new_cluster_indexes)):
                    cluster_index = new_cluster_indexes[j]
                    cluster = X[cluster_index]
                    distance_to_samples[i_sample][j] = euclidean_distances(
                        cluster, sample)

            self.k += len(new_cluster_indexes)
            sample_index_as_cluster_center = sample_index_as_cluster_center + new_cluster_indexes
            new_cluster_indexes = []

            # Merge old distances with new calculated distances
            if distance_to_each_cluster.shape[0] == 0:
                # for first iteration it will be single cluster
                distance_to_each_cluster = distance_to_samples
            else:
                distance_to_each_cluster = np.concatenate(
                    (distance_to_each_cluster, distance_to_samples), axis=1)

            # find cluster label for each sample
            for i in range(len(distance_to_each_cluster)):
                row = distance_to_each_cluster[i]
                cluster_index = row.argmin()
                cluster_labels_for_samples[i] = cluster_index

            # find farthest index of sample and distance for each cluster
            farthest_sample_from_cluster = {}
            for i in range(len(cluster_labels_for_samples)):
                cluster_index = cluster_labels_for_samples[i]
                distance = distance_to_each_cluster[i][cluster_index]

                if cluster_index in farthest_sample_from_cluster:
                    old_distance = farthest_sample_from_cluster[cluster_index][1]

                    if distance > old_distance:
                        farthest_sample_from_cluster[cluster_index] = (
                            i, distance)
                else:
                    farthest_sample_from_cluster[cluster_index] = (i, distance)

            # check is samples located in valid range
            for key in farthest_sample_from_cluster:
                distance = farthest_sample_from_cluster[key][1]
                sample_index = farthest_sample_from_cluster[key][0]

                if distance > max_valid_distance:
                    new_cluster_indexes.append(sample_index)

            # calculate new range
            if len(new_cluster_indexes) > 0:
                indexes = sample_index_as_cluster_center + new_cluster_indexes
                max_valid_distance = get_new_valid_distance(X, indexes)

        clusters = list(
            map(lambda index: X[index], sample_index_as_cluster_center))
        self.cluster_centers = np.array(clusters)

    def predict(self, X):
        # TODO add normalization in the future
        X_scaled = X
        n_samples = X_scaled.shape[0]
        distance_to_clusters = np.empty([n_samples, len(self.cluster_centers)])

        for i_sample in range(0, n_samples):
            sample = X[i_sample]

            for j in range(len(self.cluster_centers)):
                cluster = self.cluster_centers[j]
                distance_to_clusters[i_sample][j] = euclidean_distances(
                    cluster, sample)

        result = [-1] * n_samples

        # find cluster label for each sample
        for i in range(len(distance_to_clusters)):
            row = distance_to_clusters[i]
            cluster_index = row.argmin()
            result[i] = cluster_index

        return result

def euclidean_distances(pointA, pointB):
    x = math.pow(pointA[0] - pointB[0], 2)
    y = math.pow(pointA[1] - pointB[1], 2)
    return math.sqrt(x + y)


def get_index_of_max_element(array):
    max_element = max(array)
    return array.index(max_element)


def get_new_valid_distance(samples, cluster_indexes):

    sum = 0
    count = 0
    size = len(cluster_indexes)

    for i in range(size - 1):
        for j in range(i + 1, size):
            cluster_a_index = cluster_indexes[i]
            cluster_b_index = cluster_indexes[j]
            sum += euclidean_distances(samples[cluster_a_index],
                                       samples[cluster_b_index])
            count += 1

    return sum / (count * 2)
