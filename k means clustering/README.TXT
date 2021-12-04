

For the calculation of k-means clustering, the following actions were taken:
1) Take four arbitrary points from the file as initial centroids. The arbitrary points are provided.
2) Loop an iteration fifty times to ensure the points are placed to the nearest centroid.
3) Create a subloop to iterate through the N (x,y) values or points so that each point is compared to the centroids.
4) Calculate the distance between each of the (x,y) centroids and the (x,y) points to determine the shortest distance. 
The Pythagorean equation is used to calculate the distance.
5) Calculate the x-mean and y-mean to replace the initial centroids and re-evaluate the shortest
distance between the centroids and the points.
6) Points with the shortest distance to the centroids are then grouped.
