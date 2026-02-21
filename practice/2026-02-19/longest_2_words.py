left=0
max_len=0
seen={}

s="abcabcaacbndj"

for right in range(len(s)):
    seen[s[right]]=seen.get(s[right],0)+1
        
    while len(seen)>2:
    
        seen[s[left]]-=1
        
        if seen[s[left]]==0:
            del seen[s[left]]
        
        left+=1
         
    max_len=max(max_len,(right-left+1))
    
print(max_len)
    
        

    
    