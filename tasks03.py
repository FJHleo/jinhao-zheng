from math import exp

def f(x):
    return exp(x)

def trapezoidRecthangles(left,right,steps):
    result=0
    step=(right-left)/steps
    i=0
    for _ in range (steps):
        result +=(f(step*i)+f(step*(i+1)))*0.5*step
        i+=1
        return result
 
def PrintSolution():
    left=0
    right=1
    N=10
    trueIntegral =exp(1)-1
    for _ in range (9):
        answer = trapezoidRecthangles(left,right,N)
        print('N=',N,'\tError=',trueIntegral -answer)
        N *=10
    
    
    
PrintSolution()