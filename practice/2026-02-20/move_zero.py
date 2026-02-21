def move_zero(nums):
    slow=0
    
    for fast in range(len(nums)):
        if nums[fast]!=0:
           nums[slow]=nums[fast]
           slow+=1
           
    for i in range(slow,len(nums)):
        nums[i]=0
            
    return nums

print(move_zero([0,0,1,2,3,4]))

#move zero
#inplace!
# two pointer
#remember to add the 0 back!