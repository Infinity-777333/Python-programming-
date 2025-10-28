step=5
#upper part of pyramid
for i in range(step+1):
     for j in range(i):
         print("*",end=" ")
         
     print()
#lower partr of pyramid
for i in range(step-1,0,-1):
       for i in range(i):
          print("*",end=" ")
       print()     
 
