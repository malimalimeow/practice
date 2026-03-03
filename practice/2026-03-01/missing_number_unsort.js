function missing(nums){
    if (nums.length==0||nums==null){return false;}
    let n =nums.length+1;
    let expected=(n*(n+1))/2;
    for (m of nums){
        expected-=m;
    }
    return expected;

}

console.log(missing([1,2,3,4,6,7,8,9,10]))