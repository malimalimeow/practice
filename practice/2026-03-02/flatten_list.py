def flatten_list(nums):
    flatten_nums=[]
    for n in nums:
        if isinstance(n,list): #to check n data type with 'isinstance' function
            flatten_nums.extend(flatten_list(n)) #extend them to the list
            
        else:
            flatten_nums.append(n) #if it is not a list, just append them.
            