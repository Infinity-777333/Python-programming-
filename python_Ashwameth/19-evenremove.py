c=int(input("How many elements:"))
list1=[]
print("Enter the elements:")
for i in range(c):
    value=int(input())
    list1.append(value)
for i in list1[:] :
    if(i%2==0):
        list1.remove(i)

print("list without even numbers",list1)
    
