def reverse_sublist(head,m,n):
    
    dummy=listnode(0)
    dummy.next=head
    prev=dummy 
    
    for i in range(m-1): 
        prev=prev.next 
        #prev=0->1(prev)->2->3->4->5      
        #remember prev as position m-1 
    curr=prev.next #2 
    #remember curr as end of the reversion tail
    
    for i in range(n-m):
        next_node=curr.next #next:3->4->5/4->5
        curr.next=next_node.next #curr:2->4->5/5
        next_node.next=prev.next #next:3->2->4->5/4->3->2->5
        prev.next=next_node 
        #prev=0->1->3->2->4->5
        #prev=0->1->4->3->2->5
        
    return dummy.next