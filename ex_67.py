def Evengenerator(n):
    i = 0
    while i<n:
        if i % 2 == 0:
            yield i
        i += 1
n = int(input("enter the n value : "))
values = []
for i in Evengenerator(n):
    values.append(str(i))
print(",".join(values))
