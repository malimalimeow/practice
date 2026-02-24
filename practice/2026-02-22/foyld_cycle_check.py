def detect_cycle(head):
    slow=head
    fast=head
    
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        
        if fast==slow:
            return True
    
    return False

def find_cycle_start(head):
    if detect_cycle(head)==False:
        return None
    
    slow=head
    fast=head
    curr=head
    
    while fast and fast.next:
        
        fast=fast.next.next
        slow=slow.next
        
        if fast==slow:
            break
        
    while curr!=slow:
        curr=curr.next
        slow=slow.next
        
    
    return curr
            
            