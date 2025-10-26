clrs=[]
count=int(input("Enter the numbers of colors:"))
print("Enter the colors:")
for x in range(count):
        color=input()
        clrs.append(color)
print("First color:",clrs[0],"     last color:",clrs[count-1])
