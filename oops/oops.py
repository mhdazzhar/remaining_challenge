class student:
    def __int__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter the name")
        self.mark=int(input("enter the mark"))
    def putdetails(self):
        print(self.name,self.mark)
class churuli(student):
    def display(self):
        print("nee thankan chettante 1d")
class bigb(churuli):
    def bilal(self):
        print("i am mammootty")
class cia(bigb):
    def dq(self):
        print("i am dulquer")
obj=cia()
obj.getdetails()
obj.putdetails()
obj.display()
obj.bilal()
obj.dq()