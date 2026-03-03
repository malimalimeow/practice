function sum(nums){
    let total=0;
    if (nums.length==0||nums==null||nums==undefined){
        return 0;
    }

    for (let n of nums){
        total+=n;
    }
    return total;
}

console.log(sum([1,2,3,4]))