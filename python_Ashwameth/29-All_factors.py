num=int(input("Enter the number:"))
factor=[]
for i in range(1,num+1):
      if num%i==0:
         factor.append(i)
         
print(f"The factors of {num} are {factor}")         
