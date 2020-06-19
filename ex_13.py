s = input()
digit = letter = 0
for c in s:
    if c.isdigit():
        digit = digit+1
    elif c.isalpha():
        letter = letter+1
    else:
        pass
print("LETTERS",letter)
print("DIGITS", digit)