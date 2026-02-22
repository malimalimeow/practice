def detect_cycle(head):
    
    if not head:
        return False
    
    fast=head
    slow=head
    
    while fast and fast.next:
        
        fast=fast.next.next
        slow=slow.next
        
        if fast==slow:
            return True
        
    return False


def find_loop_start(head):
    
    if not head:
        return False
    #when there is a loop, find start point.
    
    fast=head
    slow=head
    curr=head
    
    while fast and fast.next:
        
        fast=fast.next.next
        slow=slow.next
        
        if fast==slow:#make sure there is a loop
            break
    
    while curr!=slow:
        curr=curr.next
        slow=slow.next
        
    return curr
    
                
            
        
            
        
    
        