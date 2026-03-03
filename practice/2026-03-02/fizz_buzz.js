function fizz_buzz(nums){
    if (nums.length==0||nums==null||nums==undefined){
        return null;
    }

    let result=[];

    for (let n of nums){
        if (n%3==0 && n%5 ==0){
            n="FizzBuzz";
            result.push(n);
        }
        else if (n%3==0){
            n="Fizz";
            result.push(n);
        }
        else if (n%5==0){
            n="Buzz";
            result.push(n);
        }
        else {
            result.push(n);
        }
    }
    return result;
}

console.log(fizz_buzz([1,2,2,3,3,3,4]))