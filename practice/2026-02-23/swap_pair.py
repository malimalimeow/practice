def swap_pairs(head):
    dummy=Listnode(0)
    dummy.next=head#1
    prev=dummy #0
    
    #0->1->2->3->4->5
    while prev.next and prev.next.next:
        first=prev.next #1
        second=first.next #2
        
        first.next=second.next #1-3
        second.next=first #2-1-3
        prev.next=second #prev point to the exchanged list
        
        prev=prev.next # prev go 1 step
    
    return dummy.next
        
        
       
        
        
        
    
    return dummy.next
        
        
        
        
        
        
        
        
        
        