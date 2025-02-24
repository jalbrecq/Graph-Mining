import matplotlib.pyplot as plt
import networkx as nx

# load the graph
G = nx.karate_club_graph()

# compute the differents centrality
cc = nx.closeness_centrality(G)
bc = nx.betweenness_centrality(G)
kc = nx.katz_centrality_numpy(G)
prc = nx.pagerank(G)
dc = nx.degree_centrality(G)

# list the graph nodes
Nodes = G.nodes()

# create a list of the different centrality value for each node
correlations = [[cc[k] for k in Nodes], [bc[k] for k in Nodes], [kc[k] for k in Nodes], [prc[k] for k in Nodes], [dc[k] for k in Nodes]]
names = ['Closeness', 'Betweenness', 'Katz', 'Page rank', 'Degree']

# create a graph for each centrality and display it
for i in range(5):
    name = names[i]
    plt.title(name)
    plt.plot(correlations[i], label=names[i], color=(0, 0, 0, 1))
    plt.bar(Nodes, correlations[i], color=(0.5, 0.5, 0.5, 1))
    plt.xlabel("Nodes")
    plt.ylabel("Centrality")
    plt.show()