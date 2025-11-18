class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
    def __add__(self,other):
        hr=self.h+other.h
        mit=self.m+other.m
        sec=self.s+other.s

        mit=mit+int(sec/60)
        sec=sec%60
        hr=hr+int(hr/60)
        mit=mit%60

        return Time(hr,mit,sec)

    def display(self):
        print(f"{self.h}:{self.m}:{self.s}")

print("Time 1")
h1=int(input("Enter the hour:"))
m1=int(input("Enter the minute:"))
s1=int(input("Enter the second:"))

print("\nTime 2")
h2=int(input("Enter the hour:"))
m2=int(input("Enter the minute:"))
s2=int(input("Enter the second:"))



r1=Time(h1,m1,s1)
r2=Time(h2,m2,s2)
r3=r1+r2

print("\nTime 1=",end=" ")
r1.display()
print("Time 2=",end=" ")
r2.display()
print("Sum=",end=" ")
r3.display()
