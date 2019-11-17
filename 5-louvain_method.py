import random
import community
import networkx as nx
import matplotlib.pyplot as plt

data = []

for graph_id in range(0, 101):

    # the first graph is the karate club graph
    if(graph_id == 0):
        G = nx.karate_club_graph()
    # all the other one are random graphs
    else:
        # create a empty graph
        G = nx.Graph()

        # create a list of 34 nodes
        nodes = list(range(34))

        # create 78 links
        for i in range(78):
            # select a random source
            src = random.choice(nodes)
            # select a random destination
            dest = random.choice(nodes)

            # make sure the source and the destination are differents
            while src == dest or G.has_edge(src, dest):
                dest = random.choice(nodes)

            # create the link beteewn the selected nodes
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

    # valeur de la modularité
    mod = community.modularity(partition,G)
    print("modularity: %0.5f"%mod)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 8))
    plt.axis('off')
    if graph_id == 0:
        plt.title("Graph Karaté club")
    else:
        plt.title("Graph n°" + str(graph_id))
    nx.draw_networkx_nodes(G, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    plt.show(G)
