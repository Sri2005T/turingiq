from collections import defaultdict
def adjacencylist(edges):
    graph=defaultdict(list)
    for edge in edges:
        u=edge[0]
        v=edge[1]
        graph[u].append(v)
        graph[v].append(u)
    return graph
edges=[('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G')]
print(adjacencylist(edges))
