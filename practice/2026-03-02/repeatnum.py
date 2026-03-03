def repeat(nums):
    if nums is None:
        return None
    
    count={}
    
    for n in nums:
        count[n]=count.get(n,0)+1
        
    result=[k for k, c in count.items() if c>1]
    
    return result

print(repeat([1,2,3,2,1,1]))