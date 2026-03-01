function findAverage(array) {
  if (array.length===0||array==null||array==undefined)
  {return 0;}
  
  let avg=0;
  return avg=array.reduce((a,b)=>a+b,0)/array.length
}