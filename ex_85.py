# Enumerate :
# this function is used to adds a counter to the key of enumerate object
# this function assign an index to each item in an iterable object(list, tuple, string) that can be used to reference the item
# syntax : enumerate(iterable, start)

li = [12,24,35,70,88,120,155]
a =  [ x for (i,x) in enumerate(li) if x % 2 != 0]
print(a)