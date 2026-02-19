def isPalindrome(x: int):
    x=str(x)
    m=len(x)//2

    i=0
    while i<=m:
        if x[i]!=x[-(i+1)]:
            return False
    i+=1
    return True

isPalindrome(123321)   

