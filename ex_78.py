import random
randomlist = random.sample([x for x in range(1000) if x % 7 == 0 and x % 5 == 0], 5)
print(randomlist)