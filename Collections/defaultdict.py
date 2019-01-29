from collections import namedtuple, defaultdict, Counter, deque

#how do you get around the kew error?


challengesdone = [('mike',10),('julian',11),('mike',12)]
challengesNormal = {}

try:
    for name, challenge in challengesdone:
        challengesNormal[name].append(challenge)
    print(challengesNormal)
except:
    print('exception!!!')
print("We get an exception because mike is not a key in the dict yet")
#Use default dict to get around this


challenges = defaultdict(list)
for name, challenge in challengesdone:
    challenges[name].append(challenge)
print(challenges)