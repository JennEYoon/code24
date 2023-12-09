# Short fibonacci code from Learn Python Programming, 2nd ed book  

def fibonacci(n):  
    # init 
    a, b = 0, 1  
    while a < n:  
        print(a)
        yield a  # yield keyword?  return a?  
        temp1 = a 
        temp2 = b
        a = temp2  # 2nd number replaces 1st number   
        b = temp1  + a  # fibonacci definition, x is sum of previous 2 numbers. 
              
# call function with input variable  
print(list(fibonacci(100)))              
# >> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]      
# 1 is repeated twice, must have copied wrong from book before.  


def fib2(n): 
    #init 
    a, b = 0, 1
    while a < n: 
        yield a 
        b, a = (a + b), b
        # must have temporary registers for a, b on RHS, before assingned to b, a on LHS.  
        #print(a, b)

print(list(fib2(100)))        

# return passes specified value to caller, while yield passes a series.  
# use yield to iterate  


