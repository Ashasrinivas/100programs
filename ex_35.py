def printdictkeys():
    d = dict()
    for i in range(0, 21):
        d[i] = i ** 2
    for k in d.keys():
        print(k)
printdictkeys()