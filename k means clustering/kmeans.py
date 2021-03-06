"""
Created on Fri Feb 26, 2021
@author: Ashish Singh

"""
import math

print()     # Empty line 

# ------------------------------------------------------------------
# Stores the absolute path of the file.
# ------------------------------------------------------------------
abs_filepath = input('Please enter file path without quotes ("") : ')
print()     # Empty line.

"""
Commenting out the absolute path used for testing purposes.
abs_filepath = "/Users/ashishsingh/Documents/Documents - Ashish’s MacBook Pro" \
               "/2021 Spring/Intro to Programming Using Python/Module 5/Assignment" \
               "/kmeans.txt"
"""
# ------------------------------------------------------------------
# Checks to see if the file is available and correct in the 
# location provided, if not, throws an error message to the user.
# ------------------------------------------------------------------
try:
    file_name = open(abs_filepath, "r")
except FileNotFoundError:
    print("Please correct the file path")

# Reads the entire content of the file into a list.
file = file_name.readlines()

# ------------------------------------------------------------------
# Data modeling after reading the contents from the file.
# ------------------------------------------------------------------
# Empty lists and tuple to store the values from the file
# after modeling the data in the desired format.
centroid_list = []
centroid_tuple = ()     
temp_list = []
points = []

# The first 7 values from the file are stored in their respective 
# variables, lists, and tuples. And the rest of the x,y values are
# stored in a list of lists.
for index in range(len(file)):
    if index == 0:
        max_iter = int(file[index].strip())                         # Max. number of iterations
    elif index == 1:
        N = int(file[index].strip())                                # Number of points in the input file
    elif index == 2:
        clusters = [[] for _ in range(int(file[index].strip()))]    # Total number of clusters (k). A list of lists.
    elif index >= 3 and index <= 6:
        centroid_list.append(int(file[index].strip()))              # Index of cluster centroids.
    else:
        str_list = file[index].strip().split(",")                   # Splits the x, y values.
        temp_list.append(int(str_list[0]))                          # Stores the x value in a temp list after converting it to an integer.
        temp_list.append(int(str_list[1]))                          # Stores the y value in a temp list after converting it to an integer.
        points.append(temp_list)                                    # Stores the x, y values as lists of lists.
        temp_list = []                                              # Deletes the items in the temp list.

# Tuples are immutable, and we don't want to change the 
# initial centroids index. Hence, converting the centroid
# list to a tuple.
centroid_tuple = tuple(centroid_list)

# Stores the points for the given centroid indexes.
# This will change with the iterations.
for index in range(len(centroid_tuple)):
    centroid_list[index] = points[centroid_tuple[index]]

# ------------------------------------------------------------------
# k-means cluster calculation or grouping of the points
# to the four centroids. 
# ------------------------------------------------------------------
# Counts the iteration where the clusters length of one iteration 
# does not equal the clusters length from the previous iteration.
stable_count = 0     

for iteration in range(max_iter):
    # Length of each of the four clusters before the N elements loop.
    clusters0_count_old = len(clusters[0])
    clusters1_count_old = len(clusters[1])
    clusters2_count_old = len(clusters[2])
    clusters3_count_old = len(clusters[3])

    # Deletes the contents of the clusters.
    clusters = [[], [], [], []] 

    for i in range(len(points)):
        # Calculates the distance between the points and the centroids.
        cent0_distance = math.sqrt((centroid_list[0][0]-points[i][0])**2 + (centroid_list[0][1]-points[i][1])**2)   
        cent1_distance = math.sqrt((centroid_list[1][0]-points[i][0])**2 + (centroid_list[1][1]-points[i][1])**2)
        cent2_distance = math.sqrt((centroid_list[2][0]-points[i][0])**2 + (centroid_list[2][1]-points[i][1])**2)
        cent3_distance = math.sqrt((centroid_list[3][0]-points[i][0])**2 + (centroid_list[3][1]-points[i][1])**2)

        # Creates a dictionary with the distance variable as key and the calculated outcome
        # as values.
        min_distance = {"cent0_distance" : cent0_distance, "cent1_distance" : cent1_distance
                      , "cent2_distance" : cent2_distance, "cent3_distance" : cent3_distance}
    
        # Evaluates the minimum or the shortest distance to the centroids.
        min_val = min(min_distance.values())

        # Returns the key to the shortest distance from the 
        # min_distance dictionary.
        for key in min_distance:
            if min_distance[key] == min_val:
                nearest_val = key
                break       # Ends the loop once the key is found.
    
        # Places the points to its nearest centroid.
        if nearest_val == "cent0_distance":
            clusters[0].append(points[i])
        elif nearest_val == "cent1_distance":
            clusters[1].append(points[i])
        elif nearest_val == "cent2_distance":
            clusters[2].append(points[i])
        else:
            clusters[3].append(points[i])
            
    # ------------------------------------------------------------------
    # Calculation for x and y mean for each of the four clusters.
    # ------------------------------------------------------------------
    x_value = 0.00      
    y_value = 0.00      

    # Iterates through the four cluster lists.
    for i in range(len(clusters)):
        # Iterates through the lists within the cluster.
        for j in range(len(clusters[i])):
            # Stores the value of list within the list
            # for comparison.
            cluster_val = clusters[i][j]

            # For the items stored in the centroid
            # we should ignore those values for 
            # calculating the x mean and y mean.
            if cluster_val == centroid_list[i]:
                continue
            else:
                x_value = x_value + cluster_val[0]
                y_value = y_value + cluster_val[1]

        # For each iteration, there will be one value in 
        # each of the cluster that matches the centroid. 
        # Hence, we need to remove that one item from the
        # denominator.
        x_mean = x_value/(len(clusters[i])-1)
        y_mean = y_value/(len(clusters[i])-1)

        # Overwriting the existing centroid with 
        # x mean and y mean values.
        centroid_list[i][0] = x_mean
        centroid_list[i][1] = y_mean

        # Resetting the value of x and y.
        x_value = 0.00
        y_value = 0.00   


    # Length of each of the four clusters after the N elements loop.
    clusters0_count_new = len(clusters[0])
    clusters1_count_new = len(clusters[1])
    clusters2_count_new = len(clusters[2])
    clusters3_count_new = len(clusters[3])

    # Counts the iteration where the clusters length of one iteration 
    # does not equal the clusters length from the previous iteration.       
    if clusters0_count_new != clusters0_count_old or clusters1_count_new != clusters1_count_old \
        or clusters2_count_new != clusters2_count_old or clusters3_count_new != clusters3_count_old:
        stable_count = stable_count + 1 
    
# ------------------------------------------------------------------
# Prints the output of the program.
# ------------------------------------------------------------------
print(f"Iterations to achieve stability: {stable_count}")
print()

for i in range(len(centroid_list)):
    print(f"Centroid {i}: {centroid_list[i]}")
    print(f"Number of points in Cluster {i}: {len(clusters[i])}")
    print(f"Cluster {i}: {clusters[i]}")
    print()

        

file_name.close()       # Closes the opened file.