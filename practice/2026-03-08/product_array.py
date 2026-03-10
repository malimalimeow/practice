def product_except_self(nums):
    
    result=[]
    prefix=[1,]
    suffix=[1,]
    
    n=len(nums)
    
    product=1
    for i in range(1,n):
        product*=nums[i-1]
        prefix.append(product)         
        
    
    product_l=1
    for j in range(n-2,-1,-1):
        product_l*=nums[j+1]
        suffix.append(product_l)
    
    suffix.reverse()
    
    for i in range(n):
        result.append(prefix[i]*suffix[i])
    
    return result 

print(product_except_self([1,2,3,4]))