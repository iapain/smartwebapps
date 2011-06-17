"""
Clustering class
"""
import random
from math import sqrt
from django.utils.stopwords import strip_stopwords

def jaccard_distance(item1, item2):
    """
    A simple distance function (curse of dimentionality applies)
    distance(A, B) = 1 - n(A intersection B) / n(A union B) or
    distance(A, B) = 1 - n(A intersection B) / n(A) + n(B) - n(A intersection B)
    text1 and text2 are our features
    """
    feature1 = set(strip_stopwords("%s %s" % (item1.title, item1.body)).split())
    feature2 = set(strip_stopwords("%s %s" % (item2.title, item2.body)).split())
    
    if len(feature1) == 0 and len(feature2) == 0:
        return 1# max distance
    return 1 - float(len(feature1.intersection(feature2))/len(feature1.union(feature2)))
    
    
class Cluster(object):
    """
    Clustering class
    """
    def __init__(self, distance_function, items):
        self.distance = distance_functions
        self.items = items
        
    def kmeans(self, k=10, threshold=0.4):
        "k is number of clusters, threshold is minimum acceptable distance"
        # Determine the minimum and maximum values for each point
        ranges=[(min([row[i] for row in rows]),max([row[i] for row in rows]))
            for i in range(len(rows[0]))]

  # Create k randomly placed centroids
  clusters=[[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0] 
  for i in range(len(rows[0]))] for j in range(k)]
  
  lastmatches=None
  for t in range(100):
    print 'Iteration %d' % t
    bestmatches=[[] for i in range(k)]
    
    # Find which centroid is the closest for each row
    for j in range(len(rows)):
      row=rows[j]
      bestmatch=0
      for i in range(k):
        d=distance(clusters[i],row)
        if d<distance(clusters[bestmatch],row): bestmatch=i
      bestmatches[bestmatch].append(j)

    # If the results are the same as last time, this is complete
    if bestmatches==lastmatches: break
    lastmatches=bestmatches
    
    # Move the centroids to the average of their members
    for i in range(k):
      avgs=[0.0]*len(rows[0])
      if len(bestmatches[i])>0:
        for rowid in bestmatches[i]:
          for m in range(len(rows[rowid])):
            avgs[m]+=rows[rowid][m]
        for j in range(len(avgs)):
          avgs[j]/=len(bestmatches[i])
        clusters[i]=avgs
      
  return bestmatches
        