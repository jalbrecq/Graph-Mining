import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()
nx.draw_circular(G, with_labels=True)
plt.show()
