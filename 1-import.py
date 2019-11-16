import matplotlib.pyplot as plt
import networkx as nx

# load the karate club graph
G = nx.karate_club_graph()

# draw the graph
nx.draw_circular(G, with_labels=True)
plt.show()
