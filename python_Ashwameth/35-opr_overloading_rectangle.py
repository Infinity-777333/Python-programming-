class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def __lt__(self,other):
        return self.area()<other.area()
r1=Rectangle(10,5)
r2=Rectangle(5,5)

if r1<r2:
    print("r1 has smaller area")
else:
    print("r2 has smaller area")
