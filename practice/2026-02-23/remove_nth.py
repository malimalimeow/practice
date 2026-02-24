def remove_nth(head, n):
    
    dummy=Listnode(0)
    dummy.next=head
    fast=dummy
    slow=dummy
    
    for i in range(n):
            fast=fast.next
    
    while fast and fast.next:
        fast=fast.next    
        slow=slow.next
              
        
    slow.next=slow.next.next
        
        
    return dummy.next
        