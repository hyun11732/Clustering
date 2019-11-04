# K_MEAN

K-mean is one of basic clustering algorithm. Its algorithm is very simple. 
First, randomly select K points, called centroids, from the data and compute K-cluster by assigning each point to closest centroid.
Then, compute a new centroid with a mean point of a cluster.
Repeat this process until it converges. 

There are various versions in K-Mean algorithm like K-Median, K-Mode.
These algorithms just change a decision making of choosing a new centroid from mean to others. 
They may peform better or not. It depends on the dataset.

However, we should know about K-mean++ and k-Medoids. 
K-mean ++ selectes the point that is farthest from the current centroids.
K-Medoids selects the point with a raondom process by comparing with the current centroids.
They both converge much faster than K-Mean algorithms.
