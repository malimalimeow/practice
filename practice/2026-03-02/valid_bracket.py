def valid_bracket(bracket):
    brackets={"(":")","{":"}","[":"]"}
    
    right=[]
    
    for b in bracket:
        if b in brackets:
            right.append(b)
            
        else:
            compare=right.pop(0)
            if b!=brackets[compare]:
                return False
            
    if right!=[]:
        return False
    
    return True

print(valid_bracket(["[","{","[","(","]","}","]"]))