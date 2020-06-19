# converting int to str
def value():
    n1 = int(input("enter the value : "))
    n2 = int(input("enter the value ; "))
    n3 = str(n1) + str(n2)
    print(n3)
    print(type(n3))
print(value())


# converting string to int
def printValue():
    s1 = input(("enter the  value : "))
    s2 = input("enter the value : ")
    print(type(s1))
    s3 = int(s1) + int(s2)
    print(int(s3))
    print(type(s3))
printValue()


# without usr input
def printValue(s1,s2):
    print(int(s1)+int(s2))
printValue("6","8")