function countSheeps(sheep) {
  if (sheep==null||sheep.length==0||sheep==undefined){
    return 0;
  }

 let count=0;
 for(let i=0; i<sheep.length; i++){
   if (sheep[i]==true){
     count+=1;
   }
 }
  return count;
  }