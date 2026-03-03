function findMissing(nums){
    if (nums.length==0||nums==null){return false;}

    let index=0;
    for (let i=1; i<nums.length;i++){
        if (nums[index]!=i){
            return i;
        }
        else{
            index+=1;
        }
    }
}

console.log(findMissing([1,2,4,5,6]))