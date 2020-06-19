# random.sample:
# is used to create a random number in a list.
# without any duplicates
# syntax: random.sample(sequence, k)
# we will apply this on list, tuple, set or string

import random
randomlist = random.sample(range(100, 200), 5)# without duplicate values uin a list
print(randomlist)


# another way
# by using this method sometimes we get a duplicate values
import random
randomlist = []
for i in range(0, 10): # length of the list
    randomlist.append(random.randint(100, 200)) # any random numbers will print in list between the given range
print(randomlist)