def merge_linked_list(l1,l2):
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

#Setup a dummy head, and use a curr to be its pointer.
#To compare the value in l1 and k2, to add the smaller value to curr.next
#At the end, if only l1 or l2left, add them to curr.next to complete the merge
#return dummy.next to make sure it is only the node from l1 and l2.