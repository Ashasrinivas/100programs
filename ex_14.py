s = input(" enter the sentence : ")
up = low = 0
for c in s:
    if c.isupper():
        up = up+1
    elif c.islower():
        low = low+1
    else:
        pass
print("upper letters", up)
print("lower letters", low)