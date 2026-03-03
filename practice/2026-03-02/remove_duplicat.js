function remove_duplicate(nums){
    let no_duplicate=[];

    for (let n of nums){
        if (!no_duplicate.includes(n)){
            no_duplicate.push(n);
        }
    }
    return no_duplicate;
}

console.log(remove_duplicate([1,2,2,3,3,3,4]))