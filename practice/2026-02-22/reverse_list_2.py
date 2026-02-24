def reverse_list(head):
    prev=None
    curr=head
    #e.g:head:1->2->3->none
    while curr:
        new_node=curr.next  #new_node=2->3->None
        curr.next=prev #head:1->none
        prev=curr # prev= 1
        curr=new_node #curr=2
    
    return prev

#first set a prev with none value, and then go through the list with pointer curr.
# use new_node to remember the nodes after curr.
# swap prev and curr, then keep going on by visiting the node in new_node.