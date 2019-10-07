import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy import stats
import networkx as nx

G = nx.karate_club_graph()
clC = nx.closeness_centrality(G)
bC = nx.betweenness_centrality(G)
kC = nx.katz_centrality_numpy(G)
prC = nx.pagerank(G)
degC = nx.degree_centrality(G)

Nodes = G.nodes()
correlations = [[clC[k] for k in Nodes], [bC[k] for k in Nodes], [kC[k] for k in Nodes], [prC[k] for k in Nodes], [degC[k] for k in Nodes]]

names = ['Closeness', 'Betweenness', 'Katz', 'Page rank', 'Degree']

for i in range(5):
    
    #plt.plot(correlations[i], label = names[i])
    name = names[i]
    plt.title(name)
    plt.bar(Nodes,correlations[i])
    plt.xlabel("Nodes")
    plt.ylabel("Centrality")

    plt.show()

    