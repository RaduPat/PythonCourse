from collections import namedtuple, defaultdict, Counter, deque
import csv
import random
from urllib.request import urlretrieve

#Named Tuple
#convenient way to define a class without methods. Allows to store dict like objects that you can access by attributes

user = namedtuple('bob','coder')

#instead you can name it and avoid accessing it using indexes

User = namedtuple('User', 'name role')

user = User(name='bob', role='coder')
print(user.name +' is a '+user.role)

#used name tuples to make for more readable code



