import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy import stats
import networkx as nx

G = nx.karate_club_graph()
cc = nx.closeness_centrality(G)
bc = nx.betweenness_centrality(G)
kc = nx.katz_centrality_numpy(G)
prc = nx.pagerank(G)
dc = nx.degree_centrality(G)
Nodes = G.nodes()


correlations = [[cc[k] for k in Nodes], [bc[k] for k in Nodes], [kc[k] for k in Nodes], [prc[k] for k in Nodes], [dc[k] for k in Nodes]]

names = ['Closeness', 'Betweenness', 'Katz', 'Page rank', 'Degree']

for i in range(5):    
    plt.plot(correlations[i], label = names[i],color=(0,0,0,1))
    name = names[i]
    plt.title(name)
    plt.bar(Nodes,correlations[i],color=(0.5,0.5,0.5,1))
    plt.xlabel("Nodes")
    plt.ylabel("Centrality")
    plt.show()

    