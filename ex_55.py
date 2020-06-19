def divide(x, y):
    try:
        result = x//y
        print("your answer is : ", result)
    except ZeroDivisionError:
        print("yoyu are dividing by zero")
    
divide(3,0)
