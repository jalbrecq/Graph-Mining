import networkx as nx
import random as rdm
import matplotlib.pyplot as plt

# generate the graph
G = nx.karate_club_graph()

# choose a random starting possiton
possition = rdm.choice(list(G.nodes))
print("Starting node =", possition)
print("Degree of the starting node =", G.degree[possition])

visited_nodes = {}

step = 0

while len(visited_nodes) != 34:

    if possition in visited_nodes:
        visited_nodes[possition]+=1
    else:
        visited_nodes[possition]=1

    neighbors = list(G.neighbors(possition))
    possition = rdm.choice(neighbors)

    step+=1
    pass

nodes, y = zip(*visited_nodes.items())
fig, ax = plt.subplots()
plt.bar(nodes, y, width=0.9, color=(0, 0.5, 0.7, 1))
plt.title("Histogramme du nombre de passage")
plt.ylabel("Count")
plt.xlabel("Nodes")
ax.set_xticks([x for x in nodes])
ax.set_xticklabels(nodes)

print("Number of step =", step)
# mostvisited = sorted(visited_nodes, key = visited_nodes.get,reverse = True)
# print(visited_nodes)
# print(mostvisited)

plt.show()
