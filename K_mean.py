import random
import math

# Calculate distance between points
def distance(point1, point2):
    dim = len(point1)
    dis = 0
    for i in range(dim):
        dis += (point1[i] - point2[i]) ** 2
    return math.sqrt(dis)

#calculate new centroid  by calculating "mean" point in cluster
def calculate_centroid(K, point_dic, dim):
    count = 0
    centroids = []
    for i in range(K):
        centroid = [0] * dim
        label_points = point_dic[i]
        for point in label_points:
            for i in range(dim):
                centroid[i] += point[i]
        for i in range(len(point)):
            centroid[i] /= len(label_points)
        centroids.append(centroid)
    return centroids

# Takes centroids, other points and create K clusters from N number of points.
def k_mean(N, K, points, centroids):
    past_labels = [0]
    current_labels = [1]
    # perform the algorithm until they converge(when all points do not change after the new centroid selected)
    while past_labels != current_labels:
        past_labels = current_labels.copy()
        labels = dict()
        point_dic = dict()
        #Create K number of cluster by a dictionary
        for i in range(K):
            point_dic[i] = []
        # We make another dic by key of point and value of K cluster labels
        for point in points:
            labels[point] = -1
        # determine the point's cluster by the distance to each centroid
        for point in points:
            min_dis = 1000000000000000
            min_idx = 0
            idx = 0
            for centroid in centroids:
                d = distance(point, centroid)
                if min_dis > d:
                    min_dis = d
                    min_idx = idx
                elif min_dis == d:
                    if idx < min_idx:
                        min_dis = d
                        min_idx = idx
                idx += 1
            labels[point] = min_idx
            point_dic[min_idx].append(point)
        current_labels.clear()
        for point in points:
            current_labels.append(labels[point])
        centroids = calculate_centroid(K, point_dic, len(points[0]))
    return labels


if __name__ == "__main__":
    info = input()
    N, K = info.split()
    N = int(N)
    K = int(K)
    point = input()
    points = []
    while point != "":
        temp = tuple(float(x) for x in point.split())
        points.append(temp)
        try:
            point = input()
        except:
            break;
    #initial centroids
    initals = points[N:]
    #All points
    points = points[:N]
    k_mean_result = k_mean(N, K, points, initals)
    for key in k_mean_result.keys():
        print(k_mean_result[key])












