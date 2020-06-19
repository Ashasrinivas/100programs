def printlist():
    li = []
    for i in range(1, 20):
        li.append(i ** 2)
    print(li[-15:])
printlist()