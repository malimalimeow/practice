def find_middle(head):
    
    if not head:
        return None
    
    slow=head
    fast=head
    
    while fast and fast.next: #make sure fast and fast.next exist
        fast=fast.next.next #go 2 steps each time
        slow=slow.next #go 1 steps each time
        
    return slow