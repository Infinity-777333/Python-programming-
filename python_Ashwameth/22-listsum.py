num_list=[]
n=int(input("Enter the number of values in list:"))
if n>1:
    print("Enter the elements in the list")
    for i in range(n):
        val=int(input())
        num_list.append(val)
    total=0
    for item in num_list:
        
        total=total+item

    print("Sum of elements in list",total)

else:
    print("Invalid input")
    
