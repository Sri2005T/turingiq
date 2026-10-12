from collections import defaultdict
def adjacencylist(edges):
    graph=defaultdict(list)
    for edge in edges:
        u=edge[0]
        v=edge[1]
        graph[u].append(v)
        graph[v].append(u)
    return graph
def dfsTraversal(graph,node,res,visited):
    res.append(node)
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfsTraversal(graph,neighbor,res,visited)
edges=[('A','B'),('B','C'),('C','E'),('F','G')]
graph=adjacencylist(edges)
res=[]
visited=set()
nodes=['A','B','C','D','E','F','G']
for node in nodes:
    if node not in visited:
        dfsTraversal(graph,node,res,visited)

print(res)
