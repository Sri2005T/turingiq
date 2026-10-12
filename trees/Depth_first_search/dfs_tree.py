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



def preorder(root):
    res=[]
    def helper(root):
        if root is None:
            return
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return res
    
def inorder(root):
    res=[]
    def helper(root):
        if root is None:
            return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res

def postorder(root):
    res=[]
    def helper(root):
        if root is None:
            return
        helper(root.left)
        helper(root.right)
        res.append(root.val)
    helper(root)
    return res

print("Preorder:", preorder(root))
print("Inorder:", inorder(root))
print("Postorder:", postorder(root))
    