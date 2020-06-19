
from collections import Counter
input_str = "abcdefgabc"
res = Counter(input_str)
print(res)

# another way
input_str = "abcdefgabc"
d = dict()
for i in input_str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(str(d))

# another way
input_str = "abcdefgabc"
res = {}
for keys in input_str:
    res[keys] = res.get(keys, 0)+1
print(res)