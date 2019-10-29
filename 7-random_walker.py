import networkx as nx
import random as rdm
import matplotlib.pyplot as plt

# generate the graph
G = nx.karate_club_graph()

data = {}
data2 = {}

for start in range(0, 34):
	# choose a random starting possiton
	# possition = rdm.choice(list(G.nodes))
	print("Starting node =", start)
	print("Degree of the starting node =", G.degree[start])

	visited_nodes = {} 

	step = 0
	possition = start

	while len(visited_nodes) != 34:

	    if possition in visited_nodes:
	        visited_nodes[possition]+=1
	    else:
	        visited_nodes[possition]=1

	    neighbors = list(G.neighbors(possition))
	    possition = rdm.choice(neighbors)

	    step+=1
	    pass

	data2[start] = step

	if G.degree[start] in data:
		old_step = data[G.degree[start]]
		data[G.degree[start]] = (old_step + step)/2
	else:
		data[G.degree[start]] = step

	# nodes, y = zip(*visited_nodes.items())
	# fig, ax = plt.subplots()
	# plt.bar(nodes, y, width=0.9, color=(0, 0.5, 0.7, 1))
	# plt.title("Histogramme du nombre de passage")
	# plt.ylabel("Count")
	# plt.xlabel("Nodes")
	# ax.set_xticks([x for x in nodes])
	# ax.set_xticklabels(nodes)

	print("Number of step =", step)
	print("-"*40)
	# mostvisited = sorted(visited_nodes, key = visited_nodes.get,reverse = True)
	# print(visited_nodes)
	# print(mostvisited)


degrees, steps = zip(*data.items())
fig, ax = plt.subplots()
plt.bar(degrees, steps, width=0.9, color=(0, 0.5, 0.7, 1))
plt.title("Nombre de passage en fonction du degre de la node de depart")
plt.ylabel("Steps")
plt.xlabel("Degree")
ax.set_xticks([x for x in degrees])
ax.set_xticklabels(degrees)

nodes, steps = zip(*data2.items())
fig, ax = plt.subplots()
plt.bar(nodes, steps, width=0.9, color=(0, 0.5, 0.7, 1))
plt.title("Nombre de passage en fonction de la node de depart")
plt.ylabel("Steps")
plt.xlabel("Nodes")
ax.set_xticks([x for x in nodes])
ax.set_xticklabels(nodes)

plt.show()
