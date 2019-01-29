from collections import namedtuple, defaultdict, Counter, deque
import random

#usefull to insert on both sides of the sequences. Thread safe and will perform in the same O(1)

lst = list(range(1000000))
deq = deque(range(1000000))

def insertanddelete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index,index)

#deque is much faster!


