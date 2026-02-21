def best_time(prices):
    
    small=9999
    max_profit=0
    profit=0
    
    for n in prices:
        if n < small:
            small=n
        else:
            profit=n-small    
            max_profit=max(max_profit,profit)        
    
    return max_profit

print(best_time([7,1,5,3,6,4]))
        
    
#best time
#Greedy tracking state
#track min <--   
        
        
        
        
        
    
    
            
        