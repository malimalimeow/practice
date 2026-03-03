function Validation(pw){
    if (pw.length==0||pw==null){return false;}
    const pattern=/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[a-zA-z\d!@#$%^&*]{8,}$/

    result=pattern.test(pw)

    return result
}

console.log(Validation("hihihihihihi1"))