function mostFrequentChar(str) { 
    let count={};
    let most=0;
    let result=undefined;

    for (let s of str){
        if (s!=" "){
            count[s]=(count[s]||0)+1;    
        }
    }
    
    for (let c in count){
        if (count[c]>most){
            most=count[c];
            result=c;
        }
    }
    return result
    
 }

console.log(mostFrequentChar("Viiiiiii"))