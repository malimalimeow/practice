function betterThanAverage(classPoints, yourPoints) {
   let class_total=yourPoints;
   
   for (let i=0; i<classPoints.length; i++){
     class_total+=classPoints[i];
   }
  
  let class_avg=class_total/(classPoints.length+1);
  
  
  if (yourPoints>class_avg){
    return true;
  }
  else{
    return false;
  }
}