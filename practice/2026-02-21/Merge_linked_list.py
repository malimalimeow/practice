#Merge two sorted linked lists
def merge_two_list(l1,l2):
    
    dummy=Listnode(0)
    curr=dummy
    
    while l1 and l2:
        if l1.val<=l2.val:
            curr.next=l1
            l1=l1.next
        
        else:
            curr.next=l2
            l2=l2.next
        
        curr=curr.next
        
        if l1:
            curr.next=l1
        
        else:
            curr.next=l2
        
    return dummy.next
#dummy is a fake node, the value of it is zero, not part of the list, so we have to return dummy.next
#if we need to add something to dummy, we need a pointer=curr, 
#don't forget to move the pointer after we take something for this curr.
#You can do it :D!
            
        
        
        
        
        