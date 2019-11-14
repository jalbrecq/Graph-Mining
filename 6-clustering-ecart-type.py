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
    data.append(nx.average_clustering(G))

av_clustering_random /= 100
print("clustering karaté =",clustering_karate,"clustering moyen =",av_clustering_random)

variance=0
for i in data:
    variance+=(i-av_clustering_random)**2

variance/=100
ecart_type= (variance)**(1/2)

print("variance =",variance,"ecart-type =",ecart_type)

