import networkx as nx

# compute and display the average clustering coefficient of the karate club graph
print(nx.average_clustering(nx.karate_club_graph()))