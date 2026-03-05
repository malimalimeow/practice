function flatten(arr) {
    let result=[];
    for (let n of arr){
        if(Array.isArray(n)){
            result.push(...flatten(n));
        }

        else{
            result.push(n);}
}
return result
}
console.log(flatten([1, [2, [3, 4], 5], 6]))
