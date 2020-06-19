import re
email_add = input("enter your email address : ")
patterrn1 = "(\D+)@((\D+\.)+(com))"
if re.match(patterrn1, email_add):
    em = email_add.split('@')
    print(em)
    domain = em[1]
    print(domain)
    dom = domain.split('.')[0]
    print(dom)
    if dom.isalpha():
        print("domain name is" , dom)
    else:
        print("invalid username")
else:
    print("invalid email")

