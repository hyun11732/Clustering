# K_MEAN

K-mean is one of basic clustering algorithm. Its algorithm is very simple.

It is top-down algorithm.  

First, randomly select K points, called centroids, from the data and compute K-cluster by assigning each point to closest centroid. Then, compute a new centroid with a mean point of a cluster. Repeat this process until it converges.

![equation](https://github.com/hyun11732/K_MEAN/blob/master/image/k-Mean.JPG)

There are various versions in K-Mean algorithm like K-Median, K-Mode. These algorithms just change a decision making of choosing a new centroid from mean to others. They may perform better or not. It depends on the dataset.

However, we should know about K-mean++ and k-Medoids. K-mean ++ selects the point that is farthest from the current centroids. K-Medoids selects the point with a raondom process by comparing with the current centroids. They both converge much faster than K-Mean algorithms.






# Agglomerative Clustering Algorithm(AGNES)

While K-Mean is a top-down clustering,  AGNES is bottom-up algorithm. It started from the single point and merge to a bigger cluster.
There are some concept we need to know before we learn about AGNES: "Link". "Link" is the function which determines a cluster. For example, single Link
is the shortest distance between two cluster and complete link is the farthest distance. By using selecting another point which has a smallest link,
the points are merged into a single cluster. This is repeated until we have K number of cluster. There are bunch of link we can use and they all perform differently.



##Appendex

Saurabh Sinha. "CS 412 Intro. to Data Mining Chapter 10. Cluster Analysis". 13pg, PPT
