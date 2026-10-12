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

def left_view(root):
    leftview=[]
    rightview=[]
    if root is None:
        return
    q=deque([root])
    while q:
        size=len(q)
        for i in range(size):
            curr=q.popleft()
            if i==0:
                leftview.append(curr.val)
            if i==size-1:
                rightview.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return leftview,rightview
print(left_view(root))

