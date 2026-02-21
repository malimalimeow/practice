
def two_sum(nums,target):
    seen={}
    
    for i, n in enumerate(nums):
        compliment =target-n
        
        if compliment in seen:
            return [seen[compliment],i]
        
        seen[n]=i
        
                    
print(two_sum([2,7,11,15],9))
            
# two sum
# hash map/dictionary look up
# Time complexity:O(n)
# Space complexity:O(n)
            
        
          
    
    
            
    
two_sum([1,2,3,4,5],9)
