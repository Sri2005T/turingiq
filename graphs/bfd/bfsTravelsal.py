from collections import defaultdict,deque

def adjacencylist(edges):
    graph=defaultdict(list)
    for edge in edges:
        u=edge[0]
        v=edge[1]
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bfsTravelsal(graphs,node):
    res=[]
    visited=set()
    q=deque([node])
    visited.add(node)
    while q:
        curr=q.popleft()
        res.append(curr)
        for neighbor in graphs[curr]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    return res

edges=[('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G')]
graphs=adjacencylist(edges)
node='A'
print(bfsTravelsal(graphs,node))
