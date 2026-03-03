function largest(nums){
    if (nums.length==0||nums==null||nums==undefined){
        return 0;
    }

    let max=nums[0];
    for (n of nums){
        if (n>max){
            max=n;
        }
    }
    return max;
}

console.log(largest([1, 5, 2, 9, 3]))