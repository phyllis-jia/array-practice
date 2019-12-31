###calculate pi
## method 1: pi/4=1-1/3+1/5-....
def pi_cal(n):
    pi = 0
    a = 1
    for i in range(1, n+1, 2):
        pi += 4*a*(1/i)
        a *= -1
    return pi

### method 2
def pi_cal2():
    i = 1
    pi = 0
    a = 1
    pre = 9999
    delta = 0.00001
    
    while (abs(pi-pre)) > delta:
        pre = pi
        pi += a*(1/i)
        a *= -1
        i += 2
    return pi*4
        
        
    