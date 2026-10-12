from collections import defaultdict,deque

def adjacencylist(edges):
    graph=defaultdict(list)
    for edge in edges:
        u=edge[0]
        v=edge[1]
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfsTravelsal(graphs,node,res,visited):
    
    q=deque([node])
    visited.add(node)
    while q:
        curr=q.popleft()
        res.append(curr)
        for neighter in graphs[curr]:
            if neighter not in visited:
                q.append(neighter)
                visited.add(neighter)

edges=[('A','B'),('B','C'),('C','E'),('F','G')]
graphs=adjacencylist(edges)
res=[]
nodes=['A','B','C','D','E','F','G']

visited=set()


for node in nodes:
    if node not in visited:
        bfsTravelsal(graphs,node,res,visited)

print(res)
