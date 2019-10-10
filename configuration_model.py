# -*- coding: utf-8 -*-
import networkx as nx

# The Zachary’s Karate Club graph
G = nx.karate_club_graph()

# Create a new graph with the degree sequence of the Zachary’s Karate Club graph
G = nx.configuration_model([d for n, d in G.degree()])
config_model_degseq = [d for n, d in G.degree()]

# Remove selfloop from the new graph
G.remove_edges_from(G.selfloop_edges())

# Remove the parallel edges
G = nx.Graph(G)
without_paraledges_degseq = [d for n, d in G.degree()]

# Removed edges ratio
nb_edges_config_model = 0
nb_edges_without_paraledges = 0
for i in range(len(G)):
    nb_edges_config_model = nb_edges_config_model + config_model_degseq[i]
    nb_edges_without_paraledges = nb_edges_without_paraledges + without_paraledges_degseq[i]
edges_removed = float((nb_edges_config_model / 2) - (nb_edges_without_paraledges / 2))
nb_edges = float(nb_edges_config_model / 2)
ratio = int(edges_removed / nb_edges * 100)
print(str(int(edges_removed)) + "/" + str(int(nb_edges)))
print(str(ratio) + "%")
