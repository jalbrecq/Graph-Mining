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

keys = G.nodes()
correlations = [[clC[k] for k in keys], [bC[k] for k in keys], [kC[k] for k in keys], [prC[k] for k in keys], [degC[k] for k in keys]]

names = ['Closeness', 'Betweenness', 'Katz', 'Page rank', 'Degree']

plt.figure(figsize=(15,10))
for i in range(5):
    print(tuple(correlations[i]))
    #plt.plot(correlations[i], label = names[i])
    #plt.bar(len(G.degree()),tuple(correlations[i]))
    #plt.legend()
    #plt.show()

# for i in range(5):
#     for j in range(i + 1, 5):
#         print(names[i], ' vs ', names[j], ': PearsonResult', stats.pearsonr (correlations[i], correlations[j]), stats.spearmanr (correlations[i], correlations[j]))


# nx.draw_circular(G, with_labels=True,node_color=(0,0.5,0.7))