function countChars(str){
    let count={};
    for (let s of str){
        if (s!=" ")
        {count[s]=(count[s]||0)+1;}
    }
    return count
}

console.log(countChars("HEidy LEUNG"))