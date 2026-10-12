from collections import deque

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

root=TreeNode(1)
node1=TreeNode(2)
root.left=node1
node2=TreeNode(3)
root.right=node2
node3=TreeNode(4)
root.right.left=node3
node4=TreeNode(5)
root.right.right=node4

def bfs(root):
    res=[]
    if not root:
        return res
    queue=deque( )
    queue.append(root)
    while queue:
        curr=queue.popleft()
        res.append(curr.val)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res
print("BFS:", bfs(root))