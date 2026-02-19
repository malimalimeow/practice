class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:  #list 2->4->6->none
    def __init__(self):
        node1=Node(2)
        node2=Node(4)
        node3=Node(6)
        
        node1.next=node2
        node2.next=node3
        
        self.head=node1
    
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
            
B=LinkedList()
B.display()