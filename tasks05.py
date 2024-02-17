from math import exp
import time
time_start = time.time()
def f(x):
    return exp(x)


def Gauss2Recthangles(left,right,steps):
    result=0
    step=(right-left)/steps
    i=0
    for _ in range (steps):
        result += (f(((2*i+1)*step/2)-(step/(3**(1/2))))+f(((2*i+1)*step/2)+(step/(3**(1/2)))))*step/2
        i+=1
    return result  

def PrintSolution():
    left=0
    right=1
    N=10
    trueIntegral =exp(1)-1
    for _ in range (9):
        answer = Gauss2Recthangles(left,right,N)
        #print(trueIntegral)
        #print(answer)
        print('N=',N,'\tError=',trueIntegral -answer)
        N *=10
    
    
    
PrintSolution()
time_end = time.time()
time_sum = time_end - time_start
print(time_sum)