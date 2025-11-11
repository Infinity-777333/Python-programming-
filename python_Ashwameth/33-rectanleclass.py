class rect:
    def __init__(self,len,br):
        self.len=len
        self.br=br

    def area(self):
        return self.len*self.br

    def perimeter(self):
        return 2*(self.len+self.br)

r1=rect(10,20)
r2=rect(15,18)
print("Area of first rectangle1:",r1.area())
print("Area of first rectangle2:",r2.area())
print("\n\n")
print("Perimeter of rectangle1:",r1.perimeter())
print("Perimeter of rectangle2:",r2.perimeter())

    
if(r1.area()>r2.area()):
    
    print("Highest area is:",r1.area())

else:
    
    print("Highest area is:",r2.area())


                  

