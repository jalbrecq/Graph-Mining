import collections
import matplotlib.pyplot as plt
import networkx as nx

# load the graph
G = nx.karate_club_graph()

# extract the degree sequence
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
print("Degree sequence", degree_sequence)

# compute the number of nodes having a given centrality
degreeCount = collections.Counter(degree_sequence)
print("degreeCount", degreeCount)

# spilt into two differents list the degree and the number of nodes having that degree
deg, cnt = zip(*degreeCount.items())
print(deg, cnt)

# build and draw histogram
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
