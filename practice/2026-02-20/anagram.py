def anagram(s,t):
    count_s={}
    
    if len(s)!=len(t):
        return False
    
    for n in s:
        count_s[n]=count_s.get(n,0)+1
        
    for m in t:
        if not count_s[m]:
            return False
        else:
            count_s[m]-=1
        
    if count_s[m]<0:
        return False
        
    return True

print(anagram("kkmo","mokk"))