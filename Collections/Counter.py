from collections import namedtuple, defaultdict, Counter, deque

#Counters is an easier way to keep track of the words or count things in lists.
words = 'hello I am Radu and I am really cool because my name is Radu'.split()
#words is a list and we want to see the most common words
print(Counter(words).most_common(5))


