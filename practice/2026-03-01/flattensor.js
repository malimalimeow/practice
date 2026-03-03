function flatandsort(nums){
    if (nums.length==0||nums==null){
        return [];
    }
    let flatten=[];
    for (let n of nums){
        if (Array.isArray(n)){ //<-new syntax, just check from internet.
            flatten.push(...n)
        }
        else{
            flatten.push(n)
        }
    }

    return flatten.sort((a,b)=>a-b);
}

console.log(flatandsort([[3,2,1], [4,6,5], [], [9,7,8]]))