import random
import community
import networkx as nx
import matplotlib.pyplot as plt

data = []

for graph_id in range(0, 102):

    if(graph_id == 0):
        G = nx.karate_club_graph()
    else:
        G = nx.Graph()

        nodes = list(range(33))

        for i in range(78):
            src = random.choice(nodes)
            dest = random.choice(nodes)
            while src == dest:
                dest = random.choice(nodes)

            G.add_edge(src, dest)

    data.append([])

    # compute the best partition
    partition = community.best_partition(G)

    # draw the graph
    size = float(len(set(partition.values())))

    for i, com in enumerate(set(partition.values())):

        list_nodes = [nodes for nodes in partition.keys()
                      if partition[nodes] == com]

        data[graph_id].append((i, len(list_nodes)))

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show(G)
