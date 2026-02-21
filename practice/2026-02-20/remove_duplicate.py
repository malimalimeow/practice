#Wrong understanding of question 
def remove_duplicate(nums):
    
    seen=set()
    
    for n in nums:
        if n in seen:
            nums.remove(n)
            
        else:
            seen.add(n)
            
    return nums

print(remove_duplicate([1,1,2]))

# remove duplicate
# hints: sorted+ inplace
# method: two pointer
# Time complexity: O(n)
# Space complexity: O(1)

def remove_duplicate_v(nums):
    
    slow=0
    
    for fast in range(1,len(nums)):
        if nums[fast]!=nums[slow]:
            slow+=1
            
            nums[slow]=nums[fast]
            
    
    return slow+1