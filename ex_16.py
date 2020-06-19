li = []
values = input()
numbers = [x for x in values.split(",") if int(x) % 2 != 0]
print(",".join(numbers))
for i in numbers:
    a = str(int(i) * int(i))
    li.append(a)
print(",".join(li))