def reverse_sublist(head,m,n):
    
    dummy=Listnode(0)
    dummy.next=head
    prev=dummy.next
    #1-2-3-4-5-6
    #m=2, n=4
    
    for i in range(m-1):
        prev=prev.next
        #1-
        
    curr=prev.next#2
    
    for i in range(n-m):
        temp=curr.next
        curr.next=temp.next
        temp.next=prev.next
        prev.next=temp
        
        
    return dummy.next
        
        
        
        