import math


class cluster:

    def __init__(self, point, idx):
        self.id = idx
        self.points = [point]

    def merge(self, cluster):
        self.id = min(self.id, cluster.id)
        for point in cluster.points:
            self.points.append(point)

    def print_c(self):
        print(self.id, " : ", self.points)


def distance(point1, point2):
    dim = len(point1)
    dis = 0
    for i in range(dim):
        dis += (point1[i] - point2[i]) ** 2
    return math.sqrt(dis)


# Extract column from the 2-D list
def column(matrix, col):
    return [row[col] for row in matrix]


def distance_matrix(point_dic, id_dic):
    labels = list(point_dic.keys())
    points = list(id_dic.keys())
    distances = dict()
    idx1 = 0
    for label1 in labels:
        idx2 = 0
        distances[label1] = dict()
        for label2 in labels:
            distances[label1][label2] = distance(points[idx1], points[idx2])
            idx2 += 1
        idx1 += 1
    return (distances)


def find_cluster(clusters, idx):
    for cluster in clusters:
        if cluster.id == idx:
            return cluster


def remove_elem(d_matrix, removed, kept):
    temp_row = d_matrix[removed].copy()
    temp_col = dict()
    for key1 in list(d_matrix.keys()):
        temp_col[key1] = d_matrix[key1][removed]
    # remove merged row
    del d_matrix[removed]
    # remove merged col and update merging col
    for key in list(d_matrix.keys()):
        if key != removed:
            del d_matrix[key][removed]
            d_matrix[key][kept] = min(d_matrix[key][kept], temp_col[key])
    # update merging row
    for key in list(d_matrix[kept].keys()):
        d_matrix[kept][key] = min(d_matrix[kept][key], temp_row[key])
    return d_matrix


# id_dic point-> id
# point_dic id ->point
def AGNES(id_dic, point_dic, clusters, K):
    d_matrix = distance_matrix(point_dic, id_dic)
    while len(clusters) != K:
        min_dis = 1000000000000
        merge1 = 0
        merge2 = 0
        a = 0
        b = 1
        for i in list(d_matrix.keys()):
            for j in list(d_matrix[i].keys())[:b]:
                if i != j:
                    distance = d_matrix[i][j]
                    if distance < min_dis:
                        min_dis = distance
                        merge1 = i
                        merge2 = j
                    elif distance == min_dis:
                        print(i, j, distance, min_dis)
                        min1 = min(merge1, merge2)
                        min2 = min(i, j)
                        if min2 < min1:
                            min_dis = distance
                            merge1 = i
                            merge2 = j
                        elif min1 == min2:
                            max1 = max(merge1, merge2)
                            max2 = max(i, j)
                            if max2 <= max1:
                                min_dis = distance
                                merge1 = i
                                merge2 = j
            b += 1
        # print(merge1, merge2)
        removed = max(merge1, merge2)
        kept = min(merge1, merge2)
        clusters[kept].merge(clusters[removed])
        del clusters[removed]
        d_matrix = remove_elem(d_matrix, removed, kept)
    return clusters


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
    id_dic = dict()
    points = points[:N]
    idx = 0
    point_dic = dict()
    clusters = dict()
    for point in points:
        point_dic[idx] = point
        id_dic[point] = idx
        c = cluster(point, idx)
        clusters[idx] = c
        idx += 1
    clusters = AGNES(id_dic, point_dic, clusters, K)
    for point in points:
        for key in list(clusters.keys()):
            cluster = clusters[key]
            if point in cluster.points:
                print(key)