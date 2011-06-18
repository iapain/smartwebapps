"""
Clustering class
"""
import re
import random

from django.utils.stopwords import strip_stopwords

def jaccard_distance(item1, item2):
    """
    A simple distance function (curse of dimentionality applies)
    distance(A, B) = 1 - n(A intersection B) / n(A union B) or
    distance(A, B) = 1 - n(A intersection B) / n(A) + n(B) - n(A intersection B)
    text1 and text2 are our features
    """
    feature1 = set(re.findall('\w+', strip_stopwords("%s %s" % (item1.title.lower(), item1.body.lower())))[:100])
    feature2 = set(re.findall('\w+', strip_stopwords("%s %s" % (item2.title.lower(), item2.body.lower())))[:100])

    if len(feature1) == 0 and len(feature2) == 0:
        return 1# max distance
    similarity = 1.0*len(feature1.intersection(feature2))/len(feature1.union(feature2))
    return 1 - similarity

    
class Cluster(object):
    """
    Clustering class
    """
    def __init__(self, items, distance_function=jaccard_distance):
        self.distance = distance_function
        self.items = items
        
    def kmeans(self, k=10, threshold=0.80):
        "k is number of clusters, threshold is minimum acceptable distance"
        
        #pick n random stories and make then centroid
        centroids = random.sample(self.items, k)
        
        #remove centroid from collection
        items = list(set(self.items) - set(centroids))
        
        last_matches = None
        # Max. 50 iterations for convergence.
        for t in range(50):
            # Make k empty clusters
            best_matches = [[] for c in centroids]
            min_distance = 1 # it's max value of distance
            
            # Find which centroid is the closest for each row
            for item in items:
                best_center = 0
                min_distance = 1.1
                minima = -1
                for centroid in centroids:
                    minima+=1
                    distance = self.distance(item, centroid)   
                    if distance <= min_distance:
                        best_center = minima
                        min_distance = distance
                # maintain quality of your cluster
                if min_distance <= threshold:#threshold
                    best_matches[best_center].append(item)
                    
            # If the results are the same as last time, this is complete
            if best_matches == last_matches:
                break
            last_matches = best_matches
            
        ret = []
        cnt = 0
        for c in best_matches:
            tmp = []
            seen = 0
            for i in c:
                seen = 1
                tmp.append(i)
            if seen:
                tmp.append(centroids[cnt])
            ret.append(tmp)
            cnt += 1
        return ret
  