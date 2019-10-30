import random
import math


def distance(point1, point2):
    dim = len(point1)
    dis = 0
    for i in range(dim):
        dis += (point1[i] - point2[i]) ** 2
    return math.sqrt(dis)


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


def k_mean(N, K, points, centroids):
    past_labels = [0]
    current_labels = [1]
    while past_labels != current_labels:
        past_labels = current_labels.copy()
        labels = dict()
        point_dic = dict()
        for i in range(K):
            point_dic[i] = []
        for point in points:
            labels[point] = -1
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
    initals = points[N:]
    points = points[:N]
    k_mean_result = k_mean(N, K, points, initals)
    for key in k_mean_result.keys():
        print(k_mean_result[key])












