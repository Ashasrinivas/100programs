li = [12,24,35,24,88,120,155,88,120,155]
se = set(li)
z = list(se)
print(z)

def removedupset(li):
    newlist = []
    seen = set()
    for item in li:
        if item not  in seen:
            seen.add(item)

            newlist.append(item)
    return newlist
li = [12,24,35,24,88,120,155,88,120,155]
print(removedupset(li))