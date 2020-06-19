import re
email_add = input()
pat2 = "(\D+)@((\D+\.)+(com))"
if re.match(pat2, email_add):
    em = email_add.split('@')
    if em[0].isalpha():
        print("username is : ", em[0])
    else:
        print("invalid username ")
else:
    print("invalid mail")

