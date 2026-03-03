function palindrome(s){
    s=Array.from(s)
    let reversed=[];
    for (let i=s.length-1;i>=0;i--){
        reversed.push(s[i]);
    }

    for (let i=0;i<s.length;i++){
        if (s[i]!=reversed[i]){
            return false;
        }
    }
    return true;
    
}

console.log(palindrome("ZZozz"))