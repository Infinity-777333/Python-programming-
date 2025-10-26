import operator
mydict={}
while True:
      key=input("Enter the key(or'q' for quit):")
      if key=='q':
       break
      value=int(input("Enter the value:"))
      mydict[key]=value
print("The original dictionary is:",mydict)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1)))
print("Dictionary in asending order by value:",sd)
sd=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary in desending order by value:",sd)

