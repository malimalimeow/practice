def merge(nums1:list[int],m:int,nums2:list[int],n:int):
    nums1[m:] = []

    for x in nums2:
        nums1.append(x)
    
    nums1.sort()
    
nums1=[0]
nums2=[1]

merge(nums1,0,nums2,1)
print(nums1)