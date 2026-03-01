def path_sum(root,target):
    
    if root is None :
        return False
    
    if root.left is None and root.right is None:
        return target==root.val
    
    return path_sum(root.left,target-root.val)or path_sum(root.right,target-root.val)
    