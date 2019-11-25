import random
import community
import networkx as nx
import matplotlib.pyplot as plt

data = []
configuration_model = False
no_selfloop_no_parraledge = False

for graph_id in range(0,1):

    # the first graph is the karate club graph
    if(graph_id == 0):
        G = nx.karate_club_graph()
    # all the other one are random graphs
    else:
        if configuration_model:
            G = nx.configuration_model([d for n, d in nx.karate_club_graph().degree()])
            if no_selfloop_no_parraledge:

                # Remove the parallel edges
                G = nx.Graph(G)
                # Remove selfloop from the new graph
                G.remove_edges_from(G.selfloop_edges())

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
    x=[]
    for i, com in enumerate(set(partition.values())):

        list_nodes = [nodes for nodes in partition.keys() if partition[nodes] == com]
        if len(list_nodes)>len(x):
            x=list_nodes
        data[graph_id].append((i, len(list_nodes)))


    # valeur de la modularité
    if graph_id==0:        
        H = nx.Graph()
        nodes = x
        print(len(x),x)
        for node in nodes:
            for edge in G.edges(node):
                link=edge[1]

                if link in nodes:                   
                    H.add_edge(node, link)

        print(H.edges(),len(H.edges()))
              

        pos = nx.spring_layout(H)
        plt.figure(figsize=(8, 8))
        plt.axis('off')
        if graph_id == 0:
            plt.title("Graph Karaté club")
        else:
            plt.title("Graph n°" + str(graph_id))
        # nx.draw_networkx_nodes(H, pos, node_size=600, cmap=plt.cm.RdYlBu, node_color=(0.5,0.5,0.5))
        # nx.draw_networkx_labels(H,pos)
        # nx.draw_networkx_edges(H, pos, alpha=0.3)
        nx.draw_circular(H, with_labels=True)
        
        plt.show()
