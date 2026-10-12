def euli(graph,u,path):
    while graph[u]:
        v=graph[u].pop()
        graph[v].remove(u)
        euli(graph,v,path)
    path.append(u)
graph={0:[1,3],1:[0,2],2:[1,3,4],3:[0,2,4],4:[2,3]}
path=[]
euli(graph,2,path)
print(path[::-1])