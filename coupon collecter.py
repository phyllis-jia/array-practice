###Coupon Collector: Suppose that you have a shuffled deck of cards and you turn them face up, one by one. How many cards do you need to turn up before you have seen one of each suit? Given N distinct card types, how many random cards do you need do collect before you have (at least) one of each type?
import random
def coupon(n):
    found=[False]*n
    count=0
    distinct=0
    while distinct < n:
        val=random.randint(0,n-1)
        if not found[val]:
            distinct += 1
            found[val] = True
        count += 1
    print(count)

        