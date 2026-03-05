function firstUniqueChar(str) {
    let single=new Set(str);
    let count={};

    for(n of str){
        count[n]=(count[n]||0)+1;
    }
    
    for (n of single){
        if (count[n]==1){
            return n
        }
    }

}

console.log(firstUniqueChar("hhhelloe"))

