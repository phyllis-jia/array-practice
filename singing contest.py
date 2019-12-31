##singing contest: to design a program which remove the highest score and the lowest score from scores, then take average of the remain scores as final score
### optimized one 
def singing_score(values):
    small_pos = 0
    for i in range(1, len(values)):
        if values[i] < values[small_pos]:
            small_pos = i
            
    high_pos = 0
    for i in range(1, len(values)):
        if values[i] > values[high_pos]:
            high_pos = i
            
    values.remove(values[small_pos])
    values.remove(values[high_pos])
    rst = sum(values)/len(values)
    return rst

###optimized two
def singing_score2(values):
    maxx = values[0]
    minn = values[0]
    summ = values[0]
    for i in range(1,len(values)):
        if values[i]<minn:
            minn = values[i]
        if values[i]>maxx:
            maxx = values[i]
        summ += values[i]
        
    rst = (summ-maxx-minn)/(len(values)-2)
    return rst

### original one
def score(a):
    h = max(a)
    l = min(a)
    x = (sum(a)-h-l)/(len(a)-2)
    return x

    