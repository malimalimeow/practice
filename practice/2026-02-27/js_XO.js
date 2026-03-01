function XO(str) {
    let x=0;
    let o=0;
  
  str=str.toLowerCase();
  str=Array.from(str);
  
  for (let i = 0; i<str.length; i++){
    if (str[i]=='x'){
      x+=1;
    }
    else if(str[i]=='o'){
      o+=1
    }
  }
  if (x==o){
    return true;
  }
  else{
    return false;
  }
}