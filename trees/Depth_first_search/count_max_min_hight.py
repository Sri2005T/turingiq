class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

def count_nodes(root):
    if root is None:
        return 0
    return 1+count_nodes(root.left)+count_nodes(root.right)
#print(count_nodes(root))

def max_Nodes(root):
    if root is None:
        return 0
    return max(root.val, max(max_Nodes(root.left), max_Nodes(root.right)))
#print(max_Nodes(root))

def min_Nodes(root):
    if root is None:
        return 0
    return min(root.val, min(min_Nodes(root.left), min_Nodes(root.right)))
#print(min_Nodes(root))

def hight_node(root):
    if root is None:
        return 0
    return 1 + max((hight_node(root.left), hight_node(root.right)))
print(hight_node(root))
