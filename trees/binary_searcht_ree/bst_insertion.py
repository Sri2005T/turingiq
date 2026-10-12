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
root.left.left=node3
node4=TreeNode(5)
root.left.right=node4
node5=TreeNode(6)
root.right.left=node5
node6=TreeNode(7)
root.right.right=node6

def bst_insertion(root,val):
    if root is None:
        return TreeNode(val)
    if val<root.val:
        root.left=bst_insertion(root.left,val)
    if val>root.val:
        root.right=bst_insertion(root.right,val)
    return root
print(bst_insertion(root,8))