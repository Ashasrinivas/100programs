import math
c = 50
h = 30
values = []
values1 = []
items = input().split(',')
for x in items:
    values.append(x)
# print(values)

# print([x for x in input().split(',')])
for d in values:
    values1.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(values1)