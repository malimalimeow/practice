def count_node(root):
    
    if root is None:
        return 0
    
    left=count_node(root.left)
    right=count_node(root.right)
    
    return 1+left+right

    
    