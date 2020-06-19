class Person(object):
    def getgender(self):
        return "unknown"
class Male(Person):
    def getgender(self):
        return "male"
class Female(Person):
    def getgender(self):
        return "female"

#a = Person()
a = Male()
b = Female()
print(a.getgender())
print(b.getgender())
