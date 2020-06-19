n = input("enter the sentence : ")
word = [x for x in n.split(" ")]
print(",".join(sorted(set(word))))