function countChars(str){
    if (str==''||str==null){return false;}
    let count={};

    for (let s of str){
        if (s in count){
            count[s]+=1;
        }
        else{
            count[s]=1;
        }
    }
    return count;
}

console.log(countChars("bbccaa"))