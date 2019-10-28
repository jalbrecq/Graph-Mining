import random
import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy

data = []

clustering_karate = nx.average_clustering(nx.karate_club_graph())

av_clustering_random = 0
for graph_id in range(0, 100):

    G = nx.Graph()

    nodes = list(range(34))

    for i in range(78):
        src = random.choice(nodes)
        dest = random.choice(nodes)
        while src == dest:
            dest = random.choice(nodes)

        G.add_edge(src, dest)

    av_clustering_random += nx.average_clustering(G)
    
    data.append([])

print(av_clustering_random)
av_clustering_random /= 100
print(clustering_karate,av_clustering_random)

