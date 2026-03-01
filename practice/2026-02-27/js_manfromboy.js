function menFromBoys(arr){
  let even=[];
  let odd=[];
  
  arr=[...new Set(arr)];
  
  for(let i=0;i<arr.length;i++){
    if (arr[i]%2==0){
      even.push(arr[i]);
    }
    else{
      odd.push(arr[i]);
    }
  }
  
  even.sort((a,b)=>a-b);
  odd.sort((a,b)=>b-a);
  
even.push(...odd);
  
  return even
}