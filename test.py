import random as rdm

#Reads the graph from a GML File, named lesmis.gml
G = nx.read_gml("lesmis.gml",relabel=True)

#Start the counter
counter = 0

#Start execution counter
execution = 0

#Execute 10 times this command sequence
while execution < 10:
    #Choose a random start node
    vertexid = rdm.choice(G.nodes())
    #Dictionary that associate nodes with the amount of times it was visited
    VisitedVertex = {}

    print("Execucao n°" % (execution + 1))
    #Execute the random walk with size 10000 (10000 steps)
    while counter < 10000: 
        #Accumulate the amount of times each vertex is visited
        if vertexid in VisitedVertex:
                VisitedVertex[vertexid] += 1
        else:
                VisitedVertex[vertexid] = 1
        #Visualize the vertex neighborhood
        Vertex_Neighbors = G.neighbors(vertexid)
        #Choose a vertex from the vertex neighborhood to start the next random walk
        vertexid = rdm.choice(Vertex_Neighbors)
        #Iteration counter increment
        counter = counter + 1

    #Organize the vertex list in most visited decrescent order
    mostvisited = sorted(VisitedVertex, key = VisitedVertex.get,reverse = True)
    #Separate the top 10 most visited vertex
    top_10 = mostvisited[:10]
    print(top_10)

    #Restart the cycle
    execution = execution + 1
    counter = 0

print("Feche a janela de exibicao para encerrar.")

#Draw graph to a window
nx.draw_circular(G)

plt.savefig('myfig')
plt.show()
