def substring(s):

    count={}
    max_len=0
    left=0

    for right in range(len(s)):
        count[s[right]]=count.get(s[right],0)+1
        
        while len(count)>2 or count[s[right]]>3:
            count[s[left]]-=1
            
            if count[s[left]]==0:
                del count[s[left]]
            
            left+=1
                            
        max_len=max(max_len,right-left+1)

    return max_len

print(substring("aaabbbaaaccc"))
                
#First, I will go through a for loop on the string and use a dictionary to remember what character is seen and their count, until it hit the constraints.
#then I will shrink the dictionary with a left pointer, until the dictionary become valid again. In every valid point, it will return the max number of characters count.

           