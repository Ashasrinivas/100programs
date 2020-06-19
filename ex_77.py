import random
randomlist = random.sample([x for x in range(200) if x % 2== 0], 5)
print(randomlist)