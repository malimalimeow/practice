function reverse_string(s){
    let reversed=[];

    s=Array.from(s)
    
    for (let i=s.length-1;i>=0;i--){
        reversed.push(s[i]);
    }
    return reversed.join()
} 

console.log(reverse_string("heidy"))