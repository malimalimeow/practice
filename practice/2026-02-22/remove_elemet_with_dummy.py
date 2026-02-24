def remove_element(head):
    
    if not head:
        return None
    
    dummy=Listnode(0)
    curr=dummy
    

    while head:
        
        if head.val!=6:
            curr.next=head
            curr=curr.next
        
        head=head.next
        
    curr.next=None   
    return dummy.next
        
    
    #setup a dummy head and use a pointer to collect every node that not 6 from head.
    #while head is there, and the value is not 6 , 
    #next curr will have that val, then curr go one step, and 
    #head will go one step no matter curr take value or not.
        
        
        
            
        
        
        
            
        
        
        