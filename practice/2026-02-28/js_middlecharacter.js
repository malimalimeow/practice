function getMiddle(s) {

if (s==""||s==null||s==undefined){
    return "";}

let char=Array.from(s);
    console.log(char);
if (char.length==1){
    return s;
}


if (char.length %2==0){
return char[(char.length/2)-1]+char[(char.length/2) ]
}
else{
    return char[(Math.round(char.length/2))-1]
}

}

console.log(getMiddle("lovAe"))

