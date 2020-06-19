# using functions
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
x = int(input("enter the number"))
print(fact(x))

# with out functions
num = int(input("enter the value : "))
f = 1
for i in range(1, num+1):
    f = f*i
print(f)