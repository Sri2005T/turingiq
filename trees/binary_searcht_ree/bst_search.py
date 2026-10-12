def bst_search(root,val):
    if root is None:
        return False
    if root.val==val:
        return True
    if val<root.val:
        root.left=bst_search(root.left,val)
    if val>root.val:
        root.right=bst_search(root.right,val)
    return root