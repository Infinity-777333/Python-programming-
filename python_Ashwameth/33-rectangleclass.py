class rect:
    def __init__(self,len,br):
        self.len=len
        self.br=br

    def area(self):
        return self.len*self.br

    def perimeter(self):
        return 2*(self.len+self.br)
print("Enter the length and breadth of first rectangle")
l1=int(input("Length:"))
b1=int(input("Breadth:"))
print("\n")

print("Enter the length and breadth of second rectangle")
l2=int(input("Length:"))
b2=int(input("Breadth:"))
print("\n")

r1=rect(l1,b1)
r2=rect(l2,b2)
print("Area of first rectangle:",r1.area())
print("Area of second rectangle:",r2.area())
print("\n\n")
print("Perimeter of first rectangle:",r1.perimeter())
print("Perimeter of second rectangle:",r2.perimeter())

print("\n")
if(r1.area()>r2.area()):
    
    print("Highest area is:",r1.area())

else:
    
    print("Highest area is:",r2.area())

