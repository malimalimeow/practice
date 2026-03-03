function count_vowels(s){
    let count=0;
    vowels=["a","e","i","o","u","A","E","I","O","U"];

    s=Array.from(s);

    for (let c of s){
        if (vowels.includes(c)){
            count+=1;
        }
    }
    return count;
}

console.log(count_vowels("aaaa"))