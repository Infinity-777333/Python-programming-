mydict1={}
print("Enter  the elements of first dict")
while True:
    key=input("Enter the key(or 'q' to quit):")
    if key=='q':
        break
    value=int(input("Enter the value:"))
    mydict1[key]=value

mydict2={}
print("Enter  the elements of second dict")
while True:
    key=input("Enter the key(or 'q' to quit):")
    if key=='q':
        break
    value=int(input("Enter the value:"))
    mydict2[key]=value

print("Merged  dict is:",mydict1|mydict2)
    
