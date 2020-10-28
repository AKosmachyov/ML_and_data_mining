import numpy as np
import math


class Maximin:

    k = 0
    cluster_centers_ = []

    def fit(self, X):
        cluster_center_indices = []
        labels_for_sampels = [0] * X.shape[0]

        self.k += 1
        cluster_center_indices.append(0)

        first_segment = X[0]

        distance_to_each_point = list(map(
            lambda point: euclidean_distances(first_segment, point), X))

        distances_to_segments = np.array(distance_to_each_point).reshape(9, 1)

        max_distance = max(distance_to_each_point)
        max_distance_index = distance_to_each_point.index(max_distance)

        # 3
        max_valid_distance = max_distance / 2

        self.k += 1
        cluster_center_indices.append(max_distance_index)

        cluster_center_indices.append(max_distance_index)
        second_segment = X[max_distance_index]

        distance_to_each_point_second = list(map(
            lambda point: euclidean_distances(second_segment, point), X))

        distances_to_segments = np.concatenate(
            (distances_to_segments, np.array(distance_to_each_point_second).reshape(9, 1)), axis=1)

        # find a label for each sample
        for i in range(len(distances_to_segments)):
            row = distances_to_segments[i]
            cluster_index = row.argmin()
            labels_for_sampels[i] = cluster_index

        # find max distance for cluster
        max_point_distance = {}
        for i in range(len(labels_for_sampels)):
            cluster_index = labels_for_sampels[i]
            distance = distances_to_segments[i][cluster_index]

            if cluster_index in max_point_distance:
                old_distance = max_point_distance[cluster_index][1]

                if distance > old_distance:
                    max_point_distance[cluster_index] = (i, distance)
            else:
                max_point_distance[cluster_index] = (i, distance)

        print(max_point_distance)

        for key in max_point_distance:
            distance = max_point_distance[key][1]
            sample_i = max_point_distance[key][0]
            if distance > max_valid_distance:
                cluster_center_indices.append(sample_i)

        # D(X1,X4)=0,47
        # D(X1,X8)=0,44,
        # D(X1,X5)=0,3,
        # D(X4,X8)=0,87,
        # D(X4,X5)=0,3,
        # D(X8,X5)=0,6.

        + + + / (6 * 2)

        X1, X4, X8, X5
        #

        # if maxValues > maxValidDistance {
        #     createSegment
        # } else {
        #     continue
        # }


def euclidean_distances(pointA, pointB):
    x = math.pow(pointA[0] - pointB[0], 2)
    y = math.pow(pointA[1] - pointB[1], 2)
    return math.sqrt(x + y)


def get_index_of_max_element(array):
    max_element = max(array)
    return array.index(max_element)
