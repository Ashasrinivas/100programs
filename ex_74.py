# random.choice is used to pick a randomm elemnt in a list
import random
print(random.choice([x for x in range(11) if x %2 == 0]))


import random
print(random.choice([x for x in range(201) if x % 7 == 0 and x % 5 == 0 ]))