def same_tree(p,q):
    
    if p is None and q is None:
        return True    
    
    if p is None or q is None:
        return False
    
    if p.val!=q.val:
        return False
    
    
    return same_tree(p.left,q.left) and same_tree(p.right,q.right)