def Divgenerator(n):
    for i in range(n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
n = int(input("enter the value : "))
value = []
for i in Divgenerator(n):
    value.append(str(i))
print(",".join(value))