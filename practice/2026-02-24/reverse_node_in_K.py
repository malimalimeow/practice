def reverse_K(head,k):
    dummy=Listnode(0)
    dummy.next=head
    prev=dummy
    #1-2-3-4-5-6
    
    while prev and prev.next:
        for i in range(k-1):
            first=prev.next #remember first one->after loop will be tail #1
            temp=first.next #2
            first.next=temp.next#1-3
            temp.next=prev.next #0->2->1
            prev.next=temp #*2
        
        prev=first #prev go to first after the loop, then it can match the first in loop afterward.
        
    
    return dummy.next
            
        
        
        
            
            
        