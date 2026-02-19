def cal():
    while True:
        n=None
        expression=input("start your calculation:")
        for i,s in enumerate(expression):
            if s in ["+","-","*","/","%","^"]:
                if i==0 and s=="-":
                    continue
                
                elif i>0 and expression[i-1] in ["+","-","*","/","%","^"]:
                    continue

                x,y=expression.split(s,1)
                n=s
                break
        try:    
            x, y = expression.split(s)
            x=float(x)
            y=float(y)
        
        #except x and y not number.
        except ValueError:
            print ("please input valid expression")
            continue
        
        #except n not the correct symbol.    
        if not n in ["+","-","*","/","%","^"]:
            print ("please input valid expression")
            continue
        
        
        operators={
            "+":lambda a,b:a + b ,
            "-":lambda a,b:a - b ,
            "*":lambda a,b:a * b ,
            "/":lambda a,b:a / b ,
            "%":lambda a,b:a % b ,
            "^":lambda a,b:pow(a,b)}
        
        try:
            op=operators[n]
            ans=op(x,y)
        
        except ZeroDivisionError:
            print("please input valid expression")
            continue
        
        print (ans)
    
cal()

    
    
    
    
    


