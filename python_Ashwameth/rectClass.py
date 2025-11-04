class Rect:
    def __init__(self,l,b):
        self.l = l
        self.b= b

    def area(self):
        return self.l * self.b



    def peremeter(self):
        return 2 * (self.l + self.b)


r1 = Rect(10,15)
r2 = Rect(20,40)
print(r1.area())
print(r2.area())
print(r1.peremeter())
max = r1.area() if r1.area()> r2.area() else r2.area()
print("Greater area is " + str(max))

                  
