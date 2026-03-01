function filter_list(l) {
  let filtered=[];
  for (let n of l){
    if (typeof n === "number"){
      filtered.push(n);
    }
  }
 return filtered;}