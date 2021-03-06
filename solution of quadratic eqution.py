# number of solution for quadratic equation
### method 1
def result(a, b, c):
    if b**2-4*a*c > 0: 
       x1 = (-b+(b**2-4*a*c)**(1/2))/2*a
       x2 = (-b-(b**2-4*a*c)**(1/2))/2*a
       return(x1, x2)
    elif b**2-4*a*c == 0:
        x = (-b+(b**2-4*a*c)**(1/2))/2*a
        return x
    else:
        print('error')
### method 2
import math
def solve(a, b, c):
    v = pow(b,2)-4*a*c
    if v<0:
        raise ValueError('error')
    return (-b + math.sqrt(v))/(2*a), (-b-math.sqrt(v))/(2*a)


    

