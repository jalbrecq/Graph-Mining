import networkx as nx
import random as rdm

# generate the graph
G = nx.karate_club_graph()

# choose a random starting possiton
possition = rdm.choice(list(G.nodes))
print(possition)
print(G.degree[possition])

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

mostvisited = sorted(visited_nodes, key = visited_nodes.get,reverse = True)
print(step)
print(visited_nodes)
print(mostvisited)
