import numpy as np
import math


class Maximin:

    k = 0
    cluster_centers_ = []

    def fit(self, X):
        n_samples = X.shape[0]
        # indexes of the sample from training data, which is the center of clusters
        sample_index_as_cluster_center = []
        # indexes of the cluster for each sample
        cluster_labels_for_samples = [0] * X.shape[0]
        # np.array with shape(n_samples, n_cluster)
        distance_to_each_cluster = np.empty([0, 0])

        max_valid_distance = 0
        new_cluster_indexes = []

        # use first sample as first cluster
        new_cluster_indexes.append(0)

        while len(new_cluster_indexes) > 0:

            # append_new_cluster_index(0, sample_index_as_cluster_center)

            distance_to_sample = np.zeros(
                (n_samples, len(new_cluster_indexes)))
            for iSample in X:
                row = X[iSample]

                for jCluster in new_cluster_indexes:
                    cluster = X[jCluster]
                    distance_to_sample[iSample][jCluster] = euclidean_distances(
                        cluster, iSample)

            # Merge old distances with new calculated distances
            if distance_to_each_cluster.shape[0] == 0:
                # for first iteration it will be single cluster
                distance_to_each_cluster = distance_to_sample[0].reshape(
                    n_samples, 1)
            else:
                for distance_array in distance_to_sample:
                    transposed = distance_array.reshape(n_samples, 1)
                    distance_to_each_cluster = np.concatenate(
                        (distance_to_each_cluster, transposed), axis=1)

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
                max_valid_distance = get_new_valid_distance(
                    X, sample_index_as_cluster_center)

    def append_new_cluster_index(self, cluster_index, array):
        array.append(cluster_index)
        self.k += 1


def euclidean_distances(pointA, pointB):
    x = math.pow(pointA[0] - pointB[0], 2)
    y = math.pow(pointA[1] - pointB[1], 2)
    return math.sqrt(x + y)


def get_index_of_max_element(array):
    max_element = max(array)
    return array.index(max_element)


def get_new_valid_distance(samples, cluster_indexes, new_cluster_indexes):
    # A-B / 2 

    # A-B + A-C + B-C / (3 * 2) 

    # A-B + A-C + A-D + B-C + B-D + C-D / (6 * 2) 

    # max_valid_distance = max_distance / 2
    return 0
