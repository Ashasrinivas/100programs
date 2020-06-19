def maxlen():
    a = input("enter the a value : ")
    b = input("enter the b value : ")
    length_a = len(a)
    length_b = len(b)
    if length_a > length_b:
        print(a)
    elif length_a < length_b:
        print(b)
    else:
       print(a)
       print(b)
maxlen()



# def printValue(s1,s2):
#     len1 = len(s1)
#     len2 = len(s2)
#     if len1>len2:
#         print(s1)
#     elif len2>len1:
#         print(s2)
#     else:
#         print(s1)
#         print(s2)
# printValue("11","13")
