def duplicate(nums):
    seen=set()
    
    for n in nums:
        if n not in seen:
            seen.add(n)
        
        else:
            reture True
    
    return False