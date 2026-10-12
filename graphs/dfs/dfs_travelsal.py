from collections import defaultdict
def adjacencylist(edges):
    graph=defaultdict(list)
    for edge in edges:
        u=edge[0]
        v=edge[1]
        graph[u].append(v)
        graph[v].append(u)
    return graph
def dfsTraversal(graph,node,visited,res):
    res.append(node)
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfsTraversal(graph,neighbor,visited,res)
edges=[('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G')]
graph=adjacencylist(edges)
res=[]
node='A'
visited=set()
dfsTraversal(graph,node,visited,res)
print(res)