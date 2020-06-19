values = []
items = [x for x in input().split(',')]
for i in items:
    inti = int(i, 2)
    if not inti % 5:
        values.append(i)
print(','.join(values))

