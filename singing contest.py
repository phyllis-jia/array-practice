##singing contest: to design a program which remove the highest score and the lowest score from scores, then take average of the remain scores as final score
def score(a):
    h=max(a)
    l=min(a)
    x=(sum(a)-h-l)/(len(a)-2)
    return x

    