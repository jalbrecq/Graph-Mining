import networkx as nx
import random as rdm
import matplotlib.pyplot as plt
import numpy as np

# function for graph creation
def create_graph(dic, titre, y_label, x_label):
    nodes, y = zip(*dic.items())
    fig, ax = plt.subplots()
    plt.bar(nodes, y, width=0.9, color=(0, 0.5, 0.7, 1))
    plt.title(titre)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    ax.set_xticks([x for x in nodes])
    ax.set_xticklabels(nodes)
    plt.show()

# generate the graph
G = nx.karate_club_graph()

# initialise data
step_by_start = {}
step_by_start_degree = {}
box_plot_data = {}
# run the random walker 1000 times
for x in range(0, 1000):
    av_visited_nodes = {}
    print("ITERATION : ", x)

    # run the random walker with each time a different starting node
    # all the network node will be selected to be the starting node
    for start in range(0, 34):
        # the initialise the random walker
        step = 0
        possition = start

        visited_nodes = {}
        # the random walker keep walking until each node has not been visited
        while len(visited_nodes) != 34:

            if possition in visited_nodes:
                visited_nodes[possition]+=1
            else:
                visited_nodes[possition]=1

            # list all the neighbors of random walker node
            neighbors = list(G.neighbors(possition))
            # choose a random neighbors and put the walker on it
            possition = rdm.choice(neighbors)

            # increase the number of step
            step+=1
            pass

        # colect data
        if start in step_by_start:
            step_by_start[start] = (step_by_start[start] + step) / 2
        else:
            step_by_start[start] = step

        if G.degree[start] in step_by_start_degree:
            step_by_start_degree[G.degree[start]] = (step_by_start_degree[G.degree[start]] + step) / 2
        else:
            step_by_start_degree[G.degree[start]] = step

        if G.degree[start] in box_plot_data:
            box_plot_data[G.degree[start]].append(step)
        else:
            box_plot_data[G.degree[start]] = [step]

        for node in visited_nodes:
            if node in av_visited_nodes:
                av_visited_nodes[node] = (av_visited_nodes[node] + visited_nodes[node]) / 2
            else:
                av_visited_nodes[node] = visited_nodes[node]

# number of step by starting node
create_graph(step_by_start, "Nombre de pas en fonction de la node de depart", "Steps", "Starting Nodes")
# print(step_by_start)
# print(40*"-")

# number of step by degree of the starting node
create_graph(step_by_start_degree, "Nombre de pas en fonction du degre de la node de depart", "Steps", "Degree of starting Nodes")
# print(step_by_start_degree)
# print(40*"-")

# number of step by node
create_graph(av_visited_nodes, "Nombre de passages dans une node", "Count", "Nodes")
# print(av_visited_nodes)
# print(40*"-")

# number of step by degree of nodes
visited_nodes_by_degree = {}
for node in av_visited_nodes:
    if G.degree[node] in visited_nodes_by_degree:
        visited_nodes_by_degree[G.degree[node]] = (visited_nodes_by_degree[G.degree[node]] + av_visited_nodes[node]) / 2
    else:
        visited_nodes_by_degree[G.degree[node]] = av_visited_nodes[node]
create_graph(visited_nodes_by_degree, "Nombre de passages dans une node en fonction de son degre", "Count", "Degree")
# print(visited_nodes_by_degree)
# print(40*"-")


median_by_start_deg = {}
for deg in box_plot_data:
    median_by_start_deg[deg] = np.median(np.array(box_plot_data[deg]))
create_graph(median_by_start_deg, "Mediane du nombre de passage en fonction du degre du noeud de depart", "Median", "Degree")
# print(visited_nodes_by_degree)
# print(40*"-")

degree, steps = zip(*box_plot_data.items())
plt.boxplot(list(steps), patch_artist=True, labels=list(degree))
plt.show()
