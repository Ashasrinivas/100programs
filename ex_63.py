# sum of series 1/2+2/3+3/4+....n/(n+1)
# when we give input value as 5 then the series will be 1/2+2/3+3/4+5/6

n = int(input("enter the value : "))
sum = 0.0
for i in range(1, n+1):
    sum = sum+((i)/(i+1))
print(sum)