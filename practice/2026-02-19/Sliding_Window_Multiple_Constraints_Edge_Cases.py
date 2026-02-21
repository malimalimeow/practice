def sliding_multi(s,k,m,target_sum,t):
    ascii_count=0
    max_len=0
    left=0
    count={}
    repeat=1
    new_left=0
    
    
    for right in range(len(s)):
        count[s[right]]=count.get(s[right],0)+1
        ascii_count+=ord(s[right])
        
        if right>0 and s[right]==s[right-1]:
            repeat+=1
        
        else:
            repeat=1
            
        if repeat>t:
            new_left=right-t+1
            while left< new_left:
                count[s[left]]-=1
                ascii_count-=ord(s[left])
            
                if count[s[left]]==0:
                    del count[s[left]]
            
                left+=1
                


        while ascii_count>target_sum or len(count)>k or count.get(s[right], 0)>m :
            
            count[s[left]]-=1
            ascii_count-=ord(s[left])
            
            if count[s[left]]==0:
                del count[s[left]]
            
            left+=1
            
            
        max_len=max(max_len,right-left+1)
        
    return max_len

                
print(sliding_multi("aaabbbaaaccc",2,3,500,2))         

#I iterate the string, use a dictionary to remember the seen characters and their count, and also count the ASCII value at the same time.
#When the window(the dictionary) violates to any constraints, left will start shrinking the window,until the window become valid. 
# In every valid case, I will update the maximum length, and return it at the end.  