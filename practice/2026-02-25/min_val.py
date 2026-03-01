def find_min(root):
    if root is None:
        return None
    
    left=find_min(root.left)
    right=find_min(root.right)
     
    return min(left,right)