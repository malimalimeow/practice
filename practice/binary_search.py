def binary_search(arr,target):
    left=0
    right=len(arr)-1
    
    while left<=right:
        mid=(left+right)//2
        
        if arr[mid]==target:
            return mid
        
        elif mid<target:
            left=mid+1
        
        else:
            right=mid-1
    
    return -1

mylist=[1,2,3,4,5,6,7,8,9,15,28,30]   
target_number=28

result=binary_search(mylist,target_number)
if result != -1:
    print(f"number {target_number}is in the list，index is {result}")
else:
    print(f"number {target_number} is not in the list")