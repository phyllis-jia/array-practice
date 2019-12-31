###shuffle cards
#method 1
import random
def shuffle(cards):
    random.shuffle(cards)
    return cards

#method 2
def shuffle_list(cards):
    for i in range(len(cards)):
        randomi = i + random.randint(0,len(cards)-i-1)
        cards[i], cards[randomi] = cards[randomi], cards[i]
    return cards


    