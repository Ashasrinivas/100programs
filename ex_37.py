def printlist():
    li = []
    for i in range(1, 21):
        li.append(i  ** 2)
    print(li[0:5])
printlist()


def printlist():
    n = input("enter any 10 values : ")
    li = []
    for i in range(10):
        li.append(i ** 2)
    print(li[:10])
printlist()