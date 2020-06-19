def printdictval():
    d = dict()
    for i in range(0, 21):
        d[i] = i**2
    for (k,v) in d.items():
        print(v)
printdictval()