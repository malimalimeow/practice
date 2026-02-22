def reverse_list(head):

    if not head:
        return None
    
    prev=None
    curr=head
    
    while curr:
        next_node=curr.next #remember curr.next=2
        curr.next=prev #assign none to the node after one
        
        prev=curr #prev=1
        
        curr=next_node #keep going 
    
    return prev
        