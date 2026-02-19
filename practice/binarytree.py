class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.root=TreeNode(5)
        self.root.left=TreeNode(3)
        self.root.right=TreeNode(8)
        
    def in_order(self,node):
        if node is not None:
            self.in_order(node.left)
            print(node.data)
            self.in_order(node.right)
    
    def pre_order(self,node):
        if node is not None:
            print(node.data)
            self.pre_order(node.left)
            self.pre_order(node.right)
    
    def post_order(self,node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data)
            
bt=BinaryTree()
bt.in_order(bt.root)
bt.post_order(bt.root)
bt.pre_order(bt.root)
