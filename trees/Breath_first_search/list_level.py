from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.right=TreeNode(7)
root.left.right.right=TreeNode(6)



def list_level(root):
    res=[]
    if root is None:
        return res
    q=deque([root])
    while q:
        size=len(q)
        level=[]
        for i in range(size):
            curr=q.popleft()
            level.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        res.append(list(level[::]))
    return res
print(list_level(root))

