# import matplotlib.pyplot as plt
# import networkx as nx

# G = nx.karate_club_graph()
# degs={}
# for n in G.nodes():
#   deg = G.degree(n)
#   if deg not in degs:
#       degs[deg]=0

#   degs[deg]+=1

# items = sorted(degs.items())

# plt.hist(items)
# plt.show()

import collections
import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()

degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())


fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.9, color=(0, 0.5, 0.7, 1))

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d for d in deg])
ax.set_xticklabels(deg)

# draw graph
plt.axes([0.4, 0.38, 0.5, 0.5])
nx.draw_circular(G, with_labels=True, node_color=(0, 0.5, 0.7))
plt.show()
