def two_sum(nums, target):
    seen={}
    
    for i,n in enumerate(nums):
        diff=target-n
        if diff in seen:
            return [seen[diff]+1,i+1]
        
        else:
            seen[n]=seen.get(n,i)
    
print(two_sum([1,3,5,8,26,44],49))
        
