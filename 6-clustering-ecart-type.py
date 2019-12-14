import random
import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy

data_graph = []
data_biggest_com=[]

clustering_karate = nx.average_clustering(nx.karate_club_graph())

av_clustering_random = 0
av_clustering_biggest_com=0

#bool to display the graphs and its biggest community 
display= True

for graph_id in range(0, 101):

    # the first graph is the karate club graph
    if(graph_id == 0):
        G = nx.karate_club_graph()
    #create 100 random graph
    else: 
        G = nx.Graph()
        nodes = list(range(34))

        for i in range(78):
            src = random.choice(nodes)
            dest = random.choice(nodes)
            while src == dest:
                dest = random.choice(nodes)

            G.add_edge(src, dest)

        #compute the 100 clustering to make an average  
        av_clustering_random += nx.average_clustering(G)    
        data_graph.append(nx.average_clustering(G))

    
    #louvain method on graph
    partition = community.best_partition(G)
    #extract the biggest community in louvain method
    biggest_community=[]
    for i, com in enumerate(set(partition.values())):

        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]

        if len(list_nodes)>len(biggest_community):
            biggest_community=list_nodes

    #create a graph with the biggest community
    H = nx.Graph()    
    
    for node in biggest_community:
        for edge in G.edges(node):
            link=edge[1]
            if link in biggest_community:                   
                H.add_edge(node, link) 
    #just to display or not the graphs and the graph for the biggest community 
    if display:
        plt.subplot(121)
        plt.title("biggest_community")
        nx.draw_circular(H, with_labels=True)
        plt.subplot(122)
        plt.title("original graph")
        nx.draw_circular(G, with_labels=True)
        plt.show()

    if graph_id == 0:
        big_com_clustring_karate = nx.average_clustering(H)
    else:
        av_clustering_biggest_com += nx.average_clustering(H)
        data_biggest_com.append(nx.average_clustering(H))

#compute the average clustering for the graphs and the biggest community
av_clustering_random /= 100
av_clustering_biggest_com /= 100
print("clustering karate =",clustering_karate)
print("clustering of the biggest community of the karate graph =", big_com_clustring_karate,"\n")
print("average clustering 100 random graph=",av_clustering_random)
print("average clustering biggest community 100 random graph =",av_clustering_biggest_com,"\n")

#compute the average variances and standard deviations for the graphs and the biggest community
variance=0
for i in data_graph:
    variance += (i-av_clustering_random)**2

variance/=100
ecart_type= (variance)**(1/2)

variance_com=0
for i in data_biggest_com:
    variance_com +=(i-av_clustering_biggest_com)**2

variance_com/=100
ecart_type_com = (variance_com)**(1/2)

print("variance 100 random graph =",variance)
print("ecart type 100 random graph=",ecart_type,"\n")
print("variance biggest community 100 random graph =",variance_com)
print("ecart type biggest community 100 random graph =",ecart_type_com)