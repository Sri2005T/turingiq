def bst_validate(root,minvalue,maxvalue):
    if root is None:
        return True
    if root.val<minvalue or root.val>maxvalue:
        return False
    left=bst_validate(root.left,minvalue,root.val)
    right=bst_validate(root.right,root.val,maxvalue)
    return left and right