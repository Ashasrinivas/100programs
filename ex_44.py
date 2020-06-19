li = [1,2,3,4,5,6,7,8,9,10]
l =[]
for i in li:
    if i % 2 == 0:
        l.append(i)
print(l)


# using fiter function
li = [1,2,3,4,5,6,7,8,9,10]
is_even = lambda x : x % 2 == 0
li2 = list(filter(is_even, li))
print(li2)
fi