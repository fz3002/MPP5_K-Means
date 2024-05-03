"""Main module containing k-means clustering functions"""
import csv
import random

class KMeans:
    """Class containing functions for k-means clustering"""
    def __init__(self, data_set, k):
        self.cluster_error = -1
        self.data_set = data_set
        self.k = k
        self.clusters = self.__create_initial_clusters()
        self.centroids = {}

    def __compute_distance_square(self, vector1, vector2):
        """private function for computing distance between 2 vectors

        Arguments:
            vector1 -- list of float values represeting vector
            vector2 -- list of float values represeting vector

        Returns:
            float value of distance between vectors
        """
        distance = 0
        for i, (elem1, elem2) in enumerate(zip(vector1, vector2)):
            distance += (float(elem1) - float(elem2))**2


        return distance

    def __compute_centroid(self, list_of_vectors):
        centroid = []

        if len(list_of_vectors) == 0:
            return [0]*self.k

        for i in range(len(list_of_vectors[0])):
            sum_coords = 0
            for vector in list_of_vectors:
                sum_coords += float(vector[i])
            centroid.append(sum_coords/len(list_of_vectors))

        return centroid

    def __create_initial_clusters(self):

        clusters = {}

        for i in range(self.k):
            clusters[i] = []

        return clusters

    def __assign_random_clusters(self):

        for vector in self.data_set:
            self.clusters[random.randint(0, self.k-1)].append(vector)

    def __assign_to_clusters(self):

        new_clusters = self.__create_initial_clusters()

        for vector in self.data_set:
            distances = [self.__compute_distance_square(vector, self.centroids[i]) for i in range(self.k)]
            new_clusters[distances.index(min(distances))].append(vector)

        self.clusters = new_clusters

    def __compute_error(self):
        error = 0
        for i in range(self.k):
            for vector in self.clusters[i]:
                error += self.__compute_distance_square(vector,self.centroids[i])

        return error

    def compute(self):
        """Main computing function"""
        self.__assign_random_clusters()

        for i in range(self.k):
            self.centroids[i] = self.__compute_centroid(self.clusters[i])

        new_error = 0

        while(self.cluster_error != new_error):
            self.cluster_error = new_error
            self.__assign_to_clusters()
            for i in range(self.k):
                self.centroids[i] = self.__compute_centroid(self.clusters[i])
            new_error = self.__compute_error()
            print("E:", new_error)
            print(self.clusters)
        


def read_file(file_name):
    """This is a function that reads CSV file and returns list of lines.

    Args:
        file_name (str): File name

    Returns:
        list : List of lines
    """
    list_vec = []
    with open(file_name, newline='', encoding='utf-8') as f:
        lines = csv.reader(f, delimiter=";")
        for row in lines:
            list_vec.append(row[0].split(','))
    f.close()
    
    return list_vec


kmeans = KMeans(read_file('test.csv'), 3)
kmeans.compute()
