import community
import networkx as nx
import matplotlib.pyplot as plt

data = []

for graph_id in range(0, 102):

    if(graph_id == 0):
        G = nx.karate_club_graph()
    else:
        G = nx.gnm_random_graph(34, 78)
    
    data.append([])

    # compute the best partition
    partition = community.best_partition(G)

    # draw the graph
    size = float(len(set(partition.values())))
    pos = nx.spring_layout(G)
    count = 0.

    for i, com in enumerate(set(partition.values())):

        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys()
                      if partition[nodes] == com]
        # nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=str(count * 1. / size))
        nx.draw_networkx_nodes(G, pos, list_nodes, node_size=20, node_color=(count * 0.99/ size,count * 0.99/ size, count * 0.01 / size))

        print(data)

        data[graph_id].append((i, len(list_nodes)))

    nx.draw_networkx_edges(G, pos, alpha=0.2)