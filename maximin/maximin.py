import numpy as np
import math

class Maximin:

    k = 0
    cluster_centers_ = []

    def fit(self, X):
        cluster_center_indices = []

        self.k += 1
        cluster_center_indices.append(0)

        first_segment = X[0]

        distance_to_each_point = list(map(
            lambda point: euclidean_distances(first_segment, point), X))

        distances_to_segments = np.array(distance_to_each_point).reshape(9,1)

        max_distance = max(distance_to_each_point)
        max_distance_index = distance_to_each_point.index(max_distance)

        max_valid_distance = max_distance / 2

        self.k += 1
        cluster_center_indices.append(max_distance_index)

        cluster_center_indices.append(max_distance_index)
        second_segment = X[max_distance_index]

        distance_to_each_point_second = list(map(
            lambda point: euclidean_distances(second_segment, point), X))

        distances_to_segments = np.concatenate(
            (distances_to_segments, np.array(distance_to_each_point_second).reshape(9,1)), axis=1)
        #
        # findSegment for distanceToEachPoint && distanceToEachPointSecond

        # find maxValues for each segment

        # if maxValues > maxValidDistance {
        #     createSegment
        # } else {
        #     continue
        # }


def euclidean_distances(pointA, pointB):
    x = math.pow(pointA[0] - pointB[0], 2)
    y = math.pow(pointA[1] - pointB[1], 2)
    return math.sqrt(x + y)
